from celery_app import app
from .utils import fetch_ai
from core.config.settings import env


@app.task
def get_generated_module(theme,count_of_words=10):
    # return {'word':'слово'}
    return fetch_ai(
        content=f"""
        Respond with a **valid JSON dictionary only** (no markdown, no explanations). 
        Dictionary should be flat (no nested keys), with exactly {count_of_words} word pairs.
        Keys: English words in lowercase. Values: Russian translations in lowercase.
        Example: {{"apple": "яблоко", "tree": "дерево"}}
        Theme: '{theme}'
        number of word pairs: {count_of_words}
        
        """,
        api_key=f"Bearer {env('AI_API_KEY')}",
    )
