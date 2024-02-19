from .llms.gpt_api import chatCompletion
from typing import Literal


def get_response(llm_api:Literal["openai"]='openai', **kwargs) -> str:
    """
    This function acts as an interface for consumer libraries to get AI's response.
    It currently supports OpenAI's GPT API, but can be extended to support other APIs.

    Parameters:
    api (str): The API to use. Default is 'openai'.
    **kwargs: Arbitrary keyword arguments. These will be passed to the API function.

    Returns:
    The response from the AI.
    """
    if llm_api == 'openai':
        response = chatCompletion(**kwargs)
        return response.choices[0].message.content
    else:
        raise ValueError(f"Unsupported API: {llm_api}")