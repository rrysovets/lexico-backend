import requests
import json
import re


def int_to_bool_status_converter(seq):
    """Converts the first element of a tuples to boolean, preserving the second element. return iterator"""
    for tup in seq:
        yield (bool(tup[0]), tup[1])


def fetch_ai(
    content,
    api_key,
    api_url="https://openrouter.ai/api/v1/chat/completions",
    content_type="application/json",
    model="deepseek/deepseek-prover-v2:free",
    role="user",
) -> dict:
    """
    Sends a prompt to the  AI API and extracts a flat JSON dictionary from the model's response.

    Args:
        content (str): The prompt content to be sent to the model (typically an instruction for generating a dictionary).
        api_key (str): Authorization token in the format 'Bearer <token>'.
        api_url (str, optional): The endpoint of the AI API. Defaults to "https://openrouter.ai/api/v1/chat/completions".
        content_type (str, optional): HTTP Content-Type header. Defaults to "application/json".
        model (str, optional): The model identifier to be used. Defaults to "deepseek/deepseek-prover-v2:free".
        role (str, optional): The role for the message (e.g., 'user' or 'system'). Defaults to "user".

    Returns:
        dict: A flat dictionary extracted from the model's response, where keys are English words and values are Russian translations.
    """
    response = requests.post(
        url=api_url,
        headers={
            "Authorization": api_key,
            "Content-Type": content_type,
        },
        data=json.dumps(
            {
                "model": model,
                "messages": [
                    {
                        "role": role,
                        "content": content,
                    }
                ],
            }
        ),
    )
    dirty_result: str = json.loads(response.content.decode())["choices"][0]["message"][
        "content"
    ]
    clean_result: str = re.search(r"\{.*\}", dirty_result, flags=re.DOTALL).group()

    return json.loads(clean_result)
