# model.py
def recommend_energy_source(consumption_data):
    """
    Recommends an energy source based on the user's consumption data and provides an explanation.
    
    Args:
    - consumption_data (dict): User's energy consumption data.
    
    Returns:
    - tuple: (str, str) Recommended energy source and explanation.
    """
    tv_hours = consumption_data.get('tvHours', 0)
    phone_hours = consumption_data.get('phoneHours', 0)
    fridge = consumption_data.get('fridge', False)
    washer = consumption_data.get('washer', 0)
    dryer = consumption_data.get('dryer', 0)
    kitchen_hours = consumption_data.get('kitchenHours', 0)
    car_type = consumption_data.get('carType', 'Gas')
    car_miles = consumption_data.get('carMiles', 0)
    country = consumption_data.get('country', 'US')
    state = consumption_data.get('state', '')

    total_consumption = (
        tv_hours + phone_hours + washer + dryer + kitchen_hours +
        (car_miles * (2 if car_type == 'EV' else 1))
    )
    
    if total_consumption > 20:
        recommendation = "Solar Energy"
        explanation = f"Given your high total energy consumption ({total_consumption} units) and your use of an electric vehicle, solar energy is recommended to maximize efficiency and sustainability, especially in a region like {state}, {country}."
    elif total_consumption > 10:
        recommendation = "Wind Energy"
        explanation = f"With a moderate total energy consumption ({total_consumption} units), wind energy is suitable for your needs. This source will effectively complement your usage patterns in {state}, {country}."
    else:
        recommendation = "Hydropower"
        explanation = f"Your low total energy consumption ({total_consumption} units) makes hydropower a great fit, offering reliable and consistent energy with minimal environmental impact in {state}, {country}."

    return recommendation, explanation

# Test the function with sample data
sample_data = {
    'tvHours': 2,
    'phoneHours': 1,
    'fridge': True,
    'washer': 1,
    'dryer': 1,
    'kitchenHours': 2,
    'carType': 'EV',
    'carMiles': 10,
    'country': 'US',
    'state': 'California'
}

recommendation, explanation = recommend_energy_source(sample_data)
print(recommendation)
print(explanation)
