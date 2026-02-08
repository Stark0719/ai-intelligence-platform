def label_match(score: float) -> str:
    if score >= 0.55:
        return "STRONG_MATCH"
    elif score >= 0.40:
        return "MEDIUM_MATCH"
    else:
        return "WEAK_MATCH"
