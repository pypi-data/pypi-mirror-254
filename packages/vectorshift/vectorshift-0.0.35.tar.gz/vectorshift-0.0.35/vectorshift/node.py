# definitions of all particular node classes
import re
import requests

import vectorshift
from vectorshift.consts import *
from vectorshift.pipeline_data_types import *
from vectorshift.node_utils import * 

# To add a new node class:
# - define the class (using subclassing as appropriate), ensuring the functions
#   indicated in NodeTemplate are satisfied 
# - add appropriate typechecking for any constructor inputs that are 
#   NodeOutputs in validate_node_inputs
# - add any necessary details in pipeline.py

# Helper to check the well-formedness of the types of all NodeTemplate inputs 
# passed into a node. Assumes the inputs must have been initialized (i.e. 
# the node should not have any empty inputs).
# Note: we could also make this a method within NodeTemplate.
def validate_node_inputs(node: NodeTemplate) -> None:
    node_type = node.node_type
    inputs = node._inputs
    if not node_type:
        raise Exception('Node type not specified')

    # check against the node_type and the class
    match node_type:
        case 'customInput':
            assert(type(node) == InputNode)
        case 'customOutput':
            assert(type(node) == OutputNode)
            assert(len(inputs['value']) == 1)
            input = inputs['value'][0]
            if node.output_type == 'file':
                check_type('OutputNode', input.output_data_type, FILE_TYPE)
            elif node.output_type in ['text', 'formatted_text']:
                check_type('OutputNode', input.output_data_type, TEXT_TYPE)
        case 'text':
            assert(type(node) == TextNode)
            for var_name, v in inputs.items():
                assert(len(v) == 1)
                check_type(f'TextNode input {var_name}', v[0].output_data_type, TEXT_TYPE)
        case 'file':
            assert(type(node) == FileNode)
        case 'pipeline':
            assert(type(node) == PipelineNode)
            pipeline_inputs = node.pipeline_json['inputs'].values() 
            # Overall pipeline inputs and outputs are, for now, only of
            # text or file types.
            for i in pipeline_inputs:
                # this shouldn't happen as there's a check in the constructor
                # that the NodeOutput keys match the 'name' fields of each
                # input's JSON representation
                input_name = i['name']
                if input_name not in inputs.keys():
                    raise ValueError(f'PipelineNode: missing input {input_name}.')
                assert(len(inputs[input_name]) == 1)
                node_input = inputs[input_name][0]
                if i['type'] == 'Text':
                    check_type(f'PipelineNode input {input_name}', node_input.output_data_type, TEXT_TYPE)
                elif i['type'] == 'File':
                    check_type(f'PipelineNode input {input_name}', node_input.output_data_type, FILE_TYPE)
                else:
                    raise ValueError(f"PipelineNode: invalid input type input {input_name}: {i['type']}") 
        case 'integration':
            # Using AnyType() for now
            for input_name, l in inputs.items():
                for o in l:
                    check_type(f'Integration node input {input_name}', o.output_data_type, AnyType())
        case 'transformation':
            assert(type(node) == TransformationNode)
            # Using AnyType() for now
            for input_name, l in inputs.items():
                for o in l:
                    check_type(f'TransformationNode input {input_name}', o.output_data_type, AnyType())
        case 'fileSave':
            assert(type(node) == FileSaveNode)
            # inputs to fileSave should be of file or list[file] type
            assert(len(inputs['name']) == 1)
            check_type('FileSaveNode input name', inputs['name'][0].output_data_type, TEXT_TYPE)
            for o in inputs['files']:
                check_type('FileSaveNode input files', o.output_data_type, UnionType(FILE_TYPE, ListType(FILE_TYPE)))
        case 'stickyNote': assert(type(node) == StickyNoteNode)
        case 'llmOpenAI':
            assert(type(node) == OpenAILLMNode)
            for k, v in inputs.items():
                assert(len(v) == 1)
                check_type(f'OpenAILLMNode input {k}', v[0].output_data_type, TEXT_TYPE)
        case 'llmAnthropic' | 'llmCohere' | 'llmAWS' | 'llmLlama' | 'llmOpenSource' | 'llmGoogle':
            assert(type(node) == PromptLLMNode or issubclass(type(node), PromptLLMNode))
            for k, v in inputs.items():
                assert(len(v) == 1)
                check_type(f'OpenAILLMNode input {k}', v[0].output_data_type, TEXT_TYPE)
        case 'imageGen':
            assert(type(node) == ImageGenNode)
            assert(len(inputs['prompt']) == 1)
            check_type('ImageGenNode input prompt', inputs['prompt'][0].output_data_type, TEXT_TYPE)
        case 'speechToText':
            assert(type(node) == SpeechToTextNode)
            assert(len(inputs['audio']) == 1)
            check_type('ImageGenNode input audio', inputs['audio'][0].output_data_type, AUDIO_FILE_TYPE)
        case 'vectorDBLoader':
            assert(type(node) == VectorDBLoaderNode)
            for o in inputs['documents']:
                check_type('VectorDBLoaderNode input documents', o.output_data_type, TEXT_TYPE)
        case 'vectorDBReader':
            assert(type(node) == VectorDBReaderNode)
            assert(len(inputs['query']) == 1)
            assert(len(inputs['database']) == 1)
            check_type('VectorDBReaderNode input query', inputs['query'][0].output_data_type, TEXT_TYPE)
            check_type('VectorDBReaderNode input database', inputs['database'][0].output_data_type, VECTOR_DB_TYPE)
        case 'vectorQuery':
            assert(type(node) == VectorQueryNode)
            assert(len(inputs['query']) > 0)
            assert(len(inputs['documents']) > 0)
            for o in inputs['query']:
                check_type('VectorQueryNode input query', o.output_data_type, TEXT_TYPE)
            for o in inputs['documents']:
                check_type('VectorQueryNode input documents', o.output_data_type, TEXT_TYPE)
            if 'filter' in inputs.keys():
                check_type('VectorQueryNode input filter', inputs['filter'][0].output_data_type, TEXT_TYPE)
        case 'vectorStore':
            assert(type(node) == VectorStoreNode)
            assert(len(inputs['query']) == 1)
            check_type('VectorStoreNode input query', inputs['query'][0].output_data_type, TEXT_TYPE)
            if 'filter' in inputs.keys():
                check_type('VectorStoreNode input filter', inputs['filter'][0].output_data_type, TEXT_TYPE)
        case 'chatMemory':
            assert(type(node) == ChatMemoryNode)
        case 'condition':
            assert(type(node) == LogicConditionNode)
            # TODO: refactor according to Alex's ultimate implementation in 
            # the API. For now, we just mandate that any input names that 
            # appear in a condition are text.
            input_names = inputs.keys()
            conditional_input_names = set()
            for c in node.conditions:
                for n in input_names:
                    if n in c[0]:
                        conditional_input_names.add(n)
            for cnd_input_name in list(conditional_input_names):
                check_type(f'LogicConditionNode input {cnd_input_name}', inputs[cnd_input_name][0].output_data_type, TEXT_TYPE)
        case 'merge':
            assert(type(node) == LogicMergeNode)
        # TODO: TBD on typechecking for agents
        case 'agent':
            assert(type(node) == AgentNode)
            agent_inputs = node.agent_json['inputs'].values()
            for input in agent_inputs:
                input_name = input['name']
                if input_name not in inputs.keys():
                    raise ValueError(f'AgentNode missing input {input_name}.')
                assert(len(inputs[input_name]) == 1)
                node_input = inputs[input_name][0]
                if input['type'] == 'Text':
                    check_type(f'AgentNode input {input_name}', node_input.output_data_type, TEXT_TYPE)
                elif input['type'] == 'File':
                    check_type(f'AgentNode input {input_name}', node_input.output_data_type, FILE_TYPE)
                else:
                    raise ValueError(f"Invalid input type to AgentNode input {input_name}: {input['type']}")
        case 'splitText':
            assert(type(node) == SplitTextNode)
            assert(len(inputs['text']) == 1)
            check_type('SplitTextNode input text', inputs['text'][0].output_data_type, TEXT_TYPE)
        case 'dataLoader':
            # Asserts that the right input names are in inputs,
            # as it's possible to create a DataLoaderNode directly with
            # possibly-arbitrary input names. Also, some data loaders may
            # require exactly one input.
            assert(type(node) == DataLoaderNode or issubclass(type(node), DataLoaderNode))
            match node.loader_type:
                case 'File':
                    assert('file' in inputs and len(inputs['file']) > 0)
                    for f_input in inputs['file']:
                        check_type(
                            'File loader node', 
                            f_input.output_data_type, 
                            UnionType(
                                FILE_TYPE, ListType(FILE_TYPE), 
                                TEXT_TYPE, ListType(TEXT_TYPE)
                            )
                        )
                case 'CSV Query':
                    assert('query' in inputs and len(inputs['query']) == 1)
                    assert('csv' in inputs and len(inputs['csv']) == 1)
                    check_type(
                        'CSV Query loader node input query', 
                        inputs['query'][0].output_data_type, 
                        TEXT_TYPE
                    )
                    check_type(
                        'CSV Query loader node input csv',
                        inputs['csv'][0].output_data_type,
                        CSV_FILE_TYPE
                    )
                case 'URL':
                    assert('url' in inputs and len(inputs['url']) == 1)
                    check_type(
                        'URL loader node input url',
                        inputs['url'][0].output_data_type,
                        URL_TYPE
                    )
                case 'Wikipedia':
                    assert('query' in inputs and len(inputs['query']) == 1)
                    check_type(
                        'Wikipedia loader node input query', 
                        inputs['query'][0].output_data_type, 
                        TEXT_TYPE
                    )
                case 'YouTube':
                    assert('url' in inputs and len(inputs['url']) == 1)
                    check_type(
                        'YouTube loader node input url',
                        inputs['url'][0].output_data_type,
                        UnionType(URL_TYPE, ListType(URL_TYPE))
                    )
                case 'Arxiv':
                    assert('query' in inputs and len(inputs['query']) == 1)
                    check_type(
                        'Arxiv loader node input query', 
                        inputs['query'][0].output_data_type, 
                        TEXT_TYPE
                    )
                case 'SerpAPI':
                    assert('apiKey' in inputs and len(inputs['apiKey']) == 1)
                    assert('query' in inputs and len(inputs['query']) == 1)
                    check_type(
                        'SerpAPI loader node input apiKey', 
                        inputs['apiKey'][0].output_data_type, 
                        TEXT_TYPE
                    )
                    check_type(
                        'SerpAPI loader node input query',
                        inputs['query'][0].output_data_type,
                        TEXT_TYPE
                    )
                case 'Git':
                    assert('repo' in inputs and len(inputs['repo']) == 1)
                    check_type(
                        'Git loader node input repo',
                        inputs['repo'][0].output_data_type,
                        URL_TYPE
                    )
                # DEPRECATED
                case 'Notion':
                    assert('token' in inputs and len(inputs['token']) == 1)
                    assert('database' in inputs and len(inputs['database']) == 1)
                    check_type(
                        'Notion loader node input token', 
                        inputs['token'][0].output_data_type, 
                        TEXT_TYPE
                    )
                    check_type(
                        'Notion loader node input database',
                        inputs['database'][0].output_data_type,
                        TEXT_TYPE
                    )
                # DEPRECATED
                case 'Confluence':
                    assert('username' in inputs and len(inputs['username']) == 1)
                    assert('apiKey' in inputs and len(inputs['apiKey']) == 1)
                    assert('url' in inputs and len(inputs['url']) == 1)
                    check_type(
                        'Confluence loader node input username', 
                        inputs['username'][0].output_data_type, 
                        TEXT_TYPE
                    )
                    check_type(
                        'Confluence loader node input apiKey',
                        inputs['apiKey'][0].output_data_type,
                        TEXT_TYPE
                    )
                    check_type(
                        'Confluence loader node input url', 
                        inputs['url'][0].output_data_type, 
                        TEXT_TYPE
                    )
        case _:
            raise ValueError(f'Unrecognized node type value {node_type} (node class {type(node)})')
    return

###############################################################################
# HOME                                                                        #
###############################################################################

# Input nodes themselves don't have inputs; they define the start of a pipeline.
class InputNode(NodeTemplate):
    def __init__(self, name:str, input_type:str, **kwargs):
        super().__init__()
        self.node_type = 'customInput'
        self.category = self.task_name = 'input'
        self.name = name
        # Text or File
        if input_type not in INPUT_NODE_TYPES:
            raise ValueError(f'InputNode: input type {input_type} not supported.')
        self.input_type = input_type
        # InputNodes themselves don't take inputs
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_name(self, name:str): self.name = name
    
    def set_input_type(self, input_type:str):
        if input_type not in INPUT_NODE_TYPES:
            raise ValueError(f'InputNode: input type {input_type} not supported.')
        self.input_type = input_type 

    def init_args_strs(self):
        return [
            f"name='{self.name}'", 
            f"input_type='{self.input_type}'"
        ]
        
    def output(self) -> NodeOutput:
        # Input nodes can only return files or text for now
        output_data_type = FILE_TYPE if self.input_type == 'file' else TEXT_TYPE
        return NodeOutput(
            source=self, 
            output_field='value', 
            output_data_type=output_data_type
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
        
    def _to_json_rep(self):
        return {
            'inputName': self.name,
            'inputType': self.input_type.capitalize(),
        }
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'InputNode':
        return InputNode(
            name=json_data['data']['inputName'], 
            input_type=json_data['data']['inputType'].lower(),
            skip_typecheck=True
        )

# Outputs are the end of the pipeline and so only take inputs.
class OutputNode(NodeTemplate):
    def __init__(self, name:str, output_type:str, input:NodeOutput, **kwargs):
        super().__init__()
        self.node_type = 'customOutput'
        self.category = self.task_name = 'output'
        self.name = name
        # Text or File
        if not output_type.lower() in OUTPUT_NODE_TYPES:
            raise ValueError(f'OutputNode: output type {output_type} not supported.')
        self.output_type = output_type
        self._inputs = {'value': [input]}
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_name(self, name:str): self.name = name
    
    def set_output_type(self, output_type:str):
        if output_type not in OUTPUT_NODE_TYPES:
            raise ValueError(f'InputNode: input type {output_type} not supported.')
        self.output_type = output_type 
    
    def set_input(self, input:NodeOutput):
        old_input = self._inputs['value']
        self._inputs['value'] = [input]
        try:
            validate_node_inputs(self)
        except ValueError as err:
            self._inputs['value'] = old_input
            raise err

    def init_args_strs(self):
        input = self._inputs['value'][0]
        return [
            f"name='{self.name}'", 
            f"output_type='{self.output_type}'",
            format_node_output_with_name('input', input)
        ]

    def outputs(self): return None
    
    def _to_json_rep(self):
        return {
            'outputName': self.name,
            'outputType': self.output_type.capitalize(),
        }
        
    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'OutputNode':
        return OutputNode(
            name=json_data['data']['outputName'], 
            output_type=json_data['data']['outputType'].lower(),
            input=None,
            skip_typecheck=True
        )

# Text data. Can be blocks of text in themselves, or also take in outputs of
# other text nodes as inputs (e.g. with text variables like {{Context}}, 
# {{Task}}). In the latter case, an additional argument text_inputs should
# be passed in as a dict of input variables to Outputs.
class TextNode(NodeTemplate):
    def __init__(self, text:str, text_inputs:dict[str, NodeOutput]={},
            format_text:bool=True, **kwargs):
        super().__init__()
        self.node_type = 'text'
        self.category = 'task'
        self.task_name = 'text'
        self.text = text
        # if there are required inputs, they should be of the form {{}} - each
        # of them is a text variable
        self.text_vars = find_text_vars(self.text)
        self.format_text = format_text
        
        # wrap each NodeOutput into a singleton list to fit the type. 
        # if there are variables, we expect them to be matched with inputs
        # they should be passed in a dictionary with the
        # arg name text_inputs. E.g. {"Context": ..., "Task": ...}
        # make it possible for the user to supply extraneous inputs, but
        # only store NodeOutputs corresponding to text vars in self._inputs
        self.all_inputs = {k: [v] for k, v in text_inputs.items()}

        check_text_vars(self.text_vars, self.all_inputs.keys())
        self._inputs = {
            k: v for k, v in self.all_inputs.items() if k in self.text_vars
        }
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)
    
    # if the new text adds variables, the proper pattern of usage is to first 
    # add an input for that variable, then calling set_text
    def set_text(self, text:str):
        self.text = text 
        self.text_vars = find_text_vars(self.text)
        check_text_vars(self.text_vars, self.all_inputs.keys())
        # the actual text variables used may have changed
        self._inputs = {
            k: v for k, v in self.all_inputs if k in self.text_vars
        }

    def set_format_text(self, format_text:bool): self.format_text = format_text
    
    def set_text_input(self, text_var:str, input:NodeOutput):
        check_type(f'TextNode input {text_var}', input.output_data_type, TEXT_TYPE)
        self.all_inputs[text_var] = [input]

    def remove_text_input(self, text_var:str):
        if text_var in self.text_vars:
            raise ValueError(f'TextNode: text variable {text_var} is being used.')
        del self.all_inputs[text_var]
    
    def set_text_inputs(self, text_inputs:dict[str, NodeOutput]):
        check_text_vars(self.text_vars, text_inputs.keys())
        for k, v in text_inputs.items():
            check_type(f'TextNode input {k}', v.output_data_type, TEXT_TYPE)
        self.all_inputs = {k: [v] for k, v in text_inputs}
        self._inputs = {
            k: v for k, v in self.all_inputs if k in self.text_vars
        }
            
    def init_args_strs(self):
        return [
            f"text='{self.text}'".replace('\n', '\\n'),
            f"text_inputs={format_node_output_dict(self._inputs)}"
        ]
            
    def output(self) -> NodeOutput: 
        return NodeOutput(
            source=self, 
            output_field='output', 
            output_data_type=TEXT_TYPE
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
        
    def _to_json_rep(self):
        input_names = self.text_vars if len(self.text_vars) > 0 else None
        return {
            'text': self.text,
            'inputNames': input_names,
            'formatText': self.format_text,
        }
        
    def _from_json_rep(json_data:dict) -> 'TextNode':
        text_inputs = {}
        for name in json_data['data'].get('inputNames', []):
            text_inputs[name] = None
        return TextNode(
            text=json_data['data']['text'],
            text_inputs=text_inputs,
            skip_typecheck=True
        )

# Nodes representing file data, taking no inputs.
### USES USER-CREATED OBJECT - see comments in VectorStoreNode
class FileNode(NodeTemplate):
    def __init__(self, file_names:list[str], process_files:bool=True, 
            chunk_size:int=DEFAULT_CHUNK_SIZE,
            chunk_overlap:int=DEFAULT_CHUNK_OVERLAP, 
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__()
        self.node_type = 'file'
        self.category = 'task'
        self.task_name = 'file'
        if file_names is None or file_names == []:
            raise ValueError('FileNode: file names must be specified.')
        self.file_names = file_names
        self.process_files = process_files
        if chunk_size < 1 or chunk_size > 4096:
            raise ValueError(f'FileNode: invalid chunk_size value.')
        if chunk_overlap < 0: raise ValueError('FileNode: invalid chunk_overlap value.')
        if chunk_overlap >= chunk_size:
            raise ValueError(f'FileNode: chunk_overlap must be smaller than chunk_size.')
        self.chunk_size, self.chunk_overlap = chunk_size, chunk_overlap
        self._public_key = public_key or vectorshift.public_key
        self._private_key = private_key or vectorshift.private_key
        # files take no inputs
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_file_names(self, file_names:list[str]):
        if file_names is None or file_names == []:
            raise ValueError('FileNode: file names must be specified.')
        self.file_names = file_names
    
    def set_process_files(self, process_files:bool):
        self.process_files = process_files 

    # TODO: refactor setters for attrs shared across node classes
    def set_chunk_size(self, chunk_size:int):
        if chunk_size < 1 or chunk_size > 4096:
            raise ValueError(f'FileNode: invalid chunk_size value.')
        self.chunk_size = chunk_size 

    def set_chunk_overlap(self, chunk_overlap:int):
        if chunk_overlap < 0: raise ValueError('FileNode: invalid chunk_overlap value.')
        if chunk_overlap >= self.chunk_size:
            raise ValueError(f'FileNode: chunk_overlap must be smaller than chunk_size.')
        self.chunk_overlap = chunk_overlap
    
    def set_api_key(self, public_key:str, private_key:str):
        self._public_key = public_key
        self._private_key = private_key

    def init_args_strs(self):
        return [
            f'file_names={self.file_names}',
            f'process_files={self.process_files}', 
            f'chunkSize={self.chunk_size}',
            f'chunkOverlap={self.chunk_overlap}',
            f"public_key={nullable_str(self._public_key)}",
            f"private_key={nullable_str(self._private_key)}"
        ]

    def output(self) -> NodeOutput:
        output_data_type = ListType(DOCUMENT_TYPE) if self.process_files else ListType(FILE_TYPE)
        return NodeOutput(
            source=self,
            output_field='files',
            output_data_type=output_data_type
        )

    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self):
        if self._public_key is None or self._private_key is None:
            raise ValueError('FileNode: API key required to fetch files.')
        # Note: there's currently no way in the API code to get files owned 
        # by another user, nor is there a way to get files by their ID.
        response = requests.get(
            API_FILE_FETCH_ENDPOINT,
            data={
                'file_names': self.file_names,
            },
            headers={
                'Public-Key': self._public_key,
                'Private-Key': self._private_key
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error fetching files: {response.text}')
        # list of JSONs for each file
        files_json = response.json()
        return {
            'selectedFiles': files_json, 
            'processFiles': self.process_files,
            'chunkSize': self.chunk_size,
            'chunkOverlap': self.chunk_overlap,
        }

    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'FileNode':
        file_names = [
            file_data['name'] \
                 for file_data in json_data['data'].get('selectedFiles', [])
        ]
        return FileNode(
            file_names=file_names,
            process_files=json_data['data']['processFiles'],
            chunk_size=json_data['data']['chunkSize'],
            chunk_overlap=json_data['data']['chunkOverlap'],
            skip_typecheck=True
        )

# Nodes representing entire other pipelines, a powerful tool for abstraction.
# When the node is executed, the pipeline it represents is executed with the
# supplied inputs, and the overall pipeline's output becomes the node's output.
### USES USER-CREATED OBJECT - see comments in VectorStoreNode
class PipelineNode(NodeTemplate):
    def init_pipeline_data(self, pipeline_id:str, pipeline_name:str, 
                           username:str, org_name:str, 
                           inputs=dict[str, NodeOutput]):
        # We'd like to know what the input and output names are upon 
        # initialization so we can validate that the inputs dict matches up.
        # So the API call to get the pipeline JSON is located in the
        # constructor here (compare to other nodes, where it's in _to_json_rep)
        if self._public_key is None or self._private_key is None:
            raise ValueError('PipelineNode: API key required to fetch pipeline.')
        response = requests.get(
            API_PIPELINE_FETCH_ENDPOINT,
            data={
                'pipeline_id': pipeline_id,
                'pipeline_name': pipeline_name,
                'username': username,
                'org_name': org_name,
            },
            headers={
                'Public-Key': self._public_key or vectorshift.public_key,
                'Private-Key': self._private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(response.text)
        # No need to construct a Pipeline object here.
        self.pipeline_json:dict = response.json()
        self.pipeline_id = self.pipeline_json['id']
        self.pipeline_name = self.pipeline_json['name']
        # The list of inputs provided should have keys matching the input names
        # defined by the integration function
        input_names = [
            i['name'] for i in self.pipeline_json['inputs'].values()
        ]
        if sorted(list(inputs.keys())) != sorted(input_names):
            raise ValueError(f'PipelineNode: inputs do not match expected input names: expected f{input_names}')

        self._inputs = {
            input_name: [inputs[input_name]] for input_name in input_names
        }

    def __init__(self, pipeline_id:str=None, pipeline_name:str=None, 
            inputs=dict[str, NodeOutput],
            username:str=None, org_name:str=None,
            public_key:str=None, private_key:str=None, 
            batch_mode:bool = False, **kwargs):
        super().__init__()
        self.node_type = 'pipeline'
        self.category = self.task_name = 'pipeline'
        if pipeline_name is None and pipeline_id is None:
            raise ValueError('PipelineNode: either the pipeline ID or name should be specified.')
        self.pipeline_id = pipeline_id 
        self.pipeline_name = pipeline_name 
        self.username = username
        self.org_name = org_name 
        self._public_key = public_key or vectorshift.public_key
        self._private_key = private_key or vectorshift.private_key
        self.batch_mode = batch_mode 

        # set the inputs and outputs
        self.init_pipeline_data(pipeline_id, pipeline_name, username, org_name, inputs)

        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)
    
    def set_batch_mode(self, batch_mode:bool):
        self.batch_mode = batch_mode

    def set_input(self, input_name:str, input:NodeOutput):
        if input_name not in self._inputs.keys():
            raise ValueError(f'PipelineNode: Invalid input name {input_name}.')
        old_input = self._inputs[input_name]
        self._inputs[input_name] = [input] 
        try:
            validate_node_inputs(self)
        except ValueError as err:
            self._inputs[input_name] = old_input
            raise err

    def set_inputs(self, inputs:dict[str, NodeOutput]):
        if sorted(inputs.keys()) != sorted(self._inputs.keys()):
            raise ValueError(f'PipelineNode: Invalid input names provided.')
        old_inputs = self._inputs.copy()
        self._inputs = {
            k: [v] for k, v in inputs.items()
        } 
        try:
            validate_node_inputs(self)
        except ValueError as err:
            self._inputs = old_inputs
            raise err

    @staticmethod
    def from_pipeline_obj(pipeline_obj, 
                          inputs=dict[str, NodeOutput],
                          public_key=None, private_key=None) -> 'PipelineNode':
        if not pipeline_obj.id:
            print('PipelineNode: Pipeline object does not contain a required ID, which likely means that the pipeline has not yet been saved. Attempting to save the pipeline...')
            pipeline_obj.save(public_key, private_key)
            print('PipelineNode: Pipeline object successfully saved.')
        # This is inefficient right now, since we save (write to Mongo) and 
        # then immediately query the object (read from Mongo) in the 
        # constructor.
        return PipelineNode(
            pipeline_id=pipeline_obj.id,
            pipeline_name=pipeline_obj.name,
            inputs=inputs,
            public_key=public_key, 
            private_key=private_key
        )

    def init_args_strs(self):
        return [
            f"pipeline_id={nullable_str(self.pipeline_id)}",
            f"pipeline_name={nullable_str(self.pipeline_name)}",
            f'inputs={format_node_output_dict(self._inputs)}',
            f"username={nullable_str(self.username)}",
            f"org_name={nullable_str(self.org_name)}",
            f"public_key={nullable_str(self._public_key)}",
            f"private_key={nullable_str(self._private_key)}",
            f'batch_mode={self.batch_mode}'
        ]

    def set_api_key(self, public_key:str, private_key:str) -> None:
        self._public_key = public_key
        self._private_key = private_key

    def outputs(self):
        os = {}
        for o in self.pipeline_json['outputs'].values():
            output_field = o['name']
            # Pipelines can only return files or text for now
            # note: these correspond with how the output type for an OutputNode
            # is stored in Mongo, which is capitalized 
            output_data_type = None
            if o['type'] == 'File':
                output_data_type = FILE_TYPE 
            elif o['type'] in ['Text', 'Formatted Text']:
                output_data_type = TEXT_TYPE 
            else:
                raise ValueError(f"PipelineNode: invalid pipeline output type {o['type']}")
            os[output_field] = NodeOutput(
                source=self, 
                output_field=output_field, 
                output_data_type=output_data_type
            )
        return os

    def _to_json_rep(self):
        pipeline_field_json = {
            # TODO: To my knowledge there is no way for the API to currently
            # return the "category" of a pipeline (favorite, my, imported etc.)
            # But this is stored in a pipeline node's representation as-is 
            # right now. For now I'm just excluding the field, as it doesn't 
            # seem to be used.
            'id': self.pipeline_json['id'],
            'name': self.pipeline_json['name'],
            'inputs': self.pipeline_json['inputs'],
            'outputs': self.pipeline_json['outputs'],
            # TODO: we just use the name as a placeholder; if this field is 
            # important we'll have to figure out a way to determine whether or
            # not the user/org name in this pipeline is different from the 
            # user/org name of whoever is writing this code (perhaps through
            # the Config class?). Same issue in TransformationNode.
            'displayName': self.pipeline_json['name']
        }

        return {
            'pipeline': pipeline_field_json,
            'batchMode': self.batch_mode,
        }

    @staticmethod
    def _from_json_rep(json_data:dict) -> 'PipelineNode':
        inputs = {}
        for i in json_data['data']['pipeline'].get('inputs', {}).values():
            inputs[i['name']] = [None]
        return PipelineNode(
            pipeline_id=json_data['data']['pipeline']['id'],
            pipeline_name=json_data['data']['pipeline']['name'],
            # We don't have a way to recover the username/org name, or the 
            # API key
            inputs=inputs,
            skip_typecheck=True
        )
    
# Integrations with third parties.
### USES USER-CREATED OBJECTS - see comments in VectorStoreNode
class IntegrationNode(NodeTemplate):
    def __init__(self, integration_type:str, integration_name:str, 
            function:str, inputs=dict[str, list[NodeOutput]],
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__()
        self.node_type = 'integration'
        self.category = 'integration'
        # task_name is retrieved from the specific integration parameters
        self._public_key = public_key or vectorshift.public_key
        self._private_key = private_key or vectorshift.private_key

        # The specific integration is stored in two sub-fields under the 
        # data field in the node's JSON representation. One field contains 
        # details of the integration itself, which requires an API call to
        # retrieve the integration object from Mongo. The other contains 
        # details of the function to run with the integration, which defines
        # the inputs/outputs of the node and can be deduced from the 
        # constructor arguments provided.
        if integration_type not in INTEGRATION_PARAMS.keys():
            raise ValueError(f'IntegrationNode: invalid integration {integration_type}.')
        if function not in INTEGRATION_PARAMS[integration_type].keys():
            raise ValueError(f'IntegrationNode: invalid function {function} for integration {integration_type}.')
        self.integration_type = integration_type 
        self.integration_name = integration_name
        self.function = function
        self.function_params = INTEGRATION_PARAMS[self.integration_type][self.function]
        # add the function name to the function params
        self.function_params['name'] = self.function
        self.task_name = self.function_params['taskName']

        # The list of inputs provided should have keys matching the input names
        # defined by the integration function. 
        # Note: each input to an integration node could be a list of 
        # NodeOutputs (multiple in-edges to a node's input field, e.g. saving
        # multiple files to Drive at once). This is different from the input
        # structure for pipeline and transformation nodes.
        input_names = [i['name'] for i in self.function_params['inputs']]

        # Notion has a dynamic list of inputs
        if self.integration_type != 'Notion' or self.function != 'write_to_database':
            if sorted(list(inputs.keys())) != sorted(input_names):
                raise ValueError(f'IntegrationNode: inputs do not match expected input names: expected {input_names}')
        
        # Specific integrations require additional argument parameters passed
        # in via the constructor rather than NodeOutputs. We store these as
        # a dict.
        self.integration_specific_params = {}

        def handle_dynamic_inputs():
            # add dynamic inputs to input list
            dynamic_inputs = []
            for field in kwargs['database_fields']:
                dynamic_inputs.append({
                    'name': field,
                    'displayName': field,
                    'multiInput': False,
                })
            self.function_params['inputs'] = dynamic_inputs
            input_names = [
                i['name'] for i in self.function_params['inputs']
            ]
            return input_names

        if self.integration_type == 'Airtable' and self.function == 'read_tables':
            # Expects a list of dicts with base and table IDs and names for each
            # table to load from
            if not ('airtable_tables' in kwargs):
                raise ValueError('IntegrationNode: Airtable base and table names and IDs must be provided to read tables.')
            for t in kwargs['airtable_tables']:
                if 'base_id' not in t or 'base_name' not in t or 'table_id' not in t or 'table_id' not in t:
                    raise ValueError('IntegrationNode: missing base or table names or IDs in Airtable integration.') 
                self.integration_specific_params['selectedTables'] = \
                    kwargs['airtable_tables']
        elif self.integration_type == 'Notion' and self.function == 'write_to_database':
            # Expects a string containing the database_id to write to
            # Expects a list of strings which contain the fields of the database we will write to
            if not 'database_id' in kwargs or not 'database_fields' in kwargs:
                raise ValueError('IntegrationNode: Notion database_id and/or database_fields are missing,')
            self.integration_specific_params['database_id'] = kwargs['database_id']
            self.integration_specific_params['database_fields'] = kwargs['database_fields']
            
            input_names = handle_dynamic_inputs()
            # Validate that we receive an input for each database field
            for field in kwargs['database_fields']:
                if field not in list(inputs.keys()):
                    raise ValueError(f'IntegrationNode: Notion inputs do not match expected input names: expected {input_names}')

        self._inputs = {
            input_name: inputs[input_name] for input_name in input_names 
        }

        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_input(self, input_name:str, input:list[NodeOutput]):
        if input_name not in self._inputs.keys():
            raise ValueError(f'Invalid input name {input_name}.')
        old_input = self._inputs[input_name]
        self._inputs[input_name] = input
        try:
            validate_node_inputs(self)
        except ValueError as err:
            self._inputs[input_name] = old_input
            raise err

    def set_inputs(self, inputs:dict[str, list[NodeOutput]]):
        if sorted(inputs.keys()) != sorted(self._inputs.keys()):
            raise ValueError(f'Invalid input names provided.')
        old_inputs = self._inputs.copy()
        input_names = [i['name'] for i in self.function_params['inputs']]
        self._inputs = {
            input_name: inputs[input_name] for input_name in input_names 
        }
        try:
            validate_node_inputs(self)
        except ValueError as err:
            self._inputs = old_inputs
            raise err

    def set_api_key(self, public_key:str, private_key:str) -> None:
        self._public_key = public_key
        self._private_key = private_key

    def init_args_strs(self):
        args_strs = [
            f"integration_type='{self.integration_type}'",
            f"integration_name='{self.integration_name}'",
            f"function='{self.function}'",
            f"inputs={format_node_output_dict(self._inputs)}",
            f"public_key={nullable_str(self._public_key)}",
            f"private_key={nullable_str(self._private_key)}",
        ] 
        for k, v in self.integration_specific_params.items():
            args_strs.append(f"{k}={v}")
        return args_strs

    def outputs(self):
        os = {}
        for o in self.function_params['outputs']:
            output_field = o['name']
            os[output_field] = NodeOutput(
                source=self, 
                output_field=output_field,
                # TODO: start storing types with integration functions on frontend
                # Using AnyType() for now
                output_data_type=AnyType()
            )
        return os
    
    def _to_json_rep(self):
        if self._public_key is None or self._private_key is None:
            raise ValueError('IntegrationNode: API key required to fetch integration.')
        # Note: there's currently no way in the API code to get integrations
        # owned by another user, nor is there a way to get integrations by 
        # their ID.
        response = requests.get(
            API_INTEGRATION_FETCH_ENDPOINT,
            data={
                'integration_name': self.integration_name
            },
            headers={
                'Public-Key': self._public_key,
                'Private-Key': self._private_key
            }
        )
        if response.status_code != 200:
            raise Exception(f"Error fetching integration: {response.text}")
        integration_json = response.json()
        # don't need to store integration parameters in node's JSON
        if 'params' in integration_json:
            del integration_json['params']

        return {
            'integration': integration_json,
            'integrationType': self.integration_type,
            'function': self.function_params,
            **self.integration_specific_params
        }
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'IntegrationNode':
        return IntegrationNode(
            integration_type=json_data['data']['integration']['type'],
            integration_name=json_data['data']['integration']['name'],
            function=json_data['data']['function']['name'],
            # For IntegrationNodes, we must pass in the input names to the 
            # constructor, as they will be validated against the integration 
            # and function upon initialization.
            inputs={ 
                i['name']: [None] 
                for i in json_data['data']['function'].get('inputs', [])
            },
            skip_typecheck=True
        )

# The classes below are particular "types" of IntegrationNodes, which users 
# may prefer for specificity. They're all created via calls to IntegrationNode.
# TODO: override the _from_json_rep methods for this, PromptLLMNodes, and 
# DataLoaderNodes
class PineconeIntegrationNode(IntegrationNode):
    def __init__(self, integration_name:str, function:str, 
            inputs:dict[str, list[NodeOutput]], 
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Pinecone',
            integration_name=integration_name,
            function=function,
            inputs=inputs,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class SalesforceIntegrationNode(IntegrationNode):
    def __init__(self, integration_name:str, function:str, 
            inputs:dict[str, list[NodeOutput]], 
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Salesforce',
            integration_name=integration_name,
            function=function,
            inputs=inputs,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class GoogleDriveIntegrationNode(IntegrationNode):
    def __init__(self, integration_name:str, function:str, 
            inputs:dict[str, list[NodeOutput]], 
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Google Drive',
            integration_name=integration_name,
            function=function,
            inputs=inputs,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class GmailIntegrationNode(IntegrationNode):
    def __init__(self, integration_name:str, function:str, 
            inputs:dict[str, list[NodeOutput]], 
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Gmail',
            integration_name=integration_name,
            function=function,
            inputs=inputs,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

# Not currently accessible to users in the no-code builder
class MicrosoftIntegrationNode(IntegrationNode):
    def __init__(self, integration_name:str, function:str, 
            inputs:dict[str, list[NodeOutput]], 
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Microsoft',
            integration_name=integration_name,
            function=function,
            inputs=inputs,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

# Not currently accessible to users in the no-code builder
class NotionIntegrationNode(IntegrationNode):
    def __init__(self, integration_name:str, function:str,
            inputs:dict[str, list[NodeOutput]],
            database_id:str=None,
            database_fields:list[str]=None,
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Notion',
            integration_name=integration_name,
            function=function,
            inputs=inputs,
            public_key=public_key,
            private_key=private_key,
            database_id=database_id,
            database_fields=database_fields,
            **kwargs
        )

# Not currently accessible to users in the no-code builder
class AirtableIntegrationNode(IntegrationNode):
    def __init__(self, integration_name:str, function:str, 
            inputs:dict[str, list[NodeOutput]],
            airtable_tables:list[dict]=None,
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Airtable',
            integration_name=integration_name,
            function=function,
            inputs=inputs,
            public_key=public_key,
            private_key=private_key,
            airtable_tables=airtable_tables,
            **kwargs
        )

class HubSpotIntegrationNode(IntegrationNode):
    def __init__(self, integration_name:str, function:str, 
            inputs:dict[str, list[NodeOutput]], 
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='HubSpot',
            integration_name=integration_name,
            function=function,
            inputs=inputs,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class SugarCRMIntegrationNode(IntegrationNode):
    def __init__(self, integration_name:str, function:str, 
            inputs:dict[str, list[NodeOutput]], 
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='SugarCRM',
            integration_name=integration_name,
            function=function,
            inputs=inputs,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

# Not currently accessible to users in the no-code builder
class LinearIntegrationNode(IntegrationNode):
    def __init__(self, integration_name:str, function:str, 
            inputs:dict[str, list[NodeOutput]], 
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Linear',
            integration_name=integration_name,
            function=function,
            inputs=inputs,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

# Not currently accessible to users in the no-code builder
class SlackIntegrationNode(IntegrationNode):
    def __init__(self, integration_name:str, function:str, 
            inputs:dict[str, list[NodeOutput]], 
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Slack',
            integration_name=integration_name,
            function=function,
            inputs=inputs,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

# Not currently accessible to users in the no-code builder
class DiscordIntegrationNode(IntegrationNode):
    def __init__(self, integration_name:str, function:str, 
            inputs:dict[str, list[NodeOutput]], 
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Discord',
            integration_name=integration_name,
            function=function,
            inputs=inputs,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

# Python functions for transforming data.
### USES USER-CREATED OBJECT - see comments in VectorStoreNode
class TransformationNode(NodeTemplate):
    def __init__(self, transformation_name:str, inputs=dict[str, NodeOutput],
            public_key:str=None, private_key:str=None, **kwargs):
        super().__init__()
        self.node_type = 'transformation'
        self.category = self.task_name = 'transformation'
        self._public_key = public_key or vectorshift.public_key
        self._private_key = private_key or vectorshift.private_key
        self.transformation_name = transformation_name
        # We make an API call to get the transformation JSON here to get the
        # desired outputs - see PipelineNode
        if self._public_key is None or self._private_key is None:
            raise ValueError('TransformationNode: API key required to fetch transformation.')
        # Note: there's currently no way in the API code to get files owned 
        # by another user, nor is there a way to get files by their ID.
        response = requests.get(
            API_TRANSFORMATION_FETCH_ENDPOINT,
            data={
                'transformation_name': self.transformation_name
            },
            headers={
                'Public-Key': self._public_key,
                'Private-Key': self._private_key
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error fetching transformation: {response.text}')
        self.transformation_json = response.json()
        input_names = self.transformation_json['inputs']
        # The list of inputs provided should have keys matching the input names
        # defined by the transformation
        if sorted(list(inputs.keys())) != sorted(input_names):
            raise ValueError(f'TransformationNode: inputs do not match expected input names: expected f{input_names}')

        self._inputs = {
            input_name: [inputs[input_name]] for input_name in input_names
        } 

        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_input(self, input_name:str, input:NodeOutput):
        if input_name not in self._inputs.keys():
            raise ValueError(f'Invalid input name {input_name}.')
        old_input = self._inputs[input_name]
        self._inputs[input_name] = [input] 
        try:
            validate_node_inputs(self)
        except ValueError as err:
            self._inputs[input_name] = old_input
            raise err

    def set_inputs(self, inputs:dict[str, NodeOutput]):
        if sorted(inputs.keys()) != sorted(self._inputs.keys()):
            raise ValueError(f'Invalid input names provided.')
        old_inputs = self._inputs.copy()
        self._inputs = {
            k: [v] for k, v in inputs.items()
        } 
        try:
            validate_node_inputs(self)
        except ValueError as err:
            self._inputs = old_inputs
            raise err
    
    def set_api_key(self, public_key:str, private_key:str):
        self._public_key = public_key
        self._private_key = private_key

    def init_args_strs(self):
        return [
            f"transformation_name='{self.transformation_name}'",
            f'inputs={format_node_output_dict(self._inputs)}',
            f"public_key={nullable_str(self._public_key)}",
            f"private_key={nullable_str(self._private_key)}"
        ]
    
    def outputs(self):
        os = {}
        for output_field in self.transformation_json['outputs'].keys():
            os[output_field] = NodeOutput(
                source=self,
                output_field=output_field,
                # TODO: start storing types with transformations
                # Using AnyType() for now
                output_data_type=AnyType()
            )
        return os
    
    def _to_json_rep(self):
        transformation_field_json = {
            'id': self.transformation_json['id'],
            'name': self.transformation_json['name'],
            'description': self.transformation_json['description'],
            'inputs': self.transformation_json['inputs'],
            'outputs': self.transformation_json['outputs'],
            # In the app repo this calls a helper function to format pipeline
            # names. For the time being this will be the same as the name as
            # the only case in which it isn't the name are if it's owned by the
            # user (which is impossible right now). TODO: may need to fix. Same
            # issue in PipelineNode.
            'displayName': self.transformation_json['name'],
        }

        return {
            'transformation': transformation_field_json,
        }
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'TransformationNode':
        return TransformationNode(
            transformation_name=json_data['data']['transformation']['name'],
            inputs={
                input_name: [None] 
                for input_name in json_data['data']['transformation'].get('inputs', [])
            },
            skip_typecheck=True
        )

# File save nodes have no outputs.
class FileSaveNode(NodeTemplate):
    def __init__(self, name_input:NodeOutput, files_input:list[NodeOutput], 
            **kwargs):
        super().__init__()
        self.node_type = 'fileSave'
        self.category = 'task'
        self.task_name = 'save_file'
        self._inputs = {
            'name': [name_input],
            # files aggregates one or more node outputs
            'files': files_input
        }
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def init_args_strs(self):
        name_input = self._inputs['name'][0]
        files_input_strs = [
            f"(node id {i.source._id}).outputs()['{i.output_field}']"
            for i in self._inputs['files']
        ]
        return [
            format_node_output_with_name('name_input', name_input),
            f'files_input={files_input_strs}'
        ]
    
    def set_name_input(self, name_input:NodeOutput):
        check_type('FileSaveNode input name', name_input.output_data_type, TEXT_TYPE)
        self._inputs['name'] = [name_input]
    
    def set_files_input(self, files_input:list[NodeOutput]):
        for o in files_input:
             check_type('FileSaveNode input files', o.output_data_type, UnionType(FILE_TYPE, ListType(FILE_TYPE)))
        self._inputs['files'] = files_input
    
    def outputs(self): return None
    
    def _to_json_rep(self):
        return {}
        
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'FileSaveNode':
        _ = json_data 
        return FileSaveNode(
            name_input=None,
            files_input=[],
            skip_typecheck=True
        )

# A sticky note with no functionality. (SDK users shouldn't really have
# a use for this given that Python comments exist. Included for compatibility.)
# Note: in the no-code editor, this is named a 'Note'.
class StickyNoteNode(NodeTemplate):
    def __init__(self, text:str, **kwargs):
        super().__init__()
        self.node_type = 'stickyNote'
        self.category = 'comment'
        self.task_name = 'none'
        self.text = text 
        # no typechecking needed

    def set_text(self, text:str): self.text = text 

    def init_args_strs(self):
        return [f"text='{self.text}'"]
    
    def outputs(self): return None 

    def _to_json_rep(self):
        return {'text': self.text}
    
    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'StickyNoteNode':
        return StickyNoteNode(
            text=json_data['data']['text'],
            skip_typecheck=True
        )

###############################################################################
# LLMS                                                                        #
###############################################################################

class OpenAILLMNode(NodeTemplate):
    def __init__(self, model:str, 
            system_input:str|NodeOutput, prompt_input:str|NodeOutput,
            text_inputs:dict[str, NodeOutput]={},
            max_tokens:int=1024, temperature:float=1.0, top_p:float=1.0,
            stream_response:bool = False, json_response:bool = False, 
            personal_api_key:str = None, **kwargs):
        super().__init__()
        self.node_type = 'llmOpenAI'
        self.category = 'task'
        self.task_name = 'llm_openai'
        if model not in SUPPORTED_OPENAI_LLMS.keys():
            raise ValueError(f'OpenAILLMNode: invalid model {model}.')
        self.model = model 
        self.stream_response = stream_response 
        self.json_response = json_response
        # assume if a personal API key is provided, it's being used
        self.personal_api_key = "" 
        if personal_api_key:
            self.personal_api_key = personal_api_key
        self.max_tokens, self.temp, self.top_p = max_tokens, temperature, top_p
        if self.max_tokens < 0:
            raise ValueError(f'OpenAILLMNode: invalid max_tokens value.')
        if self.max_tokens > SUPPORTED_OPENAI_LLMS[self.model]:
            raise ValueError(f'OpenAILLMNode: max_tokens {self.max_tokens} is too large for model {self.model}.')
        if self.temp < 0. or self.temp > 1.:
            raise ValueError(f'OpenAILLMNode: invalid temperature value.')
        if self.top_p <= 0.:
            raise ValueError(f'OpenAILLMNode: invalid top_p value.')
        # Store the inputs that are NodeOutputs vs. those that are strings
        # in separate dicts. For those that are strings, find text variables
        # which should be provided in text_inputs. See comments in TextNode
        self._inputs = {}
        self.all_text_inputs : dict[str, list[NodeOutput]] = {
            k: [v] for k, v in text_inputs.items()
        }
        self.system_text, self.prompt_text = '', ''
        self.system_text_vars, self.prompt_text_vars = [], []
        if type(system_input) == str:
            self.system_text = system_input
            self.system_text_vars = find_text_vars(self.system_text)
        else:
            self._inputs['system'] = [system_input]
        if type(prompt_input) == str:
            self.prompt_text = prompt_input 
            self.prompt_text_vars = find_text_vars(self.prompt_text)
        else:
            self._inputs['prompt'] = [prompt_input]
        check_text_vars(
            self.system_text_vars + self.prompt_text_vars, 
            self.all_text_inputs.keys()
        )
        # the _inputs keys are 'system', 'prompt', and any text var names
        for k, v in self.all_text_inputs.items():
            if k in self.system_text_vars or k in self.prompt_text_vars:
                self._inputs[k] = v
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_system(self, system_input:str|NodeOutput):
        if type(system_input) == NodeOutput:
            check_type('OpenAILLMNode input system', system_input.output_data_type, TEXT_TYPE)
            self.system_text, self.system_text_vars = '', []
            # update _inputs to remove any potential unused text vars
            self._inputs['system'] = [system_input]
            for k in list(self._inputs.keys()):
                if k not in ['system', 'prompt'] + self.prompt_text_vars:
                    del self._inputs[k]
        else:
            self.system_text = system_input
            self.system_text_vars = find_text_vars(self.system_text)
            check_text_vars(
                self.system_text_vars, 
                self.all_text_inputs.keys()
            )
            new_inputs = {
                k: v for k, v in self.all_text_inputs if k in self.system_text_vars + self.prompt_text_vars
            }
            if 'prompt' in self._inputs.keys(): 
                new_inputs['prompt'] = self._inputs['prompt']
            self._inputs = new_inputs

    def set_prompt(self, prompt_input:str|NodeOutput):
        if type(prompt_input) == NodeOutput:
            check_type('OpenAILLMNode input prompt', prompt_input.output_data_type, TEXT_TYPE)
            self.prompt_text, self.prompt_text_vars = '', []
            # update _inputs to remove any potential unused text vars
            self._inputs['prompt'] = [prompt_input]
            for k in list(self._inputs.keys()):
                if k not in ['system', 'prompt'] + self.system_text_vars:
                    del self._inputs[k]
        else:
            self.prompt_text = prompt_input
            self.prompt_text_vars = find_text_vars(self.prompt_text)
            check_text_vars(
                self.prompt_text_vars, 
                self.all_text_inputs.keys()
            )
            new_inputs = {
                k: v for k, v in self.all_text_inputs if k in self.system_text_vars + self.prompt_text_vars
            }
            if 'system' in self._inputs.keys():
                new_inputs['system'] = self._inputs['system']
            self._inputs = new_inputs

    def set_text_input(self, text_var:str, input:NodeOutput):
        check_type(f'OpenAILLMNode text input {text_var}', input.output_data_type, TEXT_TYPE)
        self.all_text_inputs[text_var] = [input]

    def remove_text_input(self, text_var:str):
        if text_var in self.system_text_vars + self.prompt_text_vars:
            raise ValueError(f'OpenAILLMNode: text variable {text_var} is being used.')
        del self.all_text_inputs[text_var]

    def set_text_inputs(self, text_inputs:dict[str, NodeOutput]):
        check_text_vars(self.system_text_vars + self.prompt_text_vars, text_inputs.keys())
        for k, v in text_inputs.items():
            check_type(f'OpenAILLMNode text input {k}', v.output_data_type, TEXT_TYPE)
        self.all_text_inputs = {k: [v] for k, v in text_inputs}
        for k in self._inputs.keys():
            if k in self.all_text_inputs.keys():
                self._inputs[k] = self.all_text_inputs[k]

    def set_model(self, model:str):
        if model not in SUPPORTED_OPENAI_LLMS.keys():
            raise ValueError(f'OpenAILLMNode: invalid model {model}.')
        self.model = model 

    def set_max_tokens(self, max_tokens:int):
        if max_tokens < 0:
            raise ValueError(f'OpenAILLMNode: invalid max_tokens value.')
        if max_tokens > SUPPORTED_OPENAI_LLMS[self.model]:
            raise ValueError(f'OpenAILLMNode: max_tokens {self.max_tokens} is too large for model {self.model}.')
        self.max_tokens = max_tokens
    
    def set_temperature(self, temp:float):
        if temp < 0. or temp > 1.:
            raise ValueError(f'OpenAILLMNode: invalid temperature value.')
        self.temp = temp

    def set_top_p(self, top_p:float):
        if top_p <= 0.:
            raise ValueError(f'OpenAILLMNode: invalid top_p value.')
        self.top_p = top_p
    
    def init_args_strs(self):
        system_arg_str = f"system_input='{self.system_text}'"
        prompt_arg_str = f"prompt_input='{self.prompt_text}'"
        if 'system' in self._inputs: 
            system_arg_str = format_node_output_with_name('system_input', self._inputs['system'][0])
        if 'prompt' in self._inputs: 
            prompt_arg_str = format_node_output_with_name('prompt_input', self._inputs['prompt'][0])
        # only prints any variables that are actually used
        text_inputs_arg_dict = {
            k: format_node_output(v[0], indicate_id=False) \
                for k, v in self._inputs.items() \
                    if k not in ['system', 'prompt']
        }
        args_strs = [
            f"model='{self.model}'",
            system_arg_str,
            prompt_arg_str,
            f'max_tokens={self.max_tokens}',
            f'temperature={self.temp}',
            f'top_p={self.top_p}'
        ]
        if text_inputs_arg_dict != {}:
            text_inputs_arg_dict_str = text_inputs_arg_dict.__str__().replace('"', '')
            args_strs.append(f'text_inputs={text_inputs_arg_dict_str}')
        return args_strs

    def output(self) -> NodeOutput: 
        return NodeOutput(
            source=self,
            output_field='response', 
            output_data_type=TEXT_TYPE
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self):
        json_rep = {
            'model': self.model,
            'system': self.system_text,
            'prompt': self.prompt_text,
            'maxTokens': self.max_tokens,
            'temperature': str(round(self.temp, 2)),
            'topP': str(round(self.top_p, 2)),
            'stream': self.stream_response,
            'jsonResponse': self.json_response,
            'usePersonalAPIKey': self.personal_api_key != '',
            'apiKey': self.personal_api_key,
        }
        if self.system_text_vars:
            json_rep['systemInputNames'] = self.system_text_vars
        if self.prompt_text_vars:
            json_rep['promptInputNames'] = self.prompt_text_vars
        return json_rep
       
    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'OpenAILLMNode':
        text_inputs = {}
        for name in json_data['data'].get('systemInputNames', []):
            text_inputs[name] = None
        for name in json_data['data'].get('promptInputNames', []):
            text_inputs[name] = None
        return OpenAILLMNode(
            model=json_data['data']['model'],
            system_input=json_data['data']['system'],
            prompt_input=json_data['data']['prompt'],
            text_inputs=text_inputs,
            max_tokens=json_data['data']['maxTokens'],
            temperature=float(json_data['data']['temperature']),
            top_p=float(json_data['data']['topP']),
            stream_response=json_data['data']['stream'],
            json_response=json_data['data']['jsonResponse'],
            personal_api_key=json_data['data']['apiKey'] if json_data['data']['usePersonalAPIKey'] else None,
            skip_typecheck=True
        )

# Abstraction of shared methods for node classes representing LLMs which take
# in a single prompt. OpenAILLMNode does not follow this, as it supports both
# a system and a prompt input.
class PromptLLMNode(NodeTemplate):
    def __init__(self, llm_family:str, model:str, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, 
            max_tokens:int=1024, temperature:float=1.0, top_p:float=1.0,
            **kwargs):
        super().__init__()
        self.node_type = llm_details['node_type']
        self.category = 'task'
        if llm_family not in PROMPT_LLM_FAMILIES.keys():
            raise ValueError(f'PromptLLMNode: Invalid LLM type {llm_family}.')
        llm_details = PROMPT_LLM_FAMILIES[llm_family]
        self.class_name = llm_details['node_class_name']
        self.task_name = llm_details['task_name']
        # corresponds to a const SUPPORTED_*_LLMS
        self.models:dict[str, int] = llm_details['models']
        if model not in self.models.keys():
            raise ValueError(f'{self.class_name}: invalid model {model}.')
        self.model = model 
        if max_tokens < 0:
            raise ValueError(f'{self.class_name}: invalid max_tokens value {max_tokens}.')
        if max_tokens > self.models[self.model]:
            raise ValueError(f'{self.class_name}: max_tokens {max_tokens} is too large for model {self.model}.')
        if temperature < 0. or temperature > 1.:
            raise ValueError(f'{self.class_name}: invalid temperature value {temperature}.')
        if top_p <= 0.:
            raise ValueError(f'{self.class_name}: invalid top_p value {top_p}.')
        self.max_tokens, self.temp, self.top_p = max_tokens, temperature, top_p
        # these nodes support text variables
        self._inputs = {}
        self.all_text_inputs = {
            k: [v] for k, v in text_inputs.items()
        }
        self.prompt_text, self.prompt_text_vars = '', []
        if type(prompt_input) == NodeOutput or prompt_input is None:
            self._inputs['prompt'] = [prompt_input]
        else:
            self.prompt_text = prompt_input 
            self.prompt_text_vars = find_text_vars(self.prompt_text)
            check_text_vars(self.prompt_text_vars, self.all_text_inputs.keys())
            for k, v in self.all_text_inputs.items():
                if k in self.prompt_text_vars:
                    self._inputs[k] = v
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_prompt(self, prompt_input:str|NodeOutput):
        if type(prompt_input) == NodeOutput:
            check_type(f'{self.class_name} input prompt', prompt_input.output_data_type, TEXT_TYPE)
            # no text variables if the prompt is a NodeOutput
            self._inputs = {'prompt': [prompt_input]}
        else:
            self.prompt_text = prompt_input 
            self.prompt_text_vars = find_text_vars(self.prompt_text)
            check_text_vars(
                self.prompt_text_vars, 
                self.all_text_inputs.keys()
            )
            self._inputs = {
                k: v for k, v in self.all_text_inputs if k in self.prompt_text_vars
            }

    def set_text_input(self, text_var:str, input:NodeOutput):
        check_type(f'{self.class_name} text input {text_var}', input.output_data_type, TEXT_TYPE)
        self.all_text_inputs[text_var] = [input]

    def remove_text_input(self, text_var:str):
        if text_var in self.prompt_text_vars:
            raise ValueError(f'{self.class_name}: text variable {text_var} is being used.')
        del self.all_text_inputs[text_var]

    def set_text_inputs(self, text_inputs:dict[str, NodeOutput]):
        check_text_vars(self.prompt_text_vars, text_inputs.keys())
        for k, v in text_inputs.items():
            check_type(f'{self.class_name} text input {k}', v.output_data_type, TEXT_TYPE)
        self.all_text_inputs = {k: [v] for k, v in text_inputs}
        for k in self._inputs.keys():
            if k in self.all_text_inputs.keys():
                self._inputs[k] = self.all_text_inputs[k]

    def set_model(self, model:str):
        if model not in self.models.keys():
            raise ValueError(f'{self.class_name}: invalid model {model}.')
        self.model = model 

    def set_max_tokens(self, max_tokens:int):
        if max_tokens < 0:
            raise ValueError(f'{self.class_name}: invalid max_tokens value {max_tokens}.')
        if max_tokens > SUPPORTED_ANTHROPIC_LLMS[self.model]:
            raise ValueError(f'{self.class_name}: max_tokens {self.max_tokens} is too large for model {self.model}.')
        self.max_tokens = max_tokens
    
    def set_temperature(self, temperature:float):
        if temperature < 0. or temperature > 1.:
            raise ValueError(f'{self.class_name}: invalid temperature value {temperature}.')
        self.temp = temperature

    def set_top_p(self, top_p:float):
        if top_p <= 0.:
            raise ValueError(f'{self.class_name}: invalid top_p value {top_p}.')
        self.top_p = top_p

    def init_args_strs(self):
        prompt_arg_str = f"prompt_input='{self.prompt_text}'"
        if 'prompt' in self._inputs and type(self._inputs['prompt'][0]) == NodeOutput:
            prompt_arg_str = format_node_output_with_name('prompt_input', self._inputs['prompt'][0])
        # only prints any variables that are actually used
        text_inputs_arg_dict = {
            k: format_node_output(v[0], indicate_id=False) \
                for k, v in self._inputs.items() \
                    if k not in ['system', 'prompt']
        }
        args_strs = [
            f"model='{self.model}'",
            prompt_arg_str, 
            f'max_tokens={self.max_tokens}',
            f'temperature={self.temp}',
            f'top_p={self.top_p}'
        ]
        if text_inputs_arg_dict != {}:
            text_inputs_arg_dict_str = text_inputs_arg_dict.__str__().replace('"', '')
            args_strs.append(f'text_inputs={text_inputs_arg_dict_str}')
        return args_strs
    
    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self, 
            output_field='response', 
            output_data_type=TEXT_TYPE
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self):
        json_rep = {
            'model': self.model,
            'prompt': self.prompt_text,
            'maxTokens': self.max_tokens,
            'temperature': str(round(self.temp, 2)),
            'topP': str(round(self.top_p, 2)),
        }
        if self.prompt_text_vars:
            json_rep['promptInputNames'] = self.prompt_text_vars
        return json_rep
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'PromptLLMNode':
        text_inputs = {}
        for name in json_data['data'].get('promptInputNames', []):
            text_inputs[name] = None
        llm_family = ''
        for family, details in PROMPT_LLM_FAMILIES.items():
            if details['task_name'] == json_data['data']['task_name']:
                llm_family = family
        return PromptLLMNode(
            llm_family=llm_family,
            model=json_data['data']['model'],
            prompt_input=json_data['data']['prompt'],
            text_inputs=text_inputs,
            max_tokens=json_data['data']['maxTokens'],
            temperature=float(json_data['data']['temperature']),
            top_p=float(json_data['data']['topP']),
            skip_typecheck=True
        )

class AnthropicLLMNode(PromptLLMNode):
    def __init__(self, model:str, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, 
            max_tokens:int=1024, temperature:float=1.0, top_p:float=1.0,
            **kwargs):
        super().__init__(
            llm_family='anthropic',
            model=model, 
            prompt_input=prompt_input,
            text_inputs=text_inputs,
            max_tokens=max_tokens, 
            temperature=temperature, 
            top_p=top_p, 
            **kwargs
        )
        
class CohereLLMNode(PromptLLMNode):
    def __init__(self, model:str, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, 
            max_tokens:int=1024, temperature:float=1.0, top_p:float=1.0,
            **kwargs):
        super().__init__(
            llm_family='cohere',
            model=model, 
            prompt_input=prompt_input,
            text_inputs=text_inputs,
            max_tokens=max_tokens, 
            temperature=temperature, 
            top_p=top_p, 
            **kwargs
        )

class AWSLLMNode(PromptLLMNode):
    def __init__(self, model:str, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, 
            max_tokens:int=1024, temperature:float=1.0, top_p:float=1.0,
            **kwargs):
        super().__init__(
            llm_family='aws',
            model=model, 
            prompt_input=prompt_input,
            text_inputs=text_inputs,
            max_tokens=max_tokens, 
            temperature=temperature, 
            top_p=top_p, 
            **kwargs
        )
    
class MetaLLMNode(PromptLLMNode):
    def __init__(self, model:str, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, 
            max_tokens:int=1024, temperature:float=1.0, top_p:float=1.0,
            **kwargs):
        super().__init__(
            llm_family='meta',
            model=model, 
            prompt_input=prompt_input,
            text_inputs=text_inputs,
            max_tokens=max_tokens, 
            temperature=temperature, 
            top_p=top_p, 
            **kwargs
        )

class OpenSourceLLMNode(PromptLLMNode):
    def __init__(self, model:str, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, 
            max_tokens:int=1024, temperature:float=1.0, top_p:float=1.0,
            **kwargs):
        super().__init__(
            llm_family='open_source',
            model=model, 
            prompt_input=prompt_input,
            text_inputs=text_inputs,
            max_tokens=max_tokens, 
            temperature=temperature, 
            top_p=top_p, 
            **kwargs
        )

class GoogleLLMNode(PromptLLMNode):
    def __init__(self, model:str, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, 
            max_tokens:int=1024, temperature:float=1.0, top_p:float=1.0,
            **kwargs):
        super().__init__(
            llm_family='google',
            model=model, 
            prompt_input=prompt_input,
            text_inputs=text_inputs,
            max_tokens=max_tokens, 
            temperature=temperature, 
            top_p=top_p, 
            **kwargs
        )

###############################################################################
# MULTIMODAL                                                                  #
###############################################################################

class ImageGenNode(NodeTemplate):
    def __init__(self, model:str, 
            image_size:int|tuple[int,int], num_images:int, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, **kwargs):
        super().__init__()
        self.node_type = 'imageGen'
        self.category = 'task'
        self.task_name = 'generate_image'
        if model not in SUPPORTED_IMAGE_GEN_MODELS.keys():
            raise ValueError(f'ImageGenNode: invalid model {model}.')
        # models like DALL-E are represented with dots in the database
        self.model = model
        if image_size not in SUPPORTED_IMAGE_GEN_MODELS[self.model][0]:
            raise ValueError(f'ImageGenNode: Invalid image size {image_size}.')
        if num_images not in SUPPORTED_IMAGE_GEN_MODELS[self.model][1]:
            raise ValueError(f'ImageGenNode: Invalid number of images {num_images}.')
        self.image_size = image_size 
        self.num_images = num_images 
        # this node also supports text vars
        self._inputs = {}
        self.all_text_inputs = {
            k: [v] for k, v in text_inputs.items()
        }
        self.prompt_text, self.prompt_str_vars = '', []
        if type(prompt_input) == NodeOutput or prompt_input is None:
            self._inputs['prompt'] = [prompt_input]
        else:
            self.prompt_text = prompt_input 
            self.prompt_text_vars = find_text_vars(self.prompt_text)
            check_text_vars(self.prompt_text_vars, self.all_text_inputs.keys())
            for k, v in self.all_text_inputs.items():
                if k in self.prompt_text_vars:
                    self._inputs[k] = v
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_prompt(self, prompt_input:str|NodeOutput):
        if type(prompt_input) == NodeOutput:
            check_type('ImageGenNode input prompt', prompt_input.output_data_type, TEXT_TYPE)
            # no text variables if the prompt is a NodeOutput
            self._inputs = {'prompt': [prompt_input]}
        else:
            self.prompt_text = prompt_input 
            self.prompt_text_vars = find_text_vars(self.prompt_text)
            check_text_vars(
                self.prompt_text_vars, 
                self.all_text_inputs.keys()
            )
            self._inputs = {
                k: v for k, v in self.all_text_inputs if k in self.prompt_text_vars
            }

    def set_text_input(self, text_var:str, input:NodeOutput):
        check_type(f'ImageGenNode text input {text_var}', input.output_data_type, TEXT_TYPE)
        self.all_text_inputs[text_var] = [input]

    def remove_text_input(self, text_var:str):
        if text_var in self.prompt_text_vars:
            raise ValueError(f'ImageGenNode: text variable {text_var} is being used.')
        del self.all_text_inputs[text_var]

    def set_text_inputs(self, text_inputs:dict[str, NodeOutput]):
        check_text_vars(self.prompt_text_vars, text_inputs.keys())
        for k, v in text_inputs.items():
            check_type(f'ImageGenNode text input {k}', v.output_data_type, TEXT_TYPE)
        self.all_text_inputs = {k: [v] for k, v in text_inputs}
        for k in self._inputs.keys():
            if k in self.all_text_inputs.keys():
                self._inputs[k] = self.all_text_inputs[k]

    def set_model_params(self, model:str, image_size:int|tuple[int,int], num_images:int):
        if model not in SUPPORTED_IMAGE_GEN_MODELS.keys():
            raise ValueError(f'AnthropicLLMNode: invalid model {model}.')
        self.model = model 
        if image_size not in SUPPORTED_IMAGE_GEN_MODELS[self.model][0]:
            raise ValueError(f'ImageGenNode: Invalid image size {image_size}.')
        if num_images not in SUPPORTED_IMAGE_GEN_MODELS[self.model][1]:
            raise ValueError(f'ImageGenNode: Invalid number of images {num_images}.')
        self.image_size = image_size 
        self.num_images = num_images 
    
    def init_args_strs(self):
        prompt_arg_str = f"prompt_input='{self.prompt_text}'"
        if 'prompt' in self._inputs and type(self._inputs['prompt'][0]) == NodeOutput:
            prompt_arg_str = format_node_output_with_name('prompt_input', self._inputs['prompt'][0])
        # only prints any variables that are actually used
        text_inputs_arg_dict = {
            k: format_node_output(v[0], indicate_id=False) \
                for k, v in self._inputs.items() \
                    if k not in ['system', 'prompt']
        }
        args_strs = [
            f"model='{self.model}'",
            f'image_size={self.image_size}',
            f'num_images={self.num_images}',
            prompt_arg_str
        ]
        if text_inputs_arg_dict != {}:
            text_inputs_arg_dict_str = text_inputs_arg_dict.__str__().replace('"', '')
            args_strs.append(f'text_inputs={text_inputs_arg_dict_str}')
        return args_strs

    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self, 
            output_field='images', 
            output_data_type=ListType(IMAGE_FILE_TYPE)
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self):
        size = f'{self.image_size}x{self.image_size}' \
            if type(self.image_size) == int \
            else f'{self.image_size[0]}x{self.image_size[1]}'
        json_rep = {
            'model': re.sub('DALL-E', 'DALL·E', self.model),
            'prompt': self.prompt_text,
            'size': size,
            'imageCount': self.num_images,
        }
        if self.prompt_text_vars:
            json_rep['promptInputNames'] = self.prompt_text_vars
        return json_rep
        
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'ImageGenNode':
        image_size_str = json_data['data']['size']
        x_coord = image_size_str.index('x')
        image_size = (
            int(image_size_str[:x_coord]), 
            int(image_size_str[x_coord+1:])
        )
        if image_size[0] == image_size[1]:
            image_size = image_size[0]
        text_inputs = {}
        for name in json_data['data'].get('promptInputNames', []):
            text_inputs[name] = None
        return ImageGenNode(
            model=json_data['data']['model'],
            image_size=image_size,
            num_images=int(json_data['data']['imageCount']),
            prompt_input=json_data['data']['prompt'],
            text_inputs=text_inputs,
            skip_typecheck=True
        )
    
class SpeechToTextNode(NodeTemplate):
    def __init__(self, model:str, audio_input:NodeOutput, **kwargs):
        super().__init__()
        self.node_type = 'speechToText'
        self.category = 'task'
        self.task_name = 'speech_to_text'
        if model not in SUPPORTED_SPEECH_TO_TEXT_MODELS:
            raise ValueError(f'SpeechToTextNode: invalid model {model}.')
        self.model = model
        self._inputs = {'audio': [audio_input]}
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_model(self, model:str):
        if model not in SUPPORTED_SPEECH_TO_TEXT_MODELS:
            raise ValueError(f'SpeechToTextNode: invalid model {model}.')
        self.model = model

    def set_audio_input(self, audio_input:NodeOutput):
        check_type('ImageGenNode input audio', audio_input.output_data_type, AUDIO_FILE_TYPE)
        self._inputs['audio'] = [audio_input]
    
    def init_args_strs(self):
        audio_input = self._inputs['audio'][0]
        return [
            f"model='{self.model}'",
            format_node_output_with_name('audio_input', audio_input)
        ]

    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self, 
            output_field='text', 
            output_data_type=TEXT_TYPE
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self):
        return {'model': self.model}
        
    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'SpeechToTextNode':
        return SpeechToTextNode(
            model=json_data['data']['model'],
            audio_input=None,
            skip_typecheck=True
        )

###############################################################################
# DATA LOADERS                                                                #
###############################################################################

# Nodes for loading data from various sources, with (Mongo) node type 
# "dataLoader".
class DataLoaderNode(NodeTemplate):
    # inputs can either be NodeOutputs or strings, so inputs is a dictionary of
    # input names to a list of NodeOutputs or a singleton list of strings. 
    # Currently, mixing strings/NodeOutputs is not supported.
    def __init__(self, loader_type:str, 
            inputs:dict[str, list[str|NodeOutput]], 
            chunk_size:int=DEFAULT_CHUNK_SIZE, 
            chunk_overlap:int=DEFAULT_CHUNK_OVERLAP, 
            func:str='default', **kwargs):
        super().__init__()
        self.node_type = 'dataLoader'
        self.category = 'task'
        if loader_type not in DATALOADER_PARAMS.keys():
            raise ValueError(f'DataLoaderNode: invalid dataloader type {loader_type}.')
        input_names = DATALOADER_PARAMS[loader_type]['input_names']
        if sorted(list(inputs.keys())) != sorted(input_names):
            raise ValueError(f'DataLoaderNode: inputs do not match expected input names: expected {input_names}')
        self.loader_type = loader_type
        self.task_name = DATALOADER_PARAMS[loader_type]['task_name']
        if chunk_size < 1 or chunk_size > 4096:
            raise ValueError(f'DataLoaderNode: invalid chunk_size value.')
        if chunk_overlap < 0: raise ValueError('DataLoaderNode: invalid chunk_overlap value.')
        if chunk_overlap >= chunk_size:
            raise ValueError(f'DataLoaderNode: chunk_overlap must be smaller than chunk_size.')
        self.chunk_size, self.chunk_overlap, self.func = chunk_size, chunk_overlap, func
        # Store the inputs that are NodeOutputs vs. those that are strings
        # in separate dicts
        self._inputs = {}
        self._input_strs = {}
        # only the inputs that are NodeOutputs should be added to _inputs
        if inputs:
            for k, v in inputs.items():
                if len(v) == 0:
                    raise ValueError(f'DataLoaderNode: received no inputs for input name {k}.')
                if type(v[0]) == NodeOutput or v[0] is None:
                    self._inputs[k] = v
                elif type(v[0]) == str:
                    if len(v) != 1:
                        raise ValueError('DataLoaderNode: string inputs should be singleton lists.')
                    self._input_strs[k] = v[0]
                else:
                    raise ValueError(f'DataLoaderNode: input name {k} must be a NodeOutput or a string.')
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_chunk_size(self, chunk_size:int):
        if chunk_size < 1 or chunk_size > 4096:
            raise ValueError(f'DataLoaderNode: invalid chunk_size value.')
        self.chunk_size = chunk_size 

    def set_chunk_overlap(self, chunk_overlap:int):
        if chunk_overlap < 0: raise ValueError('DataLoaderNode: invalid chunk_overlap value.')
        if chunk_overlap >= self.chunk_size:
            raise ValueError(f'DataLoaderNode: chunk_overlap must be smaller than chunk_size.')
        self.chunk_overlap = chunk_overlap

    def set_func(self, func:str): self.func = func

    def set_input(self, input_name:str, input:str|list[NodeOutput]):
        if type(input) == str:
            if input_name in self._inputs.keys(): 
                del self._inputs[input_name]
            self._input_strs[input_name] = input
        else:
            old_input = self._inputs[input_name]
            self._inputs[input_name] = [input]
            try:
                validate_node_inputs(self)
            except ValueError as err:
                self._inputs['value'] = old_input
                raise err

    def set_inputs(self, inputs:dict[str, list[str|NodeOutput]]):
        if sorted(inputs.keys()) != sorted(self._inputs.keys()):
            raise ValueError(f'Invalid input names provided.')
        old_inputs = self._inputs.copy()
        self._inputs = inputs 
        try:
            validate_node_inputs(self)
        except ValueError as err:
            self._inputs = old_inputs
            raise err

    def init_args_strs(self):
        inputs_strs = {}
        for k, v in self._inputs.items():
            inputs_strs[k] = (format_node_output(v[0], indicate_id=False))
        for k, v in self._input_strs.items():
            inputs_strs[k] = [v]
        return [
            f"loader_type='{self.loader_type}'",
            f'inputs={inputs_strs}',
            f'chunk_size={self.chunk_size}',
            f'chunk_overlap={self.chunk_overlap}',
            f"func='{self.func}'"
        ]

    def output(self) -> NodeOutput: 
        # for most datalaoders the data returned is a document list
        output_data_type = ListType(DOCUMENT_TYPE)
        if self.loader_type in ['CSV Query', 'SerpAPI']:
            output_data_type = TEXT_TYPE
        return NodeOutput(
            source=self,
            output_field='output',
            output_data_type=output_data_type
        )

    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self):
        return {
            'loaderType': self.loader_type,
            'function': self.func,
            'chunkSize': self.chunk_size,
            'chunkOverlap': self.chunk_overlap,
            # add in string params if they were passed into the constructor
            **self._input_strs
        }
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'DataLoaderNode':
        inputs = {}
        # inputs that were explicitly initialized with strings take the form
        # of additional fields in the JSON, rather than edges
        for k in DATALOADER_PARAMS[json_data['data']['loaderType']]['input_names']:
            if k in json_data['data'].keys():
                inputs[k] = [json_data['data'][k]]
            else:
                inputs[k] = [None]
        return DataLoaderNode(
            loader_type=json_data['data']['loaderType'],
            inputs=inputs,
            chunk_size=json_data['data']['chunkSize'],
            chunk_overlap=json_data['data']['chunkOverlap'],
            func=json_data['data']['function'],
            skip_typecheck=True
        )

# Like with IntegrationNodes, the classes below are particular "types" of 
# data loader nodes. They're all created via calls to DataLoaderNode. 
class FileLoaderNode(DataLoaderNode):
    def __init__(self, files_input:list[NodeOutput], **kwargs):
        super().__init__(
            loader_type='File',
            inputs={'file': files_input},
            **kwargs
        )

class CSVQueryLoaderNode(DataLoaderNode):
    def __init__(self, query_input:str|NodeOutput, csv_input:NodeOutput, 
            **kwargs):
        super().__init__(
            loader_type='CSV Query',
            inputs={'query':[query_input], 'csv':[csv_input]},
            **kwargs
        )

class URLLoaderNode(DataLoaderNode):
    def __init__(self, url_input:str|NodeOutput, **kwargs):
        super().__init__(
            loader_type='URL',
            inputs={'url':[url_input]},
            **kwargs
        )
        
class WikipediaLoaderNode(DataLoaderNode):
    def __init__(self, query_input:str|NodeOutput, **kwargs):
        super().__init__(
            loader_type='Wikipedia',
            inputs={'query':[query_input]},
            **kwargs
        )

class YouTubeLoaderNode(DataLoaderNode):
    def __init__(self, url_input:str|NodeOutput, **kwargs):
        super().__init__(
            loader_type='YouTube',
            inputs={'url':[url_input]},
            **kwargs
        )
    
class ArXivLoaderNode(DataLoaderNode):
    def __init__(self, query_input:str|NodeOutput, **kwargs):
        super().__init__(
            loader_type='Arxiv',
            inputs={'query':[query_input]},
            **kwargs
        )

class SerpAPILoaderNode(DataLoaderNode):
    def __init__(self, api_key_input:str|NodeOutput, query_input:NodeOutput, **kwargs):
        super().__init__(
            loader_type='SerpAPI',
            inputs={'apiKey':[api_key_input], 'query':[query_input]},
            **kwargs
        )

class GitLoaderNode(DataLoaderNode):
    def __init__(self, repo_input:str|NodeOutput, **kwargs):
        super().__init__(
            loader_type='Git',
            inputs={'repo':[repo_input]},
            **kwargs
        )

# DEPRECATED
class NotionLoaderNode(DataLoaderNode):
    def __init__(self, token_input, database_input, **kwargs):
        super().__init__(
            loader_type='Notion',
            inputs={'token':[token_input], 'database':[database_input]},
            **kwargs
        )

# DEPRECATED
class ConfluenceLoaderNode(DataLoaderNode):
    def __init__(self, username_input, api_key_input, url_input:NodeOutput, **kwargs):
        super().__init__(
            loader_type='Confluence',
            inputs={
                'username':[username_input],
                'apiKey':[api_key_input],
                'url':[url_input]
            },
            **kwargs
        )

###############################################################################
# VECTORDB                                                                    #
###############################################################################

# The implementation of this is akin to that of dataloader nodes.
# DEPRECATED. 
# A VectorQueryNode combines a VectorDBLoaderNode and VectorDBReaderNode.
class VectorDBLoaderNode(NodeTemplate):
    def __init__(self, documents_input:list[NodeOutput], 
            chunk_size:int=DEFAULT_CHUNK_SIZE, 
            chunk_overlap:int=DEFAULT_CHUNK_OVERLAP, 
            func:str='default', **kwargs):
        super().__init__()
        self.node_type = 'vectorDBLoader'
        self.category = 'task'
        self.task_name = 'load_vector_db'
        if chunk_size < 1 or chunk_size > 4096:
            raise ValueError(f'VectorDBLoaderNode: invalid chunk_size value.')
        if chunk_overlap < 0: raise ValueError('FileNode: invalid chunk_overlap value.')
        if chunk_overlap >= chunk_size:
            raise ValueError(f'VectorDBLoaderNode: chunk_overlap must be smaller than chunk_size.')
        self.chunk_size, self.chunk_overlap, self.func = chunk_size, chunk_overlap, func
        self._inputs = {'documents': documents_input}
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)
    
    def set_chunk_size(self, chunk_size:int):
        if chunk_size < 1 or chunk_size > 4096:
            raise ValueError(f'VectorDBLoaderNode: invalid chunk_size value.')
        self.chunk_size = chunk_size 

    def set_chunk_overlap(self, chunk_overlap:int):
        if chunk_overlap < 0: raise ValueError('DataLoaderNode: invalid chunk_overlap value.')
        if chunk_overlap >= self.chunk_size:
            raise ValueError(f'VectorDBLoaderNode: chunk_overlap must be smaller than chunk_size.')
        self.chunk_overlap = chunk_overlap

    def set_func(self, func:str): self.func = func

    def init_args_strs(self):
        documents_input_strs = [
            f"(node id {i.source._id}).outputs()['{i.output_field}']"
            for i in self._inputs['documents']
        ]
        return [f'documents_input={documents_input_strs}']

    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self, 
            output_field='database', 
            output_data_type=VECTOR_DB_TYPE
        )

    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self):
        return {'function': self.func}
        
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'VectorDBLoaderNode':
        return VectorDBLoaderNode(
            input=None,
            chunk_size=json_data['data']['chunkSize'],
            chunk_overlap=json_data['data']['chunkOverlap'],
            func=json_data['data']['function'],
            skip_typecheck=True
        )

# DEPRECATED.
class VectorDBReaderNode(NodeTemplate):
    def __init__(self, query_input:NodeOutput, database_input:NodeOutput, 
            func:str='default', max_docs_per_query:int=2,
            **kwargs):
        super().__init__()
        self.node_type = 'vectorDBReader'
        self.category = 'task'
        self.task_name = 'query_vector_db'
        self.func = func
        self.max_docs_per_query = max_docs_per_query
        if self.max_docs_per_query < 1:
            raise ValueError('VectorDBReaderNode: Invalid max_docs_per_query value.')
        self._inputs = {'query': [query_input], 'database': [database_input]}
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)
    
    def init_args_strs(self):
        query_input = self._inputs['query'][0]
        database_input = self._inputs['database'][0]
        return [
            format_node_output_with_name('query_input', query_input),
            format_node_output_with_name('database_input', database_input)
        ]

    def output(self) -> NodeOutput:
        # assume the reader returns the query result post-processed back into text
        return NodeOutput(
            source=self, 
            output_field='results', 
            output_data_type=ListType(DOCUMENT_TYPE)
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self):
        return {
            'function': self.func,
            'maxDocsPerQuery': self.max_docs_per_query
        }
        
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'VectorDBReaderNode':
        return VectorDBReaderNode(
            query_input=None,
            database_input=None,
            func=json_data['data']['function'],
            max_docs_per_query=json_data['data']['maxDocsPerQuery'],
            skip_typecheck=True
        )

# Insert documents into a fresh blank vectorstore and query it. 
class VectorQueryNode(NodeTemplate):
    def __init__(self, query_input:list[NodeOutput], 
            documents_input:list[NodeOutput], 
            max_docs_per_query:int=2, func:str='default', 
            enable_filter:bool=False, filter_input:str|NodeOutput=None, 
            rerank_documents:bool=False, **kwargs):
        super().__init__()
        self.node_type = 'vectorQuery'
        self.category = 'task'
        self.task_name = 'load_and_query_vector_db'
        if max_docs_per_query < 1: 
            raise ValueError('VectorQueryNode: invalid max_docs_per_query value.')
        self.max_docs_per_query, self.func = max_docs_per_query, func
        self.enable_filter, self.rerank_documents = enable_filter, rerank_documents
        self._inputs = {'query': query_input, 'documents': documents_input}
        self.filter_text = None
        if type(filter_input) == str:
            self.filter_text = filter_input
        elif filter_input is not None:
            self._inputs['filter'] = [filter_input]
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_enable_filter(self, enable_filter:bool): 
        self.enable_filter = enable_filter

    def set_rerank_documents(self, rerank_documents:bool):
        self.rerank_documents = rerank_documents

    def set_max_docs_per_query(self, max_docs_per_query:int):
        if max_docs_per_query < 1: 
            raise ValueError('VectorQueryNode: invalid max_docs_per_query value.')
        self.max_docs_per_query = max_docs_per_query
    
    def set_query_input(self, query_input:list[NodeOutput]):
        if len(query_input) < 1:
            raise ValueError('VectorQueryNode: documents_input is empty.')
        for o in query_input:
            check_type('VectorQueryNode input query', o.output_data_type, TEXT_TYPE)
        self._inputs['query'] = query_input
    
    def set_documents_input(self, documents_input:list[NodeOutput]):
        if len(documents_input) < 1:
            raise ValueError('VectorQueryNode: documents_input is empty.')
        for o in documents_input:
            check_type('VectorQueryNode input documents', o.output_data_type, TEXT_TYPE)
        self._inputs['documents'] = documents_input

    def set_filter_input(self, filter_input:str|NodeOutput):
        if type(filter_input) == NodeOutput:
            check_type('VectorQueryNode input filter', filter_input.output_data_type, TEXT_TYPE)
            self._inputs['filter'] = [filter_input]
            self.filter_text = None
        else:
            self.filter_text = filter_input 
            del self._inputs['filter']

    def init_args_strs(self):
        query_input_strs = [
            f"(node id {i.source._id}).outputs()['{i.output_field}']"
            for i in self._inputs['query']
        ]
        documents_input_strs = [
            f"(node id {i.source._id}).outputs()['{i.output_field}']"
            for i in self._inputs['documents']
        ]
        filter_arg_str = f'filter_input={nullable_str(self.filter_text)}'
        if 'filter' in self._inputs:
            filter_arg_str = format_node_output_with_name('filter_input', self._inputs['filter'][0])
        return [
            f'query_input={query_input_strs}',
            f'documents_input={documents_input_strs}'
            f'max_docs_per_query={self.max_docs_per_query}',
            f'func={self.func}',
            f'enable_filter={self.enable_filter}',
            filter_arg_str,
            f'rerank_documents={self.rerank_documents}'
        ]

    def output(self) -> NodeOutput:
        # assume the reader returns the query result post-processed back into text
        return NodeOutput(
            source=self, 
            output_field='result', 
            output_data_type=ListType(DOCUMENT_TYPE)
        )

    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self):
        return {
            'function': self.func,
            'maxDocsPerQuery': self.max_docs_per_query,
            'numQueries': len(self._inputs['query']),
            'enableFilter': self.enable_filter, 
            'filter': self.filter_text,
            'rerankDocuments': self.rerank_documents
        }
        
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'VectorQueryNode':
        return VectorQueryNode(
            query_input=None,
            documents_input=None,
            func=json_data['data']['function'],
            max_docs_per_query=json_data['data']['maxDocsPerQuery'],
            enable_filter=json_data['data']['enableFilter'],
            filter_input=json_data['data']['filter'],
            rerank_documents=json_data['data']['rerankDocuments'],
            skip_typecheck=True
        )
        
# With a couple of other nodes, this node references an existing object that
# lives in the VS platform, what we generally refer to as a "user-created 
# object" here. Thus, to access it, we need to make an API call to the server
# code in order to get the JSON and store the relevant parameters in the node.
# Note: in the no-code editor, this is named a 'Vector Store Reader'.
class VectorStoreNode(NodeTemplate):
    def __init__(self, query_input:NodeOutput, 
                 vectorstore_id=None, vectorstore_name=None, 
                 username=None, org_name=None, max_docs_per_query=2, 
                 enable_filter:bool=False, filter_input:str|NodeOutput=None, 
                 rerank_documents:bool=False, alpha:float=0.5,
                 public_key:str=None, private_key:str=None,
                 **kwargs):
        super().__init__()
        self.node_type = 'vectorStore'
        self.category = 'task'
        self.task_name = 'query_vectorstore'
        if vectorstore_id is None and vectorstore_name is None:
            raise ValueError('VectorStoreNode: either the vectorstore ID or name should be specified.')
        self.vectorstore_id = vectorstore_id
        self.vectorstore_name = vectorstore_name
        self.username = username 
        self.org_name = org_name
        self.max_docs_per_query = max_docs_per_query
        if self.max_docs_per_query < 1:
            raise ValueError('VectorStoreNode: Invalid max_docs_per_query value.')
        self.enable_filter, self.rerank_documents = enable_filter, rerank_documents
        # note: alpha only means something to hybrid vectorstores
        if alpha < 0. or alpha > 1.:
            raise ValueError(f'VectorStoreNode: Invalid value of alpha {alpha}.')
        self.alpha = alpha
        self._inputs = {'query': [query_input]}
        self.filter_text = None
        if type(filter_input) == str:
            self.filter_text = filter_input
        elif filter_input is not None:
            self._inputs['filter'] = [filter_input]
        # we'll need to use the API key when fetching the user-defined 
        # vectorstore
        self._public_key = public_key or vectorshift.public_key
        self._private_key = private_key or vectorshift.private_key
        # we don't store vectorstore-specific params like chunk params, since 
        # that is a property of the vectorstore and not the node
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)
    
    @staticmethod
    def from_vectorstore_obj(vectorstore_obj, 
                             query_input:NodeOutput, 
                             public_key:str=None, private_key:str=None):
        if not vectorstore_obj.id:
            print('VectorStoreNode: VectorStore object does not contain a required ID, which likely means that the VectorStore has not yet been saved. Attempting to save the pipeline...')
            vectorstore_obj.save(public_key, private_key)
            print('VectorStoreNode: VectorStore object successfully saved.')
        # This is inefficient right now, since we save (write to Mongo) and 
        # then immediately query the object (read from Mongo) in the 
        # constructor.
        return VectorStoreNode(
            query_input=query_input, 
            vectorstore_id=vectorstore_obj.id, 
            vectorstore_name=vectorstore_obj.name, 
            public_key=public_key, 
            private_key=private_key
        )

    def set_enable_filter(self, enable_filter:bool): 
        self.enable_filter = enable_filter

    def set_rerank_documents(self, rerank_documents:bool):
        self.rerank_documents = rerank_documents

    def set_max_docs_per_query(self, max_docs_per_query:int):
        if max_docs_per_query < 1: 
            raise ValueError('VectorStoreNode: invalid max_docs_per_query value.')
        self.max_docs_per_query = max_docs_per_query

    def set_query_input(self, query_input:NodeOutput):
        check_type('VectorStoreNode input query', query_input.output_data_type, TEXT_TYPE)
        self._inputs['query'] = [query_input]

    def set_filter_input(self, filter_input:str|NodeOutput):
        if type(filter_input) == NodeOutput:
            check_type('VectorStoreNode input filter', filter_input.output_data_type, TEXT_TYPE)
            self._inputs['filter'] = [filter_input]
            self.filter_text = None
        else:
            self.filter_text = filter_input 
            del self._inputs['filter']

    def set_alpha(self, alpha:float):
        if alpha < 0. or alpha > 1.:
            raise ValueError(f'VectorStoreNode: Invalid value of alpha {alpha}.')
        self.alpha = alpha
    
    # If this node was loaded from JSON and changed to reference another
    # vectorstore object, we need to use the API key to query the new object.
    # This setter provides an explicit way to make sure the API key is in the 
    # node (if the key weren't initialized globally).
    def set_api_key(self, public_key:str, private_key:str) -> None:
        self._public_key = public_key
        self._private_key = private_key

    def init_args_strs(self):
        query_input = self._inputs['query'][0]
        filter_arg_str = f'filter_input={nullable_str(self.filter_text)}'
        if 'filter' in self._inputs:
            filter_arg_str = format_node_output_with_name('filter_input', self._inputs['filter'][0])
        return [
            format_node_output_with_name('query_input', query_input),
            f"vectorstore_id={nullable_str(self.vectorstore_id)}",
            f"vectorstore_name={nullable_str(self.vectorstore_name)}",
            f"username={nullable_str(self.username)}",
            f"org_name={nullable_str(self.org_name)}",
            f'max_docs_per_query={self.max_docs_per_query}',
            f'enable_filter={self.enable_filter}',
            filter_arg_str,
            f'rerank_documents={self.rerank_documents}',
            f'alpha={self.alpha}',
            f"public_key={nullable_str(self._public_key)}",
            f"private_key={nullable_str(self._private_key)}",
        ]

    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self, 
            output_field='results', 
            output_data_type=ListType(DOCUMENT_TYPE)
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self):
        if self._public_key is None or self._private_key is None:
            raise ValueError('VectorStoreNode: API key required to fetch vectorstore.')
        # There's currently no notion of "sharing" vectorstores (so username
        # and org_name aren't required right now), but there probably will be 
        # one in the future.
        response = requests.get(
            API_VECTORSTORE_FETCH_ENDPOINT,
            data={
                'vectorstore_id': self.vectorstore_id,
                'vectorstore_name': self.vectorstore_name,
                'username': self.username,
                'org_name': self.org_name
            },
            headers={
                'Public-Key': self._public_key,
                'Private-Key': self._private_key
            }
        )
        if response.status_code != 200:
            raise Exception(f"Error fetching vectorstore: {response.text}")
        vectorstore_json = response.json()
        return {
            'maxDocsPerQuery': self.max_docs_per_query,
            # we just copy everything over, including the vectors (if any)
            'vectorStore': vectorstore_json,
            'enableFilter': self.enable_filter, 
            'filter': self.filter_text, 
            'rerankDocuments': self.rerank_documents,
            'alpha': self.alpha
        }

    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'VectorStoreNode':
        # there isn't a way to recover the API key from the JSON rep; it can
        # be set with set_api_key; also as mentioned above, (author) username
        # and org name data isn't currently saved in Mongo
        return VectorStoreNode(
            query_input=None,
            vectorstore_id=json_data['data']['vectorStore']['id'],
            vectorstore_name=json_data['data']['vectorStore']['name'], 
            max_docs_per_query=json_data['data']['maxDocsPerQuery'],
            enable_filter=json_data['data']['enableFilter'],
            filter_input=json_data['data']['filter'],
            rerank_documents=json_data['data']['rerankDocuments'],
            alpha=json_data['data'].get('alpha', None),
            skip_typecheck=True
        )

###############################################################################
# LOGIC                                                                       #
###############################################################################

# NB: To establish that these nodes specifically represent logic/control flow,
# these class names are prefixed with "Logic".
class LogicConditionNode(NodeTemplate):
    # inputs should comprise all in-edges, which are the names of all conditions 
    # and values along with the NodeOutputs they correspond to.
    # conditions is a list of (cond, val), where if cond is True the node 
    # returns val (where val is an input name).
    # default is what the node returns in the (final) else case.
    def __init__(self, inputs:dict[str, NodeOutput], 
            conditions:list[tuple[str, str]], else_value:str,
            **kwargs):
        super().__init__()
        self.node_type = 'condition'
        # task_name is not used
        self.category = self.task_name = 'condition' 
        input_names = list(inputs.keys())
        if len(set(input_names)) != len(input_names):
            raise ValueError('LogicConditionNode: duplicate input names.')
        for cond in conditions:
            if cond[1] not in input_names:
                raise ValueError(f'LogicConditionNode: Returned value {cond[1]} of condition {cond[0]} was not specified in inputs.')
        if else_value not in input_names:
            raise ValueError(f'LogicConditionNode: Returned value {else_value} of else condition was not specified in inputs.')
        self.input_names = input_names
        self.conditions = conditions
        # NB: self.predicates maps to the JSON "conditions" field. The result
        # of the corresponding predicate in the input argument conditions is
        # the same-indexed element in self.output_names.
        self.predicates = [cond[0] for cond in conditions]
        self.output_names = [cond[1] for cond in conditions] + [else_value]
        # each separate input is an in-edge to the node, with the input name
        # being the user-provided name
        self._inputs = {k: [v] for k, v in inputs.items()}
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_input(self, input_name:str, input:NodeOutput):
        if input_name not in self._inputs.keys():
            raise ValueError(f'LogicConditionNode: invalid input name {input_name}.')
        old_input = self._inputs[input_name]
        self._inputs[input_name] = [input]
        try:
            validate_node_inputs(self)
        except ValueError as err:
            self._inputs[input_name] = [old_input]
            raise err
    
    # Pragmatically speaking it might be easier to just create a new node
    # rather than fiddling around with these methods
    def set_conditions(self, conditions:list[tuple[str, str]]):
        old_conditions = self.conditions
        self.conditions = conditions
        self.predicates = [cond[0] for cond in conditions]
        self.output_names = [cond[1] for cond in conditions] \
            + self.output_names[-1]
        try:
            validate_node_inputs(self)
        except ValueError as err:
            self.conditions = old_conditions 
            self.predicates = [cond[0] for cond in self.conditions]
            self.output_names = [cond[1] for cond in self.conditions] \
                + self.output_names[-1]
            raise err

    def set_else_value(self, else_value:str):
        if else_value not in self.input_names:
            raise ValueError(f'LogicConditionNode: Returned value {else_value} of else condition is not specified in inputs.')
        self.output_names[-1] = else_value
    
    def init_args_strs(self):
        input_strs = [
            f"({k}, (node id {v[0].source._id}).outputs()['{v[0].output_field}'])" 
            for k, v in self._inputs.items()
        ]
        return [
            f'inputs={input_strs}'.replace('"', ''),
            f'conditions={self.conditions}',
            f"else_value='{self.output_names[-1]}'"
        ]

    # Unlike most other nodes, this node has several outputs, corresponding to
    # each of the specified conditions (and the else case).
    def outputs(self):
        # the outputs are labelled "output-0", "output-1", etc. followed by
        # "output-else"
        os = {}
        # We can do better than the API code since we still have access to the
        # NodeOutputs in each conditional output (and thus the type)
        for ind in range(len(self.predicates)):
            output_source_name = self.output_names[ind]
            output_data_type = self._inputs[output_source_name][0].output_data_type
            o = NodeOutput(
                source=self, 
                output_field=f'output-{ind}', 
                output_data_type=output_data_type)
            os[o.output_field] = o
        else_output_source_name = self.output_names[-1]
        else_o = NodeOutput(
            source=self, 
            output_field='output-else', 
            output_data_type=self._inputs[else_output_source_name][0].output_data_type
        )
        os[else_o.output_field] = else_o
        return os
    
    # If a user currently wants to index into a specific output, they need to 
    # call the outputs() method and then index into it by name (e.g. 
    # "output-2", "output-else"), or use the helper functions below.
    def output_index(self, i:int) -> NodeOutput:
        if i < 0 or i >= len(self.predicates):
            raise ValueError('LogicConditionNode: index out of range.')
        os = self.outputs()
        return os[f'output-{i}']
    
    def output_else(self) -> NodeOutput: 
        os = self.outputs()
        return os['output-else']
    
    def _to_json_rep(self):
        return {
            'conditions': self.predicates,
            'inputNames': self.input_names,
            'outputs': self.output_names,
        }

    @staticmethod
    def _from_json_rep(json_data:dict) -> 'LogicConditionNode':
        predicates = json_data['data']['conditions']
        output_names = json_data['data']['outputs']
        return LogicConditionNode(
            inputs=[(name, None) for name in json_data['data'].get('inputNames', [])],
            conditions=[(predicates[i], output_names[i]) for i in range(len(predicates))],
            else_value=output_names[-1],
            skip_typecheck=True
        )
    
class LogicMergeNode(NodeTemplate):
    def __init__(self, inputs:list[NodeOutput], **kwargs):
        super().__init__()
        self.node_type = 'merge'
        # task_name is not used
        self.category = self.task_name = 'merge'
        self._inputs = {
            # The JSON name for the in-edge is "input", although the displayed
            # name is "inputs".
            'input': inputs
        }
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_inputs(self, inputs:list[NodeOutput]):
        old_inputs = self._inputs['input']
        self._inputs['input'] = inputs 
        try:
            validate_node_inputs(self)
        except ValueError as err:
            self._inputs['input'] = old_inputs 
            raise err
        
    def init_args_strs(self):
        input_strs = [
            f"(node id {i.source._id}).outputs()['{i.output_field}']" 
            for i in self._inputs['input']
        ]
        return [f'inputs={input_strs}'.replace('"', '')]

    def output(self) -> NodeOutput:
        output_data_types = set([o.output_data_type for o in self._inputs['input']])
        return NodeOutput(
            source=self, 
            output_field='output', 
            output_data_type=UnionType(*output_data_types)
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self):
        # only one function is currently supported
        return {'function': 'default'}
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'LogicMergeNode':
        _ = json_data
        return LogicMergeNode(
            inputs=[],
            skip_typecheck=True
        )

class SplitTextNode(NodeTemplate):
    # Instead of giving choices for the delimiter character, we just take in
    # a string.
    def __init__(self, delimiter:str, text_input:NodeOutput, **kwargs):
        super().__init__()
        self.node_type = 'splitText'
        self.category = 'task'
        self.task_name = 'split_text'
        if not delimiter:
            raise ValueError('SplitTextNode: delimiter cannot be an empty string.')
        self.delimiter_chars = delimiter
        self.delimiter_name = 'character(s)'
        if delimiter in TEXT_SPLIT_DELIMITER_NAMES:
            self.delimiter_name = TEXT_SPLIT_DELIMITER_NAMES[delimiter]
        self._inputs = {'text': [text_input]}
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_delimiter(self, delimiter:str):
        self.delimiter_chars = delimiter
        self.delimiter_name = 'character(s)'
        if delimiter in TEXT_SPLIT_DELIMITER_NAMES:
            self.delimiter_name = TEXT_SPLIT_DELIMITER_NAMES[delimiter]

    def set_text_input(self, text_input:NodeOutput):
        check_type('SplitTextNode input text', text_input.output_data_type, TEXT_TYPE)
        self._inputs['text'] = [text_input]
    
    def init_args_strs(self):
        text_input = self._inputs['text'][0]
        return [
            f"delimiter='{self.delimiter_chars}'",
            format_node_output_with_name('text_input', text_input)
        ]
    
    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self,
            output_field='output',
            output_data_type=ListType(TEXT_TYPE)
        )

    def outputs(self):
        o = self.output()
        return {o.output_field: o}

    def _to_json_rep(self):
        character = None if self.delimiter_name != 'character(s)' else self.delimiter_chars
        return {
            'delimiter': self.delimiter_name,
            'character': character,
        }
    
    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'SplitTextNode':
        delimiter_name = json_data['data']['delimiter']
        delimiter_chars = json_data['data']['character']
        if delimiter_name == 'space':
            delimiter_chars = ' '
        if delimiter_name == 'newline':
            delimiter_chars = '\n'
        return SplitTextNode(
            delimiter=delimiter_chars,
            skip_typecheck=True
        )

###############################################################################
# CHAT                                                                        #
###############################################################################

class ChatMemoryNode(NodeTemplate):
    # Chat memory nodes don't take input
    def __init__(self, memory_type:str, memory_window:int=None, **kwargs):
        super().__init__()
        self.node_type = 'chatMemory'
        self.category = 'memory'
        self.task_name = 'load_memory'
        if memory_type not in CHAT_MEMORY_TYPES.keys():
            raise ValueError(f'ChatMemoryNode: invalid chat memory type {memory_type}.')
        self.memory_type = memory_type
        # self.memory_window is set to the value corresponding to 
        # self.memory_type's entry in memory_window_values, which may be 
        # overridden by the constructor arg memory_window
        self.memory_window = CHAT_MEMORY_TYPES[self.memory_type]
        if memory_window is not None:
            if memory_window <= 0: 
                raise ValueError(f'ChatMemoryNode: invalid memory_window value {memory_window}.')
            if CHAT_MEMORY_TYPES[self.memory_type] == 0:
                raise ValueError('ChatMemoryNode: memory window should not be specified if the chat memory is the full text.')
        self.memory_window = memory_window
        # chat memory nodes take no inputs
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    def set_memory_type(self, memory_type:str):
        if memory_type not in CHAT_MEMORY_TYPES.keys():
            raise ValueError(f'ChatMemoryNode: invalid chat memory type {memory_type}.')
        self.memory_type = memory_type

    def set_memory_window(self, memory_window:int):
        if memory_window <= 0: 
            raise ValueError(f'ChatMemoryNode: invalid memory_window value {memory_window}.')
        if CHAT_MEMORY_TYPES[self.memory_type] == 0:
            raise ValueError("ChatMemoryNode: memory window shouldn't be specified if the chat memory is the full text.")
        self.memory_window = memory_window
    
    def init_args_strs(self):
        return [f"memory_type='{self.memory_type}'"]

    def output(self) -> NodeOutput:
        output_data_type = TEXT_TYPE if self.memory_type == 'Full - Formatted' else ListType(DICT_TYPE)
        return NodeOutput(
            source=self, 
            output_field='value', 
            output_data_type=output_data_type
        )

    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self):
        return {
            'memoryType': self.memory_type,
            'memoryWindow': self.memory_window,
            'memoryWindowValues': CHAT_MEMORY_TYPES,
        }
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'ChatMemoryNode':
        n = ChatMemoryNode(
            memory_type=json_data['data']['memoryType'],
            skip_typecheck=True
        )
        # overwrite with JSON window (not passed in constructor to handle edge case of 0)
        n.memory_window = json_data['data']['memoryWindow']
        return n

###############################################################################
# AGENTS                                                                       
###############################################################################

# User created object vs Full agent definition
# as a user create object Agent Node just referenes an existing agent by ID 
# TODO - can we move boilerplate into a base class for user created objects
# Start with user created object implementation
# Maybe angent node is analagous to a pipeline node and we have an Agent class that as analagous to a pipeline class and alllows defining the agent with various tools
class AgentNode(NodeTemplate):
    def __init__(self, agent_id:str=None, agent_name:str=None,
        inputs=dict[str, NodeOutput],
        username:str=None, org_name:str=None,
        public_key:str=None, private_key:str=None, **kwargs):      

        super().__init__()
        self.node_type = 'agent'
        # task_name is not used
        self.category = self.task_name = 'agent'
        if agent_id is None and agent_name is None:
            raise ValueError('AgentNode: either the agent ID or name should be specified.')
        
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.username = username
        self.org_name = org_name
        self._public_key = public_key or vectorshift.public_key
        self._private_key = private_key or vectorshift.private_key

        if self._public_key is None or self._private_key is None:
            raise ValueError('AgentNode: API key required to fetch agent.')
        
        response = requests.get(
            API_AGENT_FETCH_ENDPOINT,
            data={
                'agent_id': self.agent_id,
                'agent_name': self.agent_name,
                'username': self.username,
                'org_name': self.org_name
            },
            headers={
                'Public-Key': self._public_key,
                'Private-Key': self._private_key
            }
        )
        if response.status_code != 200:
            raise Exception(f"Error fetching agent: {response.text}")
        
        self.agent_json = response.json()
        self.agent_id = self.agent_json['id']
        self.agent_name = self.agent_json['name']

        input_names = [
            i['name'] for i in self.agent_json['inputs'].values()
        ]

        if sorted(list(inputs.keys())) != sorted(input_names):
            raise ValueError(f'AgentNode: pipeline node inputs do not match expected input names: expected f{input_names}')
        
        self._inputs = {
            input_name: [inputs[input_name]] for input_name in input_names
        }

        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            validate_node_inputs(self)

    @staticmethod 
    def from_agent_obj(agent_obj, 
                       inputs=dict[str, NodeOutput],
                       public_key:str=None, private_key:str=None):
        if not agent_obj.id:
            print('Agent object does not contain a required ID, which likely means that the agent has not yet been saved. Attempting to save...')
            agent_obj.save(public_key, private_key)
            print('Agent object successfully saved.')
        # This is inefficient right now, since we save (write to Mongo) and 
        # then immediately query the object (read from Mongo) in the 
        # constructor.
        return AgentNode(
            agent_id=agent_obj.id,
            agent_name=agent_obj.name,
            inputs=inputs,
            public_key=public_key, 
            private_key=private_key
        )

    def set_input(self, input_name:str, input:NodeOutput):
        if input_name not in self._inputs.keys():
            raise ValueError(f'AgentNode: Invalid input name {input_name}.')
        old_input = self._inputs[input_name]
        self._inputs[input_name] = [input] 
        try:
            validate_node_inputs(self)
        except ValueError as err:
            self._inputs[input_name] = old_input
            raise err

    def set_inputs(self, inputs:dict[str, NodeOutput]):
        if sorted(inputs.keys()) != sorted(self._inputs.keys()):
            raise ValueError(f'AgentNode: Invalid input names provided.')
        old_inputs = self._inputs.copy()
        self._inputs = {
            k: [v] for k, v in inputs.items()
        } 
        try:
            validate_node_inputs(self)
        except ValueError as err:
            self._inputs = old_inputs
            raise err

    def init_args_strs(self):
        return [
            f"agent_id={nullable_str(self.agent_id)}",
            f"agent_name={nullable_str(self.agent_name)}",
            f'inputs={format_node_output_dict(self._inputs)}',
            f"username={nullable_str(self.username)}",
            f"org_name={nullable_str(self.org_name)}",
            f"public_key={nullable_str(self._public_key)}",
            f"private_key={nullable_str(self._private_key)}"
        ]

    def set_api_key(self, public_key:str, private_key:str):
        self._public_key = public_key
        self._private_key = private_key

    def outputs(self) -> dict[str, NodeOutput]:
        os = {}
        for o in self.agent_json['outputs'].values():
            output_field = o['name']
            if o['type'] in ['Text', 'Formatted Text']:
                output_data_type = TEXT_TYPE
            elif o['type'] == 'File':
                output_data_type = FILE_TYPE
            else:
                raise ValueError(f'AgentNode: unsupported output type {o["type"]}')
            os[output_field] = NodeOutput(
                source=self, 
                output_field=output_field, 
                output_data_type=output_data_type
            )
        return os
    
    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self, 
            output_field='output',
            output_data_type=None
        )
    
    def _to_json_rep(self):
        return {'agentDefinition': self.agent_json}

    @staticmethod
    def _from_json_rep(json_data:dict) -> 'AgentNode':
        inputs = {}
        for input_name in json_data['data']['agentDefinition'].get('inputs', {}).keys():
            inputs[input_name] = None
        return AgentNode(
            agent_id=json_data['data']['agentDefinition']['id'],
            agent_name=json_data['data']['agentDefinition']['name'],
            inputs=inputs,
            skip_typecheck=True
        )
