# Follow the instructions for how to code this application

# Ryan Dennis

# Variables
guest_list = []
num_guest = 0

# While Loop for Guest List Input
while num_guest >= 0:
    user_input = input("Enter a guest's name or type 'end' to stop.\n")
    if user_input.lower() == "end":
        break
    else:
        guest_list.append(user_input)
        num_guest = len(guest_list)

# Calculate Guest Cost
cost = num_guest * 12

# For Loop to Print Guest Names
for guest in guest_list:
    print(guest)

print(f"You have invited {num_guest} guests at a cost of ${cost:.2f}.")
