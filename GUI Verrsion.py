import random
import tkinter as tk

participants_list = ["Amit", "Josh", "Michael", "Jerome"]

spots = {
    "Taco Bell": {
        "participants": ["Josh"],
        "min_cost": 5,
        "max_cost": 10
    },
    "McDonald's": {
        "participants": ["Josh"],
        "min_cost": 3,
        "max_cost": 8
    },
    "Chick-fil-A": {
        "participants": ["Josh", "Amit"],
        "min_cost": 7,
        "max_cost": 15
    },
    "Wendy's": {
        "participants": ["Josh", "Michael"],
        "min_cost": 6,
        "max_cost": 12
    },
    "Publix": {
        "participants": ["Michael"],
        "min_cost": 100,
        "max_cost": 150
    }
    # Add more spots here with their respective participants, min_cost, and max_cost
}

def choose_spot():
    selected_participants = [participant for participant, var in zip(participants_list, participant_vars) if var.get() == 1]
    budget = float(budget_entry.get())

    weighted_spots = []
    for spot in spots:
        spot_weight = sum(1 for participant in selected_participants if participant in spots[spot]["participants"])
        if spot_weight > 0 and spots[spot]["min_cost"] <= budget:
            weighted_spots.append((spot, spot_weight))
            print("weighted_spots are " + str(weighted_spots))

    if weighted_spots:
        weighted_spots.sort(key=lambda x: x[1], reverse=True)
        chosen_spot = random.choice(weighted_spots[:4])  # Randomly select from top 3 weighted spots
        print("chosen_spots are " + str(chosen_spot))
        min_cost = spots[chosen_spot[0]]["min_cost"]
        max_cost = spots[chosen_spot[0]]["max_cost"]
        result_label.config(text=f"Chosen spot: {chosen_spot[0]}\nCost range: ${min_cost} - ${max_cost}")
    else:
        result_label.config(text="No suitable spots found.")

# Create the GUI
window = tk.Tk()
window.title("Lunch Spot Chooser")

participants_label = tk.Label(window, text="Participants:")
participants_label.pack()

participant_vars = []
for participant in participants_list:
    participant_var = tk.IntVar()
    participant_checkbutton = tk.Checkbutton(window, text=participant, variable=participant_var)
    participant_checkbutton.pack()
    participant_vars.append(participant_var)

budget_label = tk.Label(window, text="Budget:")
budget_label.pack()

budget_entry = tk.Entry(window)
budget_entry.pack()

choose_button = tk.Button(window, text="Choose", command=choose_spot)
choose_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
