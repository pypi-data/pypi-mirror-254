from string import ascii_uppercase


def has_caps(token: str) -> bool:
    for sym in token:
        if sym in ascii_uppercase:
            return True
    return False


def normalize_model_name(token: str) -> str:
    if not has_caps(token):
        token = token.title()
    return token.replace("_", "")
