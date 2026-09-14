from .compiler import CompilerApiClient  # Import the CompilerApiClient class from .compiler module
from .tools import ToolsApiClient  # Import the ToolsApiClient class from .tools module

class Codegyan:
    # Singleton pattern to ensure only one instance of the class is created
    _instance = None
    
    # Override the __new__ method to ensure only one instance of the class is created
    def __new__(cls, api_key, client_id):
        if cls._instance is None:
            cls._instance = super(Codegyan, cls).__new__(cls)
            # Initialize only once
            cls._instance._initialized = False
        return cls._instance
    
    # Initialize the Codegyan API client with API key and client ID
    def __init__(self, api_key, client_id):
        # Prevent re-initialization
        if self._initialized:
            return
            
        # Args:
        # - api_key (str): The API key for authentication.
        # - client_id (str): The client ID for identification.
        self.api_key = api_key
        self.client_id = client_id

        # Initialize the instances
        self.compilerApiClient = CompilerApiClient(self.api_key, self.client_id)
        self.toolsApiClient = ToolsApiClient(self.api_key, self.client_id)
        
        # Mark as initialized
        self._initialized = True