import pandas as pd


EMISSION_FACTORS = {
    "electricity": 0.82,
    "diesel": 2.68,
    "petrol": 2.31,
    "flight": 0.15,
}


def calculate_emission(activity_type, activity_value):

    factor = EMISSION_FACTORS.get(
        activity_type.lower(),
        0
    )

    emission = activity_value * factor

    return emission