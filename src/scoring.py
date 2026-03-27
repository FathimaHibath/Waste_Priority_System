def compute_priority(fill_level, waste_probs, decomposition_risk):

    contamination_risk = waste_probs.max()

    alpha = 0.3
    beta = 0.3
    gamma = 0.4

    priority_score = (
        alpha * fill_level +
        beta * contamination_risk +
        gamma * decomposition_risk
    )

    return round(priority_score, 2)


def get_priority_label(score):
    if score >= 0.7:
        return "Collect Immediately !"
    elif score >= 0.4:
        return "Schedule Collection !"
    else:
        return "Low Priority !"
