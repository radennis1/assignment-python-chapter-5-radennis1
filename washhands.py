# Follow the instructions for what to code in this file.

# Ryan Dennis

# Lists of Mother Mortality
mortality_before = [
    18.1,
    15.4,
    19.0,
    13.4,
    10.2,
    13.1,
    18.1,
    14.4,
    15.0,
    10.8,
    5.4,
    12.2
]

mortality_after = [
    0.7,
    0.0,
    0.7,
    1.0,
    1.1,
    0.4,
    0.0,
    1.0,
    2.3,
    2.9,
    1.3
]

# Loop functions to calculate average mortality rates before and after hand washing policy


def before(percent_before):
    sum_before = 0
    for percentage in percent_before:
        sum_before += percentage

    avg = sum_before / len(percent_before)
    return avg


def after(percent_after):
    sum_after = 0
    for percentage in percent_after:
        sum_after += percentage

    avg = sum_after / len(percent_after)
    return avg


print(
    f"Average mortality rate before hand washing policy: {before(mortality_before):.2f}")

print(
    f"Average mortality rate after hand washing policy: {after(mortality_after):.2f}")
