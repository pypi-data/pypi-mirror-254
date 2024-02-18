import os
from dotenv import load_dotenv

load_dotenv()

IAMCORE_URL: str = os.getenv("IAMCORE_URL", "http://iam.kaatech.com")
IAMCORE_ISSUER_URL: str = os.environ.get('IAMCORE_ISSUER_URL', 'http://iam.kaatech.com/auth')
SYSTEM_BACKEND_CLIENT_ID: str = os.environ.get('SYSTEM_BACKEND_CLIENT_ID')
