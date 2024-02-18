import json

import requests
import vectorshift
from vectorshift.consts import *

class Integration:
    def __init__(self, id: str, name: str, description: str, type: str):
        self.id = id
        self.name = name
        self.description = description
        self.type = type

    def to_json_rep(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'type': self.type,
        }
    
    def to_json(self) -> str:
        return json.dumps(self.to_json_rep(), indent=4)
    
    @staticmethod
    def from_json_rep(json_data: dict[str, any]) -> 'Integration':
        return Integration(
            name=json_data.get('name'),
            description=json_data.get('description'),
            type=json_data.get('type'),
            id=json_data.get('id'),
        )
    
    @staticmethod
    def from_json(json_str: str) -> 'Integration':
        json_data = json.loads(json_str)
        return Integration.from_json_rep(json_data)

    def __repr__(self) -> str:
        return str(self.to_json_rep())
    
    @staticmethod
    def fetch_all(
        public_key=None,
        private_key=None,
    ) -> list['Integration']:
        response = requests.get(
            API_INTEGRATION_FETCH_ALL_ENDPOINT,
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()

        integrations = [Integration.from_json_rep(integration) for integration in response]
        return integrations

    @staticmethod
    def fetch(
        integration_id: str = None,
        integration_name: str = None,
        public_key=None,
        private_key=None
    ) -> 'Integration':
        """
        Loads an existing integration from the VectorShift platform.
        
        Creating, deleting, and modifying integrations must be done via the VectorShift website.

        Args:
            integration_id (str): The id of the integration to load
            integration_name (str): The name of the integration to load
                at least one of these identifiers must be specified
        Returns:
            Integration: The loaded integration
        """
        if integration_name is None and integration_id is None:
            raise ValueError('Must specify either an integration_id and integration_name.')
        
        response = requests.get(
            API_INTEGRATION_FETCH_ENDPOINT,
            data={
                'integration_id': integration_id,
                'integration_name': integration_name,
            },
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()
        return Integration.from_json_rep(response)
    
    def sync_metadata(
        self,
        public_key=None,
        private_key=None,
    ) -> list:
        if self.id is None:
            raise ValueError('Missing integration id.')
        response = requests.post(
            API_INTEGRATION_SYNC_METADATA_ENDPOINT,
            data={
                'integration_id': self.id,
            },
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
    
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()
        return response
    
    def sync_integration(
        self,
        public_key=None,
        private_key=None,
    ):
        if self.id is None:
            raise ValueError('Missing integration id.')
        response = requests.post(
            API_INTEGRATION_SYNC_ENDPOINT,
            data={
                'integration_id': self.id,
            },
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )

        if response.status_code != 200:
            raise Exception(response.text)
        return

    def get_item_ids(
        self,
        public_key=None,
        private_key=None,
    ) -> list:
        """
        Returns a visualization of the file tree which can be used for mapping metadata
        """
        if self.id is None:
            raise ValueError('Missing integration id.')

        response = requests.get(
            API_INTEGRATION_GET_ITEM_IDS_ENDPOINT,
            data={
                'integration_id': self.id,
            },
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
    
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()
