'''
A translator that uses a prompt template to translate text.
'''
import getpass
import os

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

# Initialize the model
model = init_chat_model("gpt-4o-mini", model_provider="openai")

# Create a prompt template for translation
system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({"language": "Italian", "text": "hi!"})

prompt.to_messages()

# Invoke the model and print the result
response = model.invoke(prompt.to_messages())
print(response.content)

# python translator_prompt.py