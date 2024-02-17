"""Configuration for the SCC AI Services Client."""
import os
from dotenv import load_dotenv

load_dotenv()

SCC_USERNAME = os.getenv("USERNAME", "bib-0001")
SCC_PASSWORD = os.getenv("PASSWORD", None)
SCC_API_BASE_URL = os.getenv("API_BASE_URL", "https://test.ai-services.scc.kit.edu/")

SCC_VERIFY_SSL = os.getenv("VERIFY_SSL", "True").lower() == "true"

SYNC_MAX_RETRIES = int(os.getenv("MAX_RETRIES", "10"))
SYNC_MAX_WAIT_TIME_SEC = int(os.getenv("MAX_WAIT_TIME_SEC", "600"))
