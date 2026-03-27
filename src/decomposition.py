def calculate_decomposition_risk(days_since):

    if days_since < 1:
        risk = 0.2
    elif days_since < 2:
        risk = 0.5
    else:
        risk = 0.8

    return risk