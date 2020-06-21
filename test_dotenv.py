from dot_env import load_dotenv
load_dotenv()

import os

passw=os.getenv('password')

print(passw)
