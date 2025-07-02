import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

# Get API key
if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

# Initialize chat model
model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

# Construct prompt templates
system_template = "Translate the following from English to {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{text}"),
    ]
)

# Input prompt
prompt = prompt_template.invoke({"language": "Malay", "text": "Hello world!"})
prompt.to_messages()

# Generate response
response = model.invoke(prompt)
print(response.content)