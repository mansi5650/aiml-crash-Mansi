student = [
    {"name":"mansi", "score":90},
    {"name":"riya", "score":85},
    {"name":"rahul", "score":80},
    {"name":"harsh", "score":75},
    {"name":"mneha", "score":95}
]

def classify(score):
    if score >= 90:
        return "A"

    elif score >= 75:
        return "B"

    elif score >= 60:
        return "C"

    elif score >= 40:
        return "D"

    else:
        return "F"

