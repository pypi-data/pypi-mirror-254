

from pydantic import BaseModel, Field

class ParameterDefinition(BaseModel):
    """
    Descript the parameters of a tool for openai function calling
    # TODO 
    """
    name: str
    description: str
    type: str

class ToolDefinition(BaseModel):
    name: str
    description: str
    type: str
    id: str
    parameters: list[ParameterDefinition] = Field(default_factory=list)

DEFAULT_TOOLS = {}


# (TODO couple to registered dataloader nodes in node file)
# For the purposes of agents, dataloader nodes should return a list of documents
# Could define the base functionality and use of a dataloader and inhrerit the functionality to use either as a node or as an agent tool 
DATALOADER_TOOLS= {}


def register_default_tool(tool_name: str):
    def decorator(tool_class):
        DEFAULT_TOOLS[tool_name] = tool_class
        return tool_class
    return decorator

def register_dataloader_tool(tool_name: str):
    def decorator(tool_class):
        DEFAULT_TOOLS[tool_name] = tool_class
        return tool_class
    return decorator


@register_default_tool("calculator")
class CalculatorToolDefinition(ToolDefinition):
    name = "calculator"
    description = "A calculator tool"
    type = "calculator"
    id = "calculator"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="expression", description="numerical expression to evaluate", type="string")]

    
@register_default_tool("code_interpreter")
class CodeInterpreterToolDefinition(ToolDefinition):
    name = "code_interpreter"
    description = "Execute python code to accomplish a task, save answer in variable result"
    type = "code_interpreter"
    id = "code_interpreter"
    parameters : list[ParameterDefinition] =  [ParameterDefinition(name="code", description="python code to execute", type="string")]


@register_default_tool("serpapi")
class SerpAPIToolDefinition(ToolDefinition):
    name = "serpapi"
    description = "Use the serpapi to to search the web"
    type = "serpapi"
    id = "serpapi"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="query", description="search query", type="string")]


@register_dataloader_tool("wikipedia_loader")
class WikipediaLoaderToolDefinition(ToolDefinition):
    name = "wikipedia_loader"
    description = "Load documents from wikipedia based on a query"
    type = "wikipedia_loader"
    id = "wikipedia_loader"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="query", description="search query", type="string")]


@register_dataloader_tool("url_loader")
class URLLoaderToolDefinition(ToolDefinition):
    name = "url_loader"
    description = "A url loader tool"
    type = "url_loader"
    id = "url_loader"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="url", description="url to load", type="string")]


@register_dataloader_tool("youtube_loader")
class YoutubeLoaderToolDefinition(ToolDefinition):
    name = "youtube_loader"
    description = "Load a youtube video from url, transcribe the audio, and return the text as a set of documents"
    type = "youtube_loader"
    id = "youtube_loader"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="url", description="video url", type="string")]


@register_dataloader_tool("arxiv_loader")
class ArxivLoaderToolDefinition(ToolDefinition):
    name = "arxiv_loader"
    description = "Load documents from arxiv based on a query"
    type = "arxiv_loader"
    id = "arxiv_loader"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="query", description="search query", type="string")]


@register_dataloader_tool("github_loader")
class GithubLoaderToolDefinition(ToolDefinition):
    name = "github_loader"
    description = "Load documents from github repo"
    type = "github_loader"
    id = "github_loader"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="repo", description="repository to load from", type="string")]


@register_dataloader_tool("notion_loader")
class NotionLoaderToolDefinition(ToolDefinition): # TODO how to deal with notion access token
    name = "notion_loader"
    description = "Load documents from notion database"
    type = "notion_loader"
    id = "notion_loader"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="database", description="database to load from", type="string")]


@register_dataloader_tool("confluence_loader") 
class ConfluenceLoaderToolDefinition(ToolDefinition): # TODO deal with confluence username and apikey
    name = "confluence_loader"
    description = "Load documents from confluence"
    type = "confluence_loader"
    id = "confluence_loader"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="url", description="url to load from", type="string")]


ADVANCED_TOOLS = {}


def register_advanced_tool(tool_name: str):
    def decorator(tool_class):
        ADVANCED_TOOLS[tool_name] = tool_class
        return tool_class
    return decorator


@register_advanced_tool("image_generation")
class ImageGenerationToolDefinition(ToolDefinition):
    name = "image_generation"
    description = "Generate an image"
    type = "image_generation"
    id = "image_generation"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="prompt", description="text prompt for image generation", type="string")]


@register_advanced_tool("speech_to_text")
class SpeechToTextToolDefinition(ToolDefinition):
    name = "speech_to_text"
    description = "Convert speech to text"
    type = "speech_to_text"
    id = "speech_to_text"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="audio", description="audio file", type="file")]


@register_advanced_tool('csv_query')
class CSVQueryToolDefinition(ToolDefinition):
    name = "csv_query"
    description = "Query a csv file"
    type = "csv_query"
    id = "csv_query"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="query", description="query to run", type="string"), ParameterDefinition(name="csv", description="csv file", type="string")]
    

VECTOR_DB_TOOLS = {}

def register_vector_db_tool(tool_name: str):
    def decorator(tool_class):
        VECTOR_DB_TOOLS[tool_name] = tool_class
        return tool_class
    return decorator


@register_vector_db_tool("vectordb_loader")
class VectorDBLoaderToolDefinition(ToolDefinition):
    name = "vectordb_loader"
    description = "Load documents into a vector database"
    type = "vectordb_loader"
    id = "vectordb_loader"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="documents", description="reference to documents to load", type="string")]


@register_vector_db_tool("vectordb_query")
class VectorDBQueryToolDefinition(ToolDefinition):
    name = "vectordb_query"
    description = "Query a vector database"
    type = "vectordb_query"
    id = "vectordb_query"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="query", description="query to run", type="string"), ParameterDefinition(name="database", description="database to query", type="string")]



TOOLKITS = {}

def register_toolkit(toolkit_name: str):
    def decorator(toolkit_class):
        TOOLKITS[toolkit_name] = toolkit_class
        return toolkit_class
    return decorator


class ToolKit(BaseModel):
    """
    Class to handle providing sets of default tools to the model
    """
    name: str
    tools: list[ToolDefinition] = None

@register_toolkit("vectordb")
class VectorDBToolKit(ToolKit):
    name = "vectordb"
    tools:list[ToolDefinition]  = [VectorDBLoaderToolDefinition(), VectorDBQueryToolDefinition()]


FILE_TOOLS = {}

def register_file_tool(tool_name: str):
    def decorator(tool_class):
        FILE_TOOLS[tool_name] = tool_class
        return tool_class
    return decorator

@register_file_tool("save_file")
class SaveFileToolDefinition(ToolDefinition):
    name = "save_file"
    description = "Save a file"
    type = "save_file"
    id = "save_file"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="files", description="files to save", type="file"), ParameterDefinition(name= "name", description="name of file", type="string")]


@register_file_tool("load_file")
class LoadFileToolDefinition(ToolDefinition): # TODO address file loading
    name = "load_file"
    description = "Load a file"
    type = "load_file"
    id = "load_file"
    parameters: list[ParameterDefinition] = [ParameterDefinition(name="name", description="name of file", type="string")]

@register_toolkit("file")
class FileToolKit(ToolKit):
    name = "file"
    tools: list[ToolDefinition] = [SaveFileToolDefinition(), LoadFileToolDefinition()]



# TODO deal with user defined objects as tools ie vectorstores, files an agent has access to, etc


ALL_TOOLS = {}

for tool in DEFAULT_TOOLS.values():
    ALL_TOOLS[tool().name] = tool

for tool in ADVANCED_TOOLS.values():
    ALL_TOOLS[tool().name] = tool

for tool in VECTOR_DB_TOOLS.values():
    ALL_TOOLS[tool().name] = tool

for tool in FILE_TOOLS.values():
    ALL_TOOLS[tool().name] = tool

for tool in DATALOADER_TOOLS.values():
    ALL_TOOLS[tool().name] = tool



            