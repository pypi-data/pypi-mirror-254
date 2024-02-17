import json
import requests
from vectorshift.consts import (
    API_AUTOMATION_DELETE_ENDPOINT,
    API_AUTOMATION_DEPLOY_ENDPOINT,
    API_AUTOMATION_FETCH_ENDPOINT,
    API_AUTOMATION_GET_APPS_ENDPOINT,
    API_AUTOMATION_GET_PAYLOADS_ENDPOINT,
    API_AUTOMATION_GET_TRIGGERS_ENDPOINT,
    API_AUTOMATION_LIST_ENDPOINT,
    API_AUTOMATION_PROCESS_PAYLOADS_ENDPOINT,
    API_AUTOMATIONS_GET_EVENTS_ENDPOINT
)
import vectorshift

class Automation:
    def __init__(
        self,
        name: str,
        description: str,
        app: dict,
        event: str,
        trigger: dict,
        pipeline: dict,
        mappings: list,
        id: str = None,
    ):
        """Creating automation via the sdk is currently not supported"""
        self.id = id
        self.name = name
        self.description = description
        self.app = app
        self.event = event
        self.trigger = trigger
        self.pipeline = pipeline
        self.mappings = mappings

    def to_json_rep(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'app': self.app,
            'event': self.event,
            'trigger': self.trigger,
            'pipeline': self.pipeline,
            'mappings': self.mappings,
        }
    
    def to_json(self) -> str:
        return json.dumps(self.to_json_rep(), indent=4)
    
    @staticmethod
    def from_json_rep(json_data: dict[str, any]) -> 'Automation':
        pipeline=json_data.get('pipeline', {})
        if pipeline is not None:
            pipeline=pipeline.get('id'),
        trigger=json_data.get('trigger', {})
        if trigger is not None:
            trigger=trigger.get('name')
        return Automation(
            id=json_data.get('id'),
            name=json_data.get('name'),
            description=json_data.get('description'),
            app=json_data.get('app'),
            event=json_data.get('event'),
            trigger=trigger,
            pipeline=pipeline,
            mappings=json_data.get('mappings'),
        )

    @staticmethod
    def from_json(json_str: str) -> 'Automation':
        json_data = json.loads(json_str)
        return Automation.from_json_rep(json_data)

    def __repr__(self) -> str:
        return str(self.to_json_rep())
    
    @staticmethod
    def fetch_all(
        public_key=None,
        private_key=None,
    ) -> list['Automation']:
        response = requests.get(
            API_AUTOMATION_LIST_ENDPOINT,
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(response.text)
        
        automations = []
        for automation in response.json():
            print(automation)
            automations.append(Automation.from_json_rep(automation))
        return automations

    @staticmethod
    def fetch(
        automation_id: str = None,
        automation_name: str = None,
        public_key=None,
        private_key=None
    ) -> 'Automation':
        if automation_id is None and automation_name is None:
            raise ValueError('Must specify either automation_id or automation_name.')
        response = requests.get(
            API_AUTOMATION_FETCH_ENDPOINT,
            data={
                'automation_id': automation_id,
                'automation_name': automation_name,
            },
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()
        return Automation.from_json_rep(response)
    
    def delete(
        self,
        public_key=None,
        private_key=None
    ) -> str:
        print(self.id)
        response = requests.delete(
            f'{API_AUTOMATION_DELETE_ENDPOINT}/{self.id}',
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()
        return response
    
    @staticmethod
    def get_apps(
        public_key=None,
        private_key=None,
    ) -> list:
        response = requests.get(
            API_AUTOMATION_GET_APPS_ENDPOINT,
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()
        return response

    @staticmethod
    def get_events(
        app_id: str,
        public_key=None,
        private_key=None
    ) -> list:
        response = requests.get(
            f'{API_AUTOMATIONS_GET_EVENTS_ENDPOINT}/{app_id}',
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()
        return response
    
    @staticmethod
    def get_triggers(
        app_id: str,
        event: str,
        public_key=None,
        private_key=None
    ) -> list:
        response = requests.get(
            API_AUTOMATION_GET_TRIGGERS_ENDPOINT,
            params={
                'app_id': app_id,
                'event': event,
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

    def get_payloads(
        self,
        public_key=None,
        private_key=None
    ) -> list:
        response = requests.get(
            f'{API_AUTOMATION_GET_PAYLOADS_ENDPOINT}/{self.id}',
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()
        return response
    
    def deploy(
        self,
        active: bool,
        public_key=None,
        private_key=None
    ) -> bool:
        response = requests.post(
            f'{API_AUTOMATION_DEPLOY_ENDPOINT}/{self.id}',
            data={'active': active},
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()
        return response

    def process_payloads(
        self,
        public_key=None,
        private_key=None,
    ):
        response = requests.post(
            API_AUTOMATION_PROCESS_PAYLOADS_ENDPOINT,
            data={
                'automation_id': self.id,
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
