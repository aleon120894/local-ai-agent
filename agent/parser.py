import json

def safe_parse(text: str):

    text = text.strip()

    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        return None

    try:
        return json.loads(text[start:end+1])

    except Exception:
        return None
