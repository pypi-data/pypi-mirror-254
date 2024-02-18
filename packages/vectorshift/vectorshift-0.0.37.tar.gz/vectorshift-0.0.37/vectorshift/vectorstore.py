# functionality for defining and working with Vector Store objects
from typing import Optional
import requests
import json

import vectorshift
from vectorshift.consts import *

class VectorStore:
    # initializes a new Vector Store
    # TODO: add support for alpha here (and the corresponding node method from_vectorstore_obj)
    def __init__(
        self,
        name: str,
        description: str = '',
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
        is_hybrid: bool = False,
        id: str = None
    ):
        self.name = name
        self.description = description
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.is_hybrid = is_hybrid
        self.id = id

    # converts Vector Store object to JSON representation
    def to_json_rep(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'chunkSize': self.chunk_size,
            'chunkOverlap': self.chunk_overlap,
            'isHybrid': self.is_hybrid,
        }
    
    def to_json(self) -> str:
        return json.dumps(self.to_json_rep())
    
    @staticmethod
    def from_json_rep(json_data: dict[str, any]) -> 'VectorStore':
        return VectorStore(
            name=json_data.get('name'),
            description=json_data.get('description'),
            chunk_size=json_data.get('chunkSize', DEFAULT_CHUNK_SIZE),
            chunk_overlap=json_data.get('chunkOverlap', DEFAULT_CHUNK_OVERLAP),
            is_hybrid=json_data.get('isHybrid', False),
            id=json_data.get('id'),
        )
    
    @staticmethod
    def from_json(json_str: str) -> 'VectorStore':
        json_data = json.loads(json_str)
        return VectorStore.from_json_rep(json_data)

    def __repr__(self):
        # TODO: format this reprerentation to be more readable
        return f'VectorStore({", ".join(f"{k}={v}" for k, v in self.to_json_rep().items())})'

    # TODO: Add validation for vectorstore_id and pipeline_id (in pipeline.py)
    # to prevent 5XX errors
    @staticmethod
    def fetch(
        vectorstore_name: str = None,
        vectorstore_id: str = None,
        username: str = None,
        org_name: str = None,
        public_key: str = None,
        private_key: str = None
    ) -> 'VectorStore':
        if vectorstore_id is None and vectorstore_name is None:
            raise ValueError('Must specify either vectorstore_id or vectorstore_name.')
        if vectorstore_name is not None and username is None and org_name is not None:
            raise ValueError('Must specify username if org_name is specified.')

        response = requests.get(
            API_VECTORSTORE_FETCH_ENDPOINT,
            data={
                'vectorstore_id': vectorstore_id,
                'vectorstore_name': vectorstore_name,
                'username': username,
                'org_name': org_name,
            },
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error fetching vectorstore object: {response.text}')
        response = response.json()

        return VectorStore.from_json_rep(response)

    def save(
        self,
        update_existing: bool = False,
        public_key: str = None,
        private_key: str = None,
    ) -> dict:
        if update_existing and not self.id:
            raise ValueError("Error updating: vectorstore object does not have an existing ID. It must be saved as a new vectorstore.")
        # if update_existing is false, save as a new vectorstore
        if not update_existing:
            self.id = None

        # API_VECTORSTORE_SAVE_ENDPOINT handles saving and updating vectorstore 
        # depending on whether or not the JSON has an id (logic in api repo)
        response = requests.post(
            API_VECTORSTORE_SAVE_ENDPOINT,
            data=({'vectorstore': self.to_json()}),
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )

        if response.status_code != 200:
            raise Exception(f'Error saving vectorstore object: {response.text}')
        response = response.json()
        self.id = response.get('id')

        return response
    
    def update_metadata(
        self,
        list_of_item_ids: list[str],
        list_of_metadata: list[str],
        keep_prev: bool,
        public_key: str = None,
        private_key: str = None,
    ) -> None:
        if not self.id:
            raise ValueError("Error updating: vector store object does not have an existing ID. It must be saved first.")
        
        data = {
            'vectorstore_id': self.id,
            'list_of_item_ids': list_of_item_ids,
            'list_of_metadata': [json.dumps(metadata) for metadata in list_of_metadata],
            'keep_prev': keep_prev,            
        }

        response = requests.post(
            API_VECTORSTORE_UPDATE_METADATA_ENDPOINT,
            data=data,
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )

        if response.status_code != 200:
            raise Exception(f'Error updating document(s) metadata: {response.text}')
        return


    def update_selected_files(
        self,
        integration_id: str,
        keep_prev: bool,
        selected_items: Optional[list[str]] = None,
        select_all_items_flag: Optional[bool] = True,
        public_key: str = None,
        private_key: str = None,
    ) -> None:
        if not self.id:
            raise ValueError("Error updating: vector store object does not have an existing ID. It must be saved first.")
        
        data = {
            'vectorstore_id': self.id,
            'integration_id': integration_id,
            'selected_items': selected_items,
            'keep_prev': keep_prev,
            'select_all_items_flag': select_all_items_flag,
        }

        response = requests.post(
            API_VECTORSTORE_UPDATE_SELECTED_ITEMS_ENDPOINT,
            data=data,
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )

        if response.status_code != 200:
            raise Exception(f'Error updating items selected: {response.text}')
        return
    
    def sync(
        self,
        public_key: str = None,
        private_key: str = None,
    ) -> None:
        if not self.id:
            raise ValueError('Error loading documents: vector store object does not have an existing ID. It must be saved as a new vector store.')
        
        response = requests.post(
            API_VECTORSTORE_SYNC_ENDPOINT,
            data={
                'vectorstore_id': self.id,
            },
            headers={
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )

        if response.status_code != 200:
            raise Exception(response.text)
        
        response = response.json()
        return

    def load_documents(
        self,
        document,
        document_name: str = None,
        document_type: str = 'File',
        chunk_size: int = None,
        chunk_overlap: int = None,
        selected_items: list = None,
        select_all_items_flags: list = None,
        metadata: dict = None,
        metadata_by_item: dict = None,
        public_key: str = None,
        private_key: str = None,
    ) -> dict:
        if not self.id:
            raise ValueError('Error loading documents: vector store object does not have an existing ID. It must be saved as a new vector store.')

        chunk_size = chunk_size or self.chunk_size
        chunk_overlap = chunk_overlap or self.chunk_overlap

        data = {
            'vectorstore_id': self.id,
            'document_name': document_name,
            'document_type': document_type,
            'chunk_size': chunk_size,
            'chunk_overlap': chunk_overlap,
            'selected_items': json.dumps(selected_items),
            'select_all_items_flags': json.dumps(select_all_items_flags),
            'metadata': json.dumps(metadata),
            'metadata_by_item': json.dumps(metadata_by_item),
        }

        headers={
            'Public-Key': public_key or vectorshift.public_key,
            'Private-Key': private_key or vectorshift.private_key,
        }

        if document_type == 'File':
            if isinstance(document, str):
                with open(document, 'rb') as f:
                    files = {'document': f}
                    response = requests.post(
                        API_VECTORSTORE_LOAD_ENDPOINT,
                        data=data,
                        headers=headers,
                        files=files,
                    )
            else:
                files = {'document': document}
                response = requests.post(
                    API_VECTORSTORE_LOAD_ENDPOINT,
                    data=data,
                    headers=headers,
                    files=files,
                )
        elif document_type == 'Integration':
            data['document'] = document
            response = requests.post(
                    API_VECTORSTORE_LOAD_ENDPOINT,
                    data=data,
                    headers=headers,
                )
        else:
            data['document'] = document
            response = requests.post(
                API_VECTORSTORE_LOAD_ENDPOINT,
                data=data,
                headers=headers,
            )

        if response.status_code != 200:
            raise Exception(f'Error loading documents: {response.text}')
        response = response.json()

        return response

    def query(
        self,
        query: str,
        max_docs: int = 5,
        filter: dict = None,
        rerank: bool = False,
        public_key: str = None,
        private_key: str = None,
    ) -> dict:
        filter = filter or {}
        response = requests.post(
            API_VECTORSTORE_QUERY_ENDPOINT,
            data={
                'vectorstore_id': self.id,
                'query': query,
                'max_docs': max_docs,
                'filter': filter,
                'rerank': rerank,
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

    def list_documents(self, max_documents: int = None) -> dict:
        if not self.id:
            raise ValueError('Error listing documents: vector store object does not have an existing ID. It must be saved as a new vector store.')
        response = requests.post(
            API_VECTORSTORE_LIST_DOCUMENTS_ENDPOINT,
            data={
                'vectorstore_id': self.id,
                'max_documents': max_documents,
            },
            headers={
                'Public-Key': vectorshift.public_key,
                'Private-Key': vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error listing documents: {response.text}')
        response = response.json()

        return response

    def delete_documents(self, document_ids: list, filter: dict = None) -> dict:
        # TODO: Add the ability to delete multiple documents at once or by filter
        if not self.id:
            raise ValueError('Error deleting documents: vectorstore object does not have an existing ID. It must be saved as a new vectorstore.')
        
        if not isinstance(document_ids, list):
            document_ids = [document_ids]
        if len(document_ids) == 0:
            raise ValueError('Error deleting documents: document_ids must be a non-empty list of document IDs.')
        elif len(document_ids) > 1:
            raise NotImplementedError('Error deleting documents: deleting multiple documents at once is not yet supported.')
        response = requests.delete(
            API_VECTORSTORE_DELETE_DOCUMENTS_ENDPOINT,
            data={
                'vectorstore_id': self.id,
                'document_ids': document_ids,
            },
            headers={
                'Public-Key': vectorshift.public_key,
                'Private-Key': vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error deleting documents: {response.text}')
        response = response.json()

        return response

    def share(self, shared_users:list[str]) -> dict:
        if not self.id:
            raise ValueError('Error listing documents: vectorstore object does not have an existing ID. It must be saved in order to be shared.')
        
        shared_users_dicts = []
        for user in shared_users:
            shared_users_dicts.append({
                    'email': user,
                    'permissions': 'View',
            })
        response = requests.post(
            API_VECTORSTORE_SHARE_ENDPOINT,
            data={
                'vectorstore_id': self.id,
                'shared_users': json.dumps(shared_users_dicts),
            },
            headers={
                'Public-Key': vectorshift.public_key,
                'Private-Key': vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error sharing vectorstore: {response.text}')
        response = response.json()

        return response
    
    def fetch_shared(self) -> dict:
        if not self.id:
            raise ValueError('Error listing documents: vectorstore object does not have an existing ID. It must be saved.')
        
        response = requests.get(
            API_VECTORSTORE_FETCH_SHARED_ENDPOINT,
            headers={
                'Public-Key': vectorshift.public_key,
                'Private-Key': vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error fetching shared vectorstores: {response.text}')
        response = response.json()

        return response
    
    def remove_share(self, users_to_remove:list[str]) -> dict:
        if not self.id:
            raise ValueError('Error listing documents: vectorstore object does not have an existing ID. It must be saved in order to be shared.')
        
        response = requests.delete(
            API_VECTORSTORE_REMOVE_SHARE_ENDPOINT,
            data={
                'vectorstore_id': self.id,
                'users_to_remove': users_to_remove,
            },
            headers={
                'Public-Key': vectorshift.public_key,
                'Private-Key': vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error removing shared vectorstore: {response.text}')
        response = response.json()

        return response
