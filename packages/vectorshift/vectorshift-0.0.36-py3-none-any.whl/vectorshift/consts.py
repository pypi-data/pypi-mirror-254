from dotenv import load_dotenv
from enum import Enum
import os

# Pipeline input and output types.
INPUT_NODE_TYPES = ['text', 'file']
OUTPUT_NODE_TYPES = ['text', 'formatted_text', 'file']

# Pipeline sharing.
class PipelineShareStatus(str, Enum):
    OWNED = 'owned'
    RUN = 'run'
    EDIT = 'edit'

# Parameters for loading/processing token data
DEFAULT_CHUNK_SIZE = 400
DEFAULT_CHUNK_OVERLAP = 0

# Node-specific parameters. Map of LLM names to token limits
SUPPORTED_OPENAI_LLMS = {
    'gpt-3.5-turbo': 4096,
    'gpt-3.5-turbo-16k': 16384,
    'gpt-4': 8192,
    'gpt-4-32k': 32768,
    'gpt-4-turbo': 1200000,
    'gpt-3.5-turbo-instruct': 4096,
}

SUPPORTED_ANTHROPIC_LLMS = {
    'claude-v2': 100000, 
    'claude-instant': 100000, 
    'claude-v2.1': 200000
}

SUPPORTED_COHERE_LLMS = {
    'command': 4000,
    'command-light': 4000,
}

SUPPORTED_AWS_LLMS = {
    'titan-text-express': 8000,
    'titan-text-lite': 8000,
}

SUPPORTED_META_LLMS = {
    'llama2-chat-13b': 4096,
    'llama2-chat-70b': 4096,
    'llama2-13b': 4096,
    'llama2-70b': 4096,
}

SUPPORTED_OPENSOURCE_LLMS = {
    'mistralai/Mistral-7B-v0.1': 4096,
    'mistralai/Mistral-7B-Instruct-v0.1': 4096,
    'mistralai/Mistral-7B-Instruct-v0.2': 32768,
    'mistralai/Mixtral-8x7B-Instruct-v0.1': 32768,
    'mistralai/Mixtral-8x7B-v0.1': 32768,
}

SUPPORTED_GOOGLE_LLMS = {
    'gemini-pro': 32760,
    'text-bison': 8192,
    'text-bison-32k': 32760,
    'text-unicorn': 32760,
}

# Map of possible single-prompt LLMs to corresponding LLM node 
# types (as stored in Mongo), node names, supported LLMs, and task
PROMPT_LLM_FAMILIES:dict[str, dict[str, any]] = {
    'anthropic': {
        'node_type': 'llmAnthropic',
        'node_class_name': 'AnthropicLLMNode',
        'models': SUPPORTED_ANTHROPIC_LLMS,
        'task_name': 'llm_anthropic'
    },
    'cohere': {
        'node_type': 'llmCohere',
        'node_class_name': 'CohereLLMNode',
        'models': SUPPORTED_COHERE_LLMS,
        'task_name': 'llm_cohere'
    },
    'aws': {
        'node_type': 'llmAWS',
        'node_class_name': 'AWSLLMNode',
        'models': SUPPORTED_AWS_LLMS,
        'task_name': 'llm_aws'
    },
    'meta': {
        # note: the node type has llama, not meta, in the name
        'node_type': 'llmLlama',
        'node_class_name': 'MetaLLMNode',
        'models': SUPPORTED_META_LLMS,
        'task_name': 'llm_llama'
    },
    'open_source': {
        'node_type': 'llmOpenSource',
        'node_class_name': 'OpenSourceLLMNode',
        'models': SUPPORTED_OPENSOURCE_LLMS,
        'task_name': 'llm_opensource'
    }, 
    'google': {
        'node_type': 'llmGoogle',
        'node_class_name': 'GoogleLLMNode',
        'models': SUPPORTED_GOOGLE_LLMS,
        'task_name': 'llm_google'
    }
}

# Map of image gen models to possible sizes (in both dimensions; if in the 
# future non-square images can be generated we'll update this), and # of
# possible images to generate
SUPPORTED_IMAGE_GEN_MODELS = {
    # The SDK uses dashes instead of dots
    'DALL-E 2': ([256, 512, 1024], list(range(1, 5))),
    'Stable Diffusion XL': ([512], [1]),
    'DALL-E 3': ([1024, (1024, 1792), (1792, 1024)], [1])
}
SUPPORTED_SPEECH_TO_TEXT_MODELS = ['OpenAI Whisper']
# Some delimiters are given special names in MongoDB rather than
# just using strings.
TEXT_SPLIT_DELIMITER_NAMES = {
    ' ': 'space',
    '\n': 'newline'
    # default case: 'character(s)'
}
# Corresponding values are the default memory windows used. A value of 0
# means a window isn't (and shouldn't be) used
CHAT_MEMORY_TYPES = {
    'Full - Formatted': 0,
    'Full - Raw': 0,
    'Message Buffer': 10,
    'Token Buffer': 2048
}

# Specifications of the input names that dataloader nodes expect. 
# A dictionary that maps the dataloader type to a list of expected input names
# and the particular task name assigned to the node in Mongo.
DATALOADER_PARAMS = {
    'File': {
        'input_names': ['file'],
        'task_name': 'load_file',
    },
    'CSV Query': {
        'input_names': ['query', 'csv'],
        'task_name': 'query_csv',
    },
    'URL': {
        'input_names': ['url'],
        'task_name': 'load_url',
    },
    'Wikipedia': {
        'input_names': ['query'],
        'task_name': 'load_wikipedia',
    },
    'YouTube': {
        'input_names': ['url'],
        'task_name': 'load_youtube',
    },
    'Arxiv': {
        'input_names': ['query'],
        'task_name': 'load_arxiv',
    },
    'SerpAPI': {
        'input_names': ['apiKey', 'query'],
        'task_name': 'load_serpapi',
    },
    'Git': {
        'input_names': ['repo'], 
        'task_name': 'load_git'
    },
    # DEPRECATED
    'Notion': {
        'input_names': ['token', 'database'],
        'task_name': 'load_notion'
    },
    # DEPRECATED
    'Confluence': {
        'input_names': ['username', 'apiKey', 'url'],
        'task_name': 'load_confluence'
    }
}

# Specifications of the input names that integration nodes expect. 
# A doubly-nested dictionary. In the first level, we map the integration node type (as stored in the object's type field in the Mongo integrations table) to
# a dict of supported functions for that integration (as will be described in 
# the node's data.function.name field in the Mongo pipeline table). In the 
# second level, each function name is mapped to its task/display name and its
# input/output details. Note: the function name should be added to the resulting 
# object value's name field if working with Mongo.

# This should be analogous to app/src/reactflow/nodes/integration-schema.js. 
# The only difference is that instead of a functions field with a list, we 
# store functions as a dict, with each 'name' field being the key.
INTEGRATION_PARAMS = {
    'Pinecone': {
        'run_query': {
            'taskName': 'pinecone.run_query',
            'displayName': 'Run Query',
            'inputs': [
                { 'name': 'query', 'displayName': 'Query', 'multiInput': True }
            ],
            'outputs': [{ 'name': 'output', 'displayName': 'Output' }],
            'fields': [],
        },
        'load_data': {
            'taskName': 'pinecone.load_data',
            'displayName': 'Load Data',
            'inputs': [
                { 'name': 'data', 'displayName': 'Data', 'multiInput': True }
            ],
            'outputs': [{ 'name': 'output', 'displayName': 'Output' }],
            'fields': [],
        }
    },
    'Salesforce': {
        'run_sql_query': {
            'taskName': 'salesforce.run_sql_query',
            'displayName': 'Run SQL Query',
            'inputs': [{ 
                'name': 'sql_query', 
                'displayName': 'SQL Query', 
                'multiInput': True 
            }],
            'outputs': [{ 'name': 'output', 'displayName': 'Output'}],
            'fields': []
        },
    },
    'Google Drive': {
        'read_files': {
            'taskName': 'google_drive.read_files',
            'displayName': 'Read Files',
            'inputs': [],
            'outputs': [{ 'name': 'output', 'displayName': 'Output' }],
            'fields': []
        },
        'save_files': {
            'taskName': 'google_drive.save_files',
            'displayName': 'Save Files',
            'inputs': [
                { 'name': 'name', 'displayName': 'Name', 'multiInput': False },
                { 'name': 'files', 'displayName': 'Files', 'multiInput': True },
            ],
            'outputs': [],
            'fields': []
        },
    },
    'Gmail': {
        'create_draft': {
            'taskName': 'gmail.create_email_draft',
            'displayName': 'Create Email Draft',
            'inputs': [
                { 'name': 'subject', 'displayName': 'Subject', 'multiInput': False },
                { 'name': 'recipients', 'displayName': 'To:', 'multiInput': False },
                { 'name': 'body', 'displayName': 'Body', 'multiInput': False },
            ],
            'outputs': [],
            'fields': [],
        },
        'send_email': {
            'taskName': 'gmail.send_email',
            'displayName': 'Send Email',
            'inputs': [
                { 'name': 'subject', 'displayName': 'Subject', 'multiInput': False },
                { 'name': 'recipients', 'displayName': 'To:', 'multiInput': False },
                { 'name': 'body', 'displayName': 'Body', 'multiInput': False },
            ],
            'outputs': [],
            'fields': [],
        },
        'draft_reply': {
            'taskName': 'gmail.draft_reply',
            'displayName': 'Draft Reply',
            'inputs': [
                { 'name': 'recipients', 'displayName': 'To:', 'multiInput': False },
                { 'name': 'body', 'displayName': 'Body', 'multiInput': False },
                { 'name': 'email_id', 'displayName': 'Email Id', 'multiInput': False },
            ],
            'outputs': [],
            'fields': [],
        },
        'send_reply': {
            'taskName': 'gmail.send_reply',
            'displayName': 'Send Reply',
            'inputs': [
                { 'name': 'recipients', 'displayName': 'To:', 'multiInput': False },
                { 'name': 'body', 'displayName': 'Body', 'multiInput': False },
                { 'name': 'email_id', 'displayName': 'Email Id', 'multiInput': False },
            ],
            'outputs': [],
            'fields': [],
        },
    },
    # Not currently accessible to users in the no-code builder
    'Microsoft': {},
    # Not currently accessible to users in the no-code builder
    'Notion': {
        'read_data': {
            'taskName': 'notion.read_data',
            'displayName': 'Read Data',
            'inputs': [],
            'outputs': [{ 'name': 'output', 'displayName': 'Output' }],
            'fields': []
        },
        'write_to_database': {
            'taskName': 'notion.write_to_database',
            'displayName': 'Write to Database',
            'inputs': [],
            'outputs': [{'name': 'output', 'displayName': 'Output'}],
        },
        'create_new_page': {
            'taskName': 'notion.create_new_page',
            'displayName': 'Create New Page',
            'inputs': [
                {'name': 'parent_page_id', 'displayName': 'Parent Page Id', 'multiInput': False},
                {'name': 'title', 'displayName': 'Title', 'multiInput': False},
                {'name': 'content', 'displayName': 'Content', 'multiInput': False},
            ],
            'outputs': [{'name': 'output', 'displayName': 'Output'}],
        }
    },
    # Not currently accessible to users in the no-code builder
    'Airtable': {
        'read_tables': {
            'taskName': 'airtable.read_tables',
            'displayName': 'Read Tables',
            'inputs': [],
            'outputs': [{'name': 'output', 'displayName': 'Output'}],
            'fields': [{
                'name': 'selectedTables', 
                'displayName': 'Select Tables', 
                'type': 'button', 
                'completedValue': 'Tables Selected'
            }],
        },
    },
    'HubSpot': {
        'search_contacts': {
            'taskName': 'hubspot.search_companies',
            'displayName': 'Search Companies',
            'inputs': [
                {'name': 'query', 'displayName': 'Query', 'multiInput': False},
            ],
            'outputs': [
                {'name': 'output', 'displayName': 'Output'}
            ],
            'fields': [],
        },
        'search_companies': {
            'taskName': 'hubspot.search_companies',
            'displayName': 'Search Companies',
            'inputs': [
                {'name': 'query', 'displayName': 'Query', 'multiInput': False},
            ],
            'outputs': [
                {'name': 'output', 'displayName': 'Output'}
            ],
            'fields': [],
        },
        'search_deals': {
            'taskName': 'hubspot.search_deals',
            'displayName': 'Search Deals',
            'inputs': [
                {'name': 'query', 'displayName': 'Query', 'multiInput': False},
            ],
            'outputs': [
                {'name': 'output', 'displayName': 'Output'}
            ],
            'fields': [],
        }
    },
    'SugarCRM': {
        'get_records': {
            'taskName': 'sugar_crm.get_records',
            'displayName': 'Get Records',
            'inputs': [
                {'name': 'module', 'displayName': 'Module', 'multiInput': False},
                {'name': 'filter', 'displayName': 'Filter', 'multiInput': False},
            ],
            'outputs': [
                {'name': 'output', 'displayName': 'Output'}
            ],
            'fields': [],
        }
    },
    # Not currently accessible to users in the no-code builder
    'Linear': {
        'read_data': {
            'taskName': 'linear.read_data',
            'displayName': 'Read Data',
            'inputs': [],
            'outputs': [
                {'name': 'output', 'displayName': 'Output'}
            ],
            'fields': [],
        }
    },
    # Not currently accessible to users in the no-code builder
    'Slack': {
        'read_data': {
            'taskName': 'slack.read_data',
            'displayName': 'Read Data',
            'inputs': [],
            'outputs': [{ 'name': 'output', 'displayName': 'Output' }],
            'fields': [],
        }
    },
    # Not currently accessible to users in the no-code builder
    'Discord': {
        'read_data': {
            'taskName': 'discord.read_data',
            'displayName': 'Read Data',
            'inputs': [],
            'outputs': [{ 'name': 'output', 'displayName': 'Output' }],
            'fields': [],
        }
    }
}

# Relevant API endpoints the SDK code needs. Could also refactor to get rid of
# MODE entirely.
load_dotenv()
MODE = os.environ.get('ENVIRONMENT', 'PROD')
DOMAIN = 'http://localhost:8000' if MODE != 'PROD' else 'https://api.vectorshift.ai'

API_FILE_FETCH_ENDPOINT = f'{DOMAIN}/api/files/fetch'
API_TRANSFORMATION_FETCH_ENDPOINT = f'{DOMAIN}/api/transformations/fetch'

API_VECTORSTORE_SAVE_ENDPOINT = f'{DOMAIN}/api/vectorstores/add'
API_VECTORSTORE_FETCH_ENDPOINT = f'{DOMAIN}/api/vectorstores/fetch'
API_VECTORSTORE_UPDATE_METADATA_ENDPOINT = f'{DOMAIN}/api/vectorstores/update-metadata'
API_VECTORSTORE_UPDATE_SELECTED_ITEMS_ENDPOINT = f'{DOMAIN}/api/vectorstores/update-selected-items'
API_VECTORSTORE_SYNC_ENDPOINT = f'{DOMAIN}/api/vectorstores/sync-vectorstore-integrations'
API_VECTORSTORE_LOAD_ENDPOINT = f'{DOMAIN}/api/vectorstores/load'
API_VECTORSTORE_QUERY_ENDPOINT = f'{DOMAIN}/api/vectorstores/query'
API_VECTORSTORE_LIST_DOCUMENTS_ENDPOINT = f'{DOMAIN}/api/vectorstores/list-documents'
API_VECTORSTORE_DELETE_DOCUMENTS_ENDPOINT = f'{DOMAIN}/api/vectorstores/delete-documents'
API_VECTORSTORE_SHARE_ENDPOINT = f'{DOMAIN}/api/vectorstores/share'
API_VECTORSTORE_FETCH_SHARED_ENDPOINT = f'{DOMAIN}/api/vectorstores/shared'
API_VECTORSTORE_REMOVE_SHARE_ENDPOINT = f'{DOMAIN}/api/vectorstores/shared/remove'

API_PIPELINE_SAVE_ENDPOINT = f'{DOMAIN}/api/pipelines/add'
API_PIPELINE_FETCH_ENDPOINT = f'{DOMAIN}/api/pipelines/fetch'
API_PIPELINE_RUN_ENDPOINT = f'{DOMAIN}/api/pipelines/run'
API_PIPELINE_GET_INPUTS_ENDPOINT = f'{DOMAIN}/api/pipelines/inputs'

API_AGENT_SAVE_ENDPOINT = f'{DOMAIN}/api/agents/add'
API_AGENT_FETCH_ENDPOINT = f'{DOMAIN}/api/agents/fetch'
API_AGENT_RUN_ENDPOINT = f'{DOMAIN}/api/agents/run'

API_CHATBOT_SAVE_ENDPOINT = f'{DOMAIN}/api/chatbots/add'
API_CHATBOT_FETCH_ENDPOINT = f'{DOMAIN}/api/chatbots/fetch'
API_CHATBOT_RUN_ENDPOINT = f'{DOMAIN}/api/chatbots/run'

API_INTEGRATION_FETCH_ALL_ENDPOINT = f'{DOMAIN}/api/integrations/list'
API_INTEGRATION_FETCH_ENDPOINT = f'{DOMAIN}/api/integrations/fetch'
API_INTEGRATION_SYNC_METADATA_ENDPOINT = f'{DOMAIN}/api/integrations/sync-metadata'
API_INTEGRATION_SYNC_ENDPOINT = f'{DOMAIN}/api/integrations/sync'
API_INTEGRATION_GET_ITEM_IDS_ENDPOINT = f'{DOMAIN}/api/integrations/get-item-ids'

API_AUTOMATION_LIST_ENDPOINT = f'{DOMAIN}/api/automations/list'
API_AUTOMATION_FETCH_ENDPOINT = f'{DOMAIN}/api/automations/fetch'
API_AUTOMATION_CREATE_ENDPOINT = f'{DOMAIN}/api/automations/create'
API_AUTOMATION_DELETE_ENDPOINT = f'{DOMAIN}/api/automations/delete'
API_AUTOMATION_GET_APPS_ENDPOINT = f'{DOMAIN}/api/automations/apps'
API_AUTOMATIONS_GET_EVENTS_ENDPOINT = f'{DOMAIN}/api/automations/events'
API_AUTOMATION_GET_TRIGGERS_ENDPOINT = f'{DOMAIN}/api/automations/triggers'
API_AUTOMATION_GET_PAYLOADS_ENDPOINT = f'{DOMAIN}/api/automations/get-payloads'
API_AUTOMATION_DEPLOY_ENDPOINT = f'{DOMAIN}/api/automations/deploy'
API_AUTOMATION_PROCESS_PAYLOADS_ENDPOINT = f'{DOMAIN}/api/automations/process-payloads'
