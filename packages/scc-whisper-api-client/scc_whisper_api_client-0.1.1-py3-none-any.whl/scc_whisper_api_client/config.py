"""Configuration for the SCC AI Services Client."""
import os
from dotenv import load_dotenv

load_dotenv()

SCC_USERNAME = os.getenv("USERNAME", "bib-0001")
SCC_PASSWORD = os.getenv("PASSWORD", None)
SCC_API_BASE_URL = os.getenv("API_BASE_URL", "https://test.ai-services.scc.kit.edu/")
