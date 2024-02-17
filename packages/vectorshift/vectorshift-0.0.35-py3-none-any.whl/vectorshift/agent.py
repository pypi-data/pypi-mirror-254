
import json 
import requests
from pydantic import BaseModel

import vectorshift

from vectorshift.consts import API_AGENT_FETCH_ENDPOINT, API_AGENT_SAVE_ENDPOINT, API_AGENT_RUN_ENDPOINT

from vectorshift.tools import ToolDefinition, ParameterDefinition, ALL_TOOLS, ToolKit, TOOLKITS, DATALOADER_TOOLS, VectorDBToolKit
from pydantic import BaseModel, Field
from typing import Optional, Any, List

from vectorshift.vectorstore import VectorStore
import vectorshift.pipeline

from fastapi.encoders import jsonable_encoder

class Agent:
    def __init__(self, name: str, task: str, tools: list[ToolDefinition], llm: str = "gpt-3.5-turbo", framework: str = "ReAct", inputs: dict = None, outputs: dict = None, id : str = None):
        self.name = name
        self.task = task
        self.tools = tools
        self.llm = llm
        self.framework = framework
        self.inputs = inputs
        self.outputs = outputs
        self.id = id 

    @classmethod
    def from_json_rep(cls, json_data: dict[str, any]) -> 'Agent':
        return cls(
            name = json_data['name'],
            task = json_data['task'],
            tools = json_data['tools'], # use factory to get tools
            llm = json_data['llm'],
            framework = json_data['framework'],
            inputs = json_data['inputs'],
            outputs = json_data['outputs'],
            id = json_data['id']
        )
    
    @classmethod
    def from_tool_names(
        cls, 
        name: str, 
        task: str, 
        tool_names: list[str], 
        llm: str = "gpt-3.5-turbo", 
        framework: str = "ReAct", 
        inputs: dict = None, 
        outputs: dict = None, 
        id : str = None
    ) -> 'Agent':
        tools = ToolFactory.get_tools(tool_names)
        return cls(
            name = name,
            task = task,
            tools = tools,
            llm = llm,
            framework = framework,
            inputs = inputs,
            outputs = outputs,
            id = id
    )


    @staticmethod
    def from_json(json_str: str) -> 'Agent':
        json_data = json.loads(json_str)
        return Agent.from_json_rep(json_data)

    def to_json_rep(self) -> dict:
        return {
            'name': self.name,
            'task': self.task,
            'tools': {tool.name: tool.dict() for tool in self.tools}, 
            'llm': self.llm,
            'framework': self.framework,
            'inputs': self.inputs,
            'outputs': self.outputs
        }
    

    @staticmethod
    def fetch(agent_name: str = None, 
             agent_id: str = None, 
             username: str = None, 
             org_name: str = None, 
             public_key=None, 
             private_key=None) -> 'Agent':
        """Load an already existing agent from the VS platform, Specify the agent id, agent name or both.
        
        Args:
            agent_id (str): The ID of the agent to load.
            agent_name (str): The name of the agent to load.
            public_key (str): The public key for authentication.
            private_key (str): The private key for authentication.
        
        Returns:
            Agent: The loaded agent object.
        """
        if agent_id is None and agent_name is None:
            raise ValueError("Must specify either agent_id or agent_name.")
        
        response = requests.get(
            API_AGENT_FETCH_ENDPOINT,
            data={
                'agent_id': agent_id,
                'agent_name': agent_name,
                'username': username, 
                'org_name': org_name,
            },
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()
        return Agent.from_json_rep(response)
    
    
    def to_json(self) -> str:
        return json.dumps(self.to_json_rep(), indent=4)


    def save(self, public_key=None, private_key=None, update_existing=False) -> dict:
        """
        Save the agent to the VS platform. If update_existing is True, then will overrite an existing pipeline

        Args:
            update_existing (bool, optional): Update existing pipeline. Defaults to False.
        """
        if update_existing and not self.id:
            raise ValueError("Cannot update a agent that has not been saved yet.")
        
        if not update_existing:
            self.id  = None 

        response = requests.post(
            API_AGENT_SAVE_ENDPOINT,
            data={'agent': self.to_json()},
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()
        self.id = response.get('id')
        return response

    def run(self, inputs={}, public_key: str=None, private_key: str=None) -> dict:
        if not self.id:
            raise ValueError("Agent must be saved before it can be run.")
        
        response = requests.post(
            API_AGENT_RUN_ENDPOINT,
            data = ({
                'agent_id': self.id,
                'inputs': json.dumps(inputs),
            }),
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()
        return response

    def __repr__(self) -> str:
        return str(self.to_json_rep())
    

    def __str__(self) -> str:
        agent_str = f"Agent: {self.name}\n Task: {self.task}"
        agent_str += f"\n LL Model: {self.llm}"
        agent_str += f"\n Framework: {self.framework}"
        agent_str += f"\n Inputs: {self.inputs}"
        agent_str += f"\n Outputs: {self.outputs}"
        agent_str += "\n Tools: "
        for tool in self.tools.values():
            agent_str += f"\n\t Tool:{tool['name']}"
            agent_str += f"\n\t\t Description: {tool['description']}"
            agent_str += f"\n\t\t Type: {tool['type']}"
            agent_str += f"\n\t\t ID: {tool['id']}"
        return agent_str
    
# TODO below awkwardly has to be in this file to avoid a circular import


USER_OBJECT_CLASS_MAPPINGS = {
    "vectorstore": VectorStore,
    "pipeline": vectorshift.pipeline.Pipeline,
    "agent": Agent,
}


def convert_io_definition_to_parameter_definition(io_definition: dict) -> List[ParameterDefinition]:
    """
    Convert the inputs of a pipeline or agent to a parameter definition

    Args:
        io_definition (dict): Input/Output description

    Returns:
        List[ParameterDefinition]: Parameter definition


    Examples:
    io_definition = {
        "Query": {
        "name": "Query",
        "type": "Text"
        }
    }
    convert_io_definition_to_parameter_definition(io_definition)
    >>> [ParameterDefinition(name='Query', description="", type="string")]
    """
    parameter_definitions = []
    for name, definition in io_definition.items():
        parameter_definitions.append(ParameterDefinition(name=name, description=definition.get("description", ""), type="string"))
    return parameter_definitions



USER_DEFINED_TOOLS = {}


def register_user_defined_tool_type(tool_type: str):
    def decorator(tool_class):
        USER_DEFINED_TOOLS[tool_type] = tool_class
        tool_class.type = tool_type
        return tool_class
    return decorator

class UserDefinedToolDefinition(ToolDefinition):
    name: str
    description: str
    type: str
    id: str
    parameters: list[ParameterDefinition] = Field(default_factory=list)

    @classmethod
    def from_name(cls, name: str  = None, id: str = None, description: str = "", **kwargs):
        
        user_object = USER_OBJECT_CLASS_MAPPINGS[cls.type].fetch(name=name, id=id, **kwargs)
        return cls(
            name = user_object.name,
            description = user_object.description if not description else description, # Overwrite with custom description if provided, for agents description is task
            type = user_object.type,
            id = user_object.id,
        )


@register_user_defined_tool_type("vectorstore")
class VectorStoreToolDefinition(UserDefinedToolDefinition):

    @classmethod
    def from_name(cls, name: str  = None, id: str = None, description: str = "", **kwargs):
        user_object =  VectorStore.fetch(vectorstore_name=name, vectorstore_id=id, **kwargs)

        return cls(
            name = user_object.name,
            description = user_object.description if not description else description, 
            type = cls.type,
            id = user_object.id,
            parameters = [ParameterDefinition(name="query", description="query for vectorstore", type="string")]
        )


@register_user_defined_tool_type("agent")
class AgentToolDefinition(UserDefinedToolDefinition):

    @classmethod
    def from_name(cls, name: str  = None, id: str = None, description: str = "", **kwargs):
        user_object =  Agent.fetch(agent_name=name, agent_id=id, **kwargs)
        parameters = convert_io_definition_to_parameter_definition(user_object.inputs)

        return cls(
            name = user_object.name,
            description = user_object.task if not description else description, # Overwrite with custom description if provided, 
            type = cls.type,
            id = user_object.id,
            parameters = parameters
        )

@register_user_defined_tool_type("pipeline")
class PipelineToolDefinition(UserDefinedToolDefinition):

    @classmethod
    def from_name(cls, name: str  = None, id: str = None, description: str = "", **kwargs):
                # IF it is an agent or a pipline, the inputs and outputs are defined by the agent or pipline
        user_object = vectorshift.pipeline.Pipeline.fetch(pipeline_name=name, pipeline_id = id, **kwargs)
        parameters = convert_io_definition_to_parameter_definition(user_object.inputs)

        return cls(
            name = user_object.name,
            description = user_object.description if not description else description, 
            type = cls.type,
            id = user_object.id,
            parameters = parameters
        )
    

class ToolFactory:

    @staticmethod
    def get_tool(tool_name: str) -> ToolDefinition:
        return ALL_TOOLS[tool_name]()

    @staticmethod
    def get_toolkit(toolkit_name: str) -> ToolKit:
        return TOOLKITS[toolkit_name]()


    @staticmethod
    def get_tools(tool_names: list[str]) -> list[ToolDefinition]:
        tool_definitions = []
        for tool_name in tool_names:
            tool_definitions.append(ToolFactory.get_tool(tool_name))
            if tool_name in DATALOADER_TOOLS:
                # Add the tools in the vectordb toolkit to be able to load and query the documents
                tool_definitions.extend(VectorDBToolKit().tools)
            if tool_name == "image_generation":
                # Add the save file tool to be able to save the image
                tool_definitions.append(ToolFactory.get_tool('save_file'))
        return tool_definitions