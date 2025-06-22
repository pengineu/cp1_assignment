def mbti(message: str) -> str:
    if "..." in message:
        return "I"
    elif "!!!" in message:
        return "E"
    else:
        return "?"