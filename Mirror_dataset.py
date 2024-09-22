import pandas as pd
import numpy as np

# Combined male and female percentages for each age (ages 18 to 100+)
age_distribution = {
    18: 0.67 + 0.64,
    19: 0.67 + 0.64,
    20: 0.66 + 0.63,
    21: 0.66 + 0.63,
    22: 0.67 + 0.64,
    23: 0.67 + 0.64,
    24: 0.66 + 0.64,
    25: 0.66 + 0.64,
    26: 0.66 + 0.64,
    27: 0.66 + 0.64,
    28: 0.67 + 0.65,
    29: 0.69 + 0.67,
    30: 0.70 + 0.68,
    31: 0.71 + 0.70,
    32: 0.72 + 0.71,
    33: 0.72 + 0.71,
    34: 0.70 + 0.69,
    35: 0.69 + 0.68,
    36: 0.68 + 0.67,
    37: 0.68 + 0.67,
    38: 0.68 + 0.67,
    39: 0.66 + 0.65,
    40: 0.67 + 0.66,
    41: 0.67 + 0.66,
    42: 0.66 + 0.65,
    43: 0.66 + 0.65,
    44: 0.63 + 0.62,
    45: 0.61 + 0.61,
    46: 0.60 + 0.60,
    47: 0.58 + 0.58,
    48: 0.59 + 0.59,
    49: 0.57 + 0.58,
    50: 0.58 + 0.59,
    51: 0.61 + 0.61,
    52: 0.65 + 0.65,
    53: 0.63 + 0.64,
    54: 0.61 + 0.61,
    55: 0.59 + 0.60,
    56: 0.59 + 0.61,
    57: 0.60 + 0.61,
    58: 0.62 + 0.64,
    59: 0.63 + 0.66,
    60: 0.63 + 0.66,
    61: 0.63 + 0.66,
    62: 0.62 + 0.66,
    63: 0.61 + 0.65,
    64: 0.59 + 0.64,
    65: 0.59 + 0.63,
    66: 0.57 + 0.62,
    67: 0.54 + 0.60,
    68: 0.52 + 0.58,
    69: 0.50 + 0.56,
    70: 0.48 + 0.54,
    71: 0.45 + 0.52,
    72: 0.43 + 0.50,
    73: 0.40 + 0.47,
    74: 0.39 + 0.46,
    75: 0.38 + 0.45,
    76: 0.40 + 0.46,
    77: 0.27 + 0.33,
    78: 0.26 + 0.32,
    79: 0.24 + 0.30,
    80: 0.24 + 0.30,
    81: 0.20 + 0.26,
    82: 0.17 + 0.23,
    83: 0.15 + 0.21,
    84: 0.13 + 0.19,
    85: 0.12 + 0.17,
    86: 0.10 + 0.15,
    87: 0.09 + 0.14,
    88: 0.08 + 0.12,
    89: 0.06 + 0.10,
    90: 0.05 + 0.09,
    91: 0.04 + 0.08,
    92: 0.04 + 0.07,
    93: 0.03 + 0.06,
    94: 0.02 + 0.05,
    95: 0.02 + 0.04,
    96: 0.01 + 0.03,
    97: 0.01 + 0.02,
    98: 0.01 + 0.02,
    99: 0.00 + 0.01,
    100: 0.01 + 0.02
}

# Convert age distribution to a cumulative distribution
ages = list(age_distribution.keys())
percentages = list(age_distribution.values())
cumulative_probs = np.cumsum(percentages)
cumulative_probs = np.append(0, cumulative_probs)  # Add 0 for the starting point


# Function to sample an age based on the combined percentages
def sample_age():
    rand_val = np.random.rand() * cumulative_probs[-1]  # Use the total cumulative percentage
    age_index = np.searchsorted(cumulative_probs, rand_val, side='right') - 1

    # Handle edge case where age_index might be out of range
    if age_index < 0:
        age_index = 0
    elif age_index >= len(ages):
        age_index = len(ages) - 1

    return ages[age_index]


def generate_income(age):
    if age <= 24:
        base_income = 60000 + (age - 18) * 2000
    elif 25 <= age <= 34:
        base_income = 70000 + (age - 25) * 3000
    elif 35 <= age <= 44:
        base_income = 130000 + (age - 35) * 2000
    elif 45 <= age <= 54:
        base_income = 90000 + (age - 45) * 2000
    elif 55 <= age <= 64:
        base_income = 70000 + (age - 55) * 1000
    elif 65 <= age <= 74:
        base_income = 60000 + (age - 65) * 1000
    else:
        base_income = 40000 + (age - 75) * 1000

    # Generate random income within the range using normal distribution and round to the nearest 100
    income = base_income + np.random.normal(0, 15000)
    income = round(income / 100) * 100

    # Introduce some outliers
    if np.random.rand() < 0.02:  # 2% chance of being an outlier
        income *= np.random.choice([0.8, 1.5])  # Outliers can be significantly lower or higher

    return max(1000, income)  # Ensure income is not unrealistically low


# Function to generate the number of devices based on age and income
def generate_devices(age, income):
    if income < 40000:
        mean_devices, std_devices = 3.5, 1
    elif income < 60000:
        mean_devices, std_devices = 4.5, 1
    elif income < 80000:
        mean_devices, std_devices = 5.5, 1
    elif income < 100000:
        mean_devices, std_devices = 6.5, 1
    else:
        mean_devices, std_devices = 7.5, 1

    devices = int(np.random.normal(mean_devices, std_devices))

    # Introduce some outliers
    if np.random.rand() < 0.01:  # 5% chance of being an outlier
        devices += np.random.choice([-2, 2, 5])  # Some outliers with unusually high or low number of devices

    return max(1, devices)  # Ensure at least 1 device


# Function to generate budget based on income
def generate_budget(income):
    if income <= 50000:
        budget = '<30'
    elif 50000 < income <= 100000:
        budget = '30-60'
    elif 100000 < income <= 150000:
        budget = '60-100'
    else:
        budget = '>100'

    # Introduce some outliers
    if np.random.rand() < 0.01:  # 5% chance of being an outlier
        budget = np.random.choice(['<30', '30-60', '60-100', '>100'])

    return budget


def generate_speed(budget):
    if budget == '<30':
        # 20% chance for speed to be less than 50 Mbps and multiple of 5 Mbps (for tech excluding fibers)
        if np.random.rand() < 0.2:
            speed = np.random.normal(25, 35)
            rounded_speed = round(speed / 5) * 5
        else:
            speed = np.random.normal(100, 75)
            rounded_speed = round(speed / 50) * 50
        # speed = np.random.normal(150, 75)  # mean 150, adjust std deviation
        # rounded_speed = round(speed / 5) * 5
    elif budget == '30-60':
        # Adjusted standard deviation for 30-60
        speed = np.random.normal(500, 200)  # mean 800, adjust std deviation
        rounded_speed = round(speed / 50) * 50
    elif budget == '60-100':
        # Adjusted standard deviation for 60-100
        speed = np.random.normal(1000, 400)  # mean 1300, adjust std deviation
        rounded_speed = round(speed / 100) * 100
    else:
        # Adjusted standard deviation for >100
        speed = np.random.normal(1500, 500)  # mean 1750, adjust std deviation
        rounded_speed = round(speed / 200) * 200

    # Ensure speed is at least 10 Mbps
    return max(10, rounded_speed)


# Generate 500,000 rows of data
n = 500000

# # Generate ages based on the age distribution
ages = [sample_age() for _ in range(n)]

# Generate incomes based on ages
incomes = [generate_income(age) for age in ages]

# Generate number of devices based on ages and incomes
devices = [generate_devices(age, income) for age, income in zip(ages, incomes)]

# Create a DataFrame
data = pd.DataFrame({
    'Age': ages,
    'Income': incomes,  # Keep income as numeric for calculations
    'Number_of_Devices': devices
})

# Generate budget data based on income
data['Budget'] = data['Income'].apply(generate_budget)

# Generate internet speed data based on budget
data['Current_Internet_Speed'] = data['Budget'].apply(generate_speed)

# Convert 'Income' to numeric if it contains formatting
data['Income'] = pd.to_numeric(data['Income'], errors='coerce')

# Save the data to a CSV file
save_path = 'C:\\Users\\anmol\\Desktop\\Q2\\assignment_R\\Kaggle\\Test with python\\pythonProject1\\'
data.to_csv(save_path + 'New_test.csv', index=False)

# Calculate median, lowest, and highest income
median_income = data['Income'].median()
lowest_income = data['Income'].min()
highest_income = data['Income'].max()

# Print the results
print(f"Median Income: ${median_income:,.2f}")
print(f"Lowest Income: ${lowest_income:,.2f}")
print(f"Highest Income: ${highest_income:,.2f}")

# Optional: Preview the first 5 rows of the DataFrame
print(data.head(5))
