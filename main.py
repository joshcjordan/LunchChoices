import random


def generate_lunch_option(spots, price_range):
    valid_options = []
    for spot, price_info in spots.items():
        max_price = price_info["max"]
        if price_range >= price_info["min"]:
            valid_options.append(spot)

    if not valid_options:
        return "No options available within the given price range."

    random_option = random.choice(valid_options)
    return random_option


# Predefined list of lunch spots with price ranges
spots = {
    "Zaxby's": {"min": 10, "max": 20},
    "McDonalds": {"min": 5, "max": 15},
    "Aubreys": {"min": 15, "max": 25},
    "Shane's Rib Shack": {"min": 8, "max": 18},
    "Dos Bros": {"min": 12, "max": 22}
}

# User input for available budget
budget = float(input("Enter your available budget: "))

lunch_option = generate_lunch_option(spots, budget)
print("Let's eat at " + lunch_option + "!")
