import os
import time
from ..logger import get_logger
logging = get_logger()



# from openai import AzureOpenAI
# client = AzureOpenAI(azure_endpoint="https://openai-test-uksouth.openai.azure.com/",
# api_version="2023-07-01-preview",
# api_key=os.getenv('AZURE_OPENAI_API_KEY'),
# api_key=openai_api_key)
import openai
from openai import OpenAI
from openai import AzureOpenAI

# import sys
# sys.path.append('../../llm_wrap')
# sys.path.append('/Users/akihitosudo/Dropbox/src/llm_wrap/llm_wrap')
# sys.path.append('./llm_wrap')
# from .. import app_constants
# import llm_wrap.app_constants as app_constants
# from ..app_constants import PRODUCTION, IS_AZURE

def parse_str_to_bool(s):
    if isinstance(s, bool):
        return s
    if s.lower() == "true":
        return True
    elif s.lower() == "false":
        return False
    else:
        raise ValueError("Invalid boolean string")


def is_azure_env():
    return parse_str_to_bool(os.environ.get('IS_AZURE', True))

def is_production_env():
    return parse_str_to_bool(os.environ.get('LLM_WRAP_PRODUCTION', True))


logging.info(f"is_production: {is_production_env()}")
logging.info(f"is_azure: {is_azure_env()}")

def initialize_client_and_model(is_azure, is_production):
    from openai import OpenAI, AzureOpenAI
    import os

    if is_azure:
        logging.info("#A#A#A#A#A#A Using Azure API #A#A#A#A#A#A ")
        client = AzureOpenAI(
            api_key=os.getenv('AZURE_OPENAI_API_KEY'),
            azure_endpoint="https://openai-test-uksouth.openai.azure.com/",
            api_version="2023-12-01-preview",
        )
        if is_production:
            model = "gpt-4-1106-Preview-azure"
        else:
            model = "gpt-35-turbo-1106-azure"
        logging.info(f"GPT model: {model}")
    else:
        logging.info("%O%O%O%O%O% Using OpenAI API %O%O%O%O%O%")
        openai_api_key = os.getenv('OPENAI_API_KEY')
        client = OpenAI(api_key=openai_api_key)
        if is_production:
            model = "gpt-4-1106-preview"
        else:
            model = "gpt-3.5-turbo-1106"
        logging.info(f"GPT model: {model}")

    return client, model

def generate_ai_stream(messages, is_json=True, temperature=0, client=None, model=None, is_azure=None, is_production=None):
    # logging.debug(f"[azure_api#generate_ai_stream] start with messages: {messages}")

    is_azure = is_azure or is_azure_env()
    is_production = is_production or is_production_env()

    # Set up the client and model by the environment variables
    tmp_client, tmp_model = initialize_client_and_model(
        is_azure_env(), is_production_env())
    if client is None:
        client = tmp_client
    if model is None:
        model = tmp_model

    logging.info(f"[azure_api#generate_ai_stream] start with model: {model}")
    common_args = {
        # 'model': 'gpt-3.5-turbo',  # Uncomment and adjust as needed
        # 'model': "gpt-4-32k-test",  # Uncomment and adjust as needed
        # 'model': "gpt4-max-mrt",    # Uncomment and adjust as needed
        'model': model,
        'messages': messages,
        # 'messages': [
        #     {'role': 'user', 'content': f"Give me 50 random digits in JSON format"}
        # ],  # Uncomment and adjust as needed
        'temperature': temperature,
        'stream': True
    }
    if is_json:
        common_args['response_format'] = {"type": "json_object"}
    response = client.chat.completions.create(**common_args)

    for chunk in response:
        # if 'choices' in dir(chunk) and len(chunk.choices) > 0 and hasattr(chunk.choices[0], 'delta'):
        finish_reason = None
        if len(chunk.choices) > 0:
            delta = chunk.choices[0].delta
            finish_reason = chunk.choices[0].finish_reason
            try:
                for char in delta.content:
                    # logging.debug(f"[azure_api#generate_ai_stream] char: {char}")
                    # yield "random"
                    yield char  # Each event is formatted as "data: <data>\n\n"
            except:
                pass
        if finish_reason == 'stop':
            # logging.info(f"##########\n finish_reason: {finish_reason} ###########\n\n")
            break  # Stop the generator

def chatCompletion(messages, temperature=0.5, max_tokens=None, top_p=0.5, frequency_penalty=0, presence_penalty=0, stop=None, client=None, model=None, retries=0, sleep_period=0):
    """
    Generates a chat completion using the OpenAI API.

    Args:
        messages (list): A list of message objects, where each object has a 'role' (either "system", "user", or "assistant") and 'content' (the content of the message).
        temperature (float, optional): Controls the randomness of the output. Higher values make the output more random, while lower values make it more deterministic. Defaults to 0.5.
        max_tokens (int, optional): The maximum number of tokens to generate in the completion. Defaults to None.
        top_p (float, optional): Controls the diversity of the output by setting a threshold for cumulative probability of the generated tokens. Defaults to 0.5.
        frequency_penalty (float, optional): Controls the penalty for using frequent tokens in the output. Higher values discourage the model from repeating the same tokens. Defaults to 0.
        presence_penalty (float, optional): Controls the penalty for using tokens that were already present in the input. Higher values discourage the model from reusing the same tokens. Defaults to 0.
        stop (str or list, optional): One or more stop sequences to stop generation at. Defaults to None.
        client (object, optional): The OpenAI API client. If not provided, it will be initialized based on the environment variables.
        model (str, optional): The model to use for chat completion. If not provided, it will be initialized based on the environment variables.
        retries (int, optional): The number of times to retry the API call if it fails. Default is 0.
        sleep_period (int, optional): The number of seconds to wait between retries. Default is 0.

    Returns:
        object: The response object from the OpenAI API containing the generated completion.
    """
    logging.info(f"[azure_api#chatCompletion] start")
    common_args = {
        'messages': messages,
        'temperature': temperature,
        'top_p': top_p,
        'frequency_penalty': frequency_penalty,
        'presence_penalty': presence_penalty,
        'stop': stop
    }

    if max_tokens is not None:
        common_args['max_tokens'] = max_tokens

    # Set up the client and model by the environment variables
    tmp_client, tmp_model = initialize_client_and_model(
        is_azure_env(), is_production_env())
    if client is None:
        client = tmp_client
    if model is None:
        model = tmp_model

    common_args['model'] = model

    for i in range(retries + 1):
        try:
            logging.debug(f"[azure_api#chatCompletion] call API with: {common_args}")
            response = client.chat.completions.create(**common_args)
            logging.info(f"response text: {response.choices[0].message.content}")
            return response
        except openai.RateLimitError as e:
            logging.error(f"Rate limit exceeded: {e}")
            raise
        except Exception as e:
            logging.warning(f"Attempt {i+1} failed with exception: {e}")
            if i < retries:
                time.sleep(sleep_period)
            else:
                raise Exception(f"All {retries+1} attempts failed. Check the logs for exception details.")