# functionality for defining and working with Vector Store objects
import requests
import json

import vectorshift
from vectorshift.pipeline import Pipeline
from vectorshift.consts import (
    API_CHATBOT_FETCH_ENDPOINT,
    API_CHATBOT_SAVE_ENDPOINT,
    API_CHATBOT_RUN_ENDPOINT,
)

# TODO: Potentially change to inherit from Pydantic BaseModel
class Chatbot:
    # initializes a new Vector Store
    def __init__(
        self,
        name: str,
        description: str = '',
        pipeline: Pipeline = None,
        input: str = None,
        output: str = None,
        id: str = None,
    ):
        self.name = name
        self.description = description
        self.pipeline = pipeline
        self.input = input
        self.output = output
        self.id = id

    # converts Chatbot object to JSON representation
    def to_json_rep(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'pipeline': self.pipeline.to_json_rep() if self.pipeline else None,
            'input': self.input,
            'output': self.output,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_json_rep())

    @staticmethod
    def from_json_rep(json_data: dict[str, any]) -> 'Chatbot':
        return Chatbot(
            name=json_data.get('name'),
            description=json_data.get('description'),
            pipeline=json_data.get('pipeline'),
            input=json_data.get('input'),
            output=json_data.get('output'),
            id=json_data.get('id'),
        )
    
    @staticmethod
    def from_json(json_str: str) -> 'Chatbot':
        json_data = json.loads(json_str)
        return Chatbot.from_json_rep(json_data)

    def __repr__(self):
        # TODO: format this reprerentation to be more readable
        return f'Chatbot({", ".join(f"{k}={v}" for k, v in self.to_json_rep().items())})'

    # TODO: Add validation for chatbot_id and pipeline_id (in pipeline.py)
    # to prevent 5XX errors
    @staticmethod
    def fetch(
        chatbot_name: str = None,
        chatbot_id: str = None,
        username: str = None,
        org_name: str = None,
        public_key: str = None,
        private_key: str = None
    ) -> 'Chatbot':
        if chatbot_id is None and chatbot_name is None:
            raise ValueError('Must specify either chatbot_id or chatbot_name.')
        if chatbot_name is not None and username is None and org_name is not None:
            raise ValueError('Must specify username if org_name is specified.')

        response = requests.get(
            API_CHATBOT_FETCH_ENDPOINT,
            data={
                'chatbot_id': chatbot_id,
                'chatbot_name': chatbot_name,
                'username': username,
                'org_name': org_name,
            },
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error fetching chatbot object: {response.text}')
        response = response.json()
        response['pipeline'] = Pipeline.fetch(pipeline_id=response.get('pipeline', {}).get('id'))

        return Chatbot.from_json_rep(response)

    # TODO: Build functionality alongside FastAPI endpoint
    def save(
        self,
        update_existing: bool = False,
        public_key: str = None,
        private_key: str = None,
    ) -> dict:
        raise NotImplementedError('Chatbot.save() is not yet implemented.')

    def run(self, input: str, public_key:str = None, private_key:str = None) -> dict:
        if not self.id:
            raise ValueError('Chatbot must be saved before it can be run.')
        response = requests.post(
            API_CHATBOT_RUN_ENDPOINT,
            data=({
                'chatbot_id': self.id,
                'input': input,
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
