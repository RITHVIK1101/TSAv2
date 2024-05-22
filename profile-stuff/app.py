from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('recommendation_model.pkl')

# Define explanations for different energy recommendations
explanations = {
    'Solar': 'Solar energy is recommended due to your high usage of electrical appliances during the day.',
    'Wind': 'Wind energy is suitable because of your consistent energy consumption throughout the day.',
    'Biomass': 'Biomass energy is recommended because it matches well with your diverse energy needs.'
}

@app.route('/api/get_recommendation', methods=['POST'])
def get_recommendation():
    data = request.json

    # Extract the necessary data from the request
    country = data.get('country')
    state = data.get('state')
    tvHours = data.get('tvHours')
    phoneHours = data.get('phoneHours')
    fridge = data.get('fridge')
    washer = data.get('washer')
    dryer = data.get('dryer')
    kitchenHours = data.get('kitchenHours')
    carType = data.get('carType')
    carMiles = data.get('carMiles')

    # Prepare the input data for the recommendation model
    input_data = [tvHours, phoneHours, fridge, washer]

    # Get the recommendation from the model
    recommendation = model.predict([input_data])[0]

    # Enhance the recommendation based on location and other factors
    enhanced_recommendation = enhance_recommendation(recommendation, country, state)

    # Get the explanation for the recommendation
    explanation = explanations.get(enhanced_recommendation, 'No specific explanation available.')

    return jsonify({'recommendation': enhanced_recommendation, 'explanation': explanation})
def enhance_recommendation(recommendation, country, state):
    # Enhance the recommendation based on location and other factors
    if recommendation == 'Solar':
        if country in ['US', 'AU']:
            # Assume US and Australia have generally sunny weather
            return 'Solar'
        else:
            # For other countries, consider wind or biomass
            return 'Wind'
    elif recommendation == 'Wind':
        if country in ['CA', 'GB', 'DE']:
            # Assume these countries have generally windy weather
            return 'Wind'
        else:
            # For other countries, consider solar or biomass
            return 'Solar'
    else:
        # For other recommendations, consider biomass as a versatile option
        return 'Biomass'
if __name__ == '__main__':
    app.run(debug=True, port=5001)
