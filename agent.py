import autogen
from anthropic import Anthropic
import os 
from dotenv import load_dotenv

load_dotenv()
AnthropicApiKey = os.getenv('AnthropicApiKey')
config_list_claude = [
    {
        # Choose your model name.
        "model": "claude-3-5-sonnet-20241022",
        # You need to provide your API key here.
        "api_key": AnthropicApiKey,
        "api_type": "anthropic",
    }]

# agent = autogen.ConversableAgent(
#     "chatbot",
#     llm_config={
#         "config_list": config_list_claude,
#     },
#     code_execution_config=False,  # Turn off code execution, by default it is off.
#     function_map=None,  # No registered functions, by default it is None.
#     human_input_mode="NEVER",  # Never ask for human input.,
#     max_consecutive_auto_reply=1
# )
# reply = agent.generate_reply(messages=[{"content": "Tell me a joke.", "role": "user"}])
# print(reply['content'])

cathy = autogen.ConversableAgent(
    "cathy",
    system_message="Your name is Cathy and you are a part of a duo of comedians.",
    llm_config={"config_list": config_list_claude },
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = autogen.ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a part of a duo of comedians.",
    llm_config={"config_list": config_list_claude },
    human_input_mode="NEVER",  # Never ask for human input.
)

result = joe.initiate_chat(cathy, message="Cathy, tell me a joke.", max_turns=2)

print(result)