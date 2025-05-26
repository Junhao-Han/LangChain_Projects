import getpass
import os

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

# Initialize the model
model = init_chat_model("gpt-4o-mini", model_provider="openai")

# Create Messages
messages = [
    SystemMessage("Translate the user's input into French."),
    HumanMessage("Hello, how are you?"),
]

# Invoke the model and print the result
response = model.invoke(messages)
print(response.content)

# python translator.py