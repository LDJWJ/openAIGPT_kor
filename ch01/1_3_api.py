import os
import openai

# reading variables from .env file, namely API_KEY and ORG_ID.
with open(".env") as env:
   for line in env:
       key, value = line.strip().split("=")
       os.environ[key] = value

# Initializing the API key and organization id
openai.api_key = os.environ.get("API_KEY")
openai.organization = os.environ.get("ORG_ID")

# Calling the API and listing models
models = openai.Model. list ()
print(models)
