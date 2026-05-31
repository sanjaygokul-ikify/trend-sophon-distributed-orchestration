import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration settings
class Config:
    def __init__(self):
        self.host = os.environ.get('HOST', 'localhost')
        self.port = int(os.environ.get('PORT', 8080))

    def get_host(self) -> str:
        return self.host

    def get_port(self) -> int:
        return self.port

config = Config()
