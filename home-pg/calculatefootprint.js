function calculateCarbonFootprint() {
  // Get selected values
  var transportation = document.getElementById('transportation').value;
  var electricity = document.getElementById('electricity').value;
  var heatUsage = document.getElementById('heatUsage').value;
  var meatConsumption = document.getElementById('meatConsumption').value;

  // Placeholder values for carbon emissions (in kilograms) per year
  var carbonEmissions = {
    walk: 0,
    car: 2000,
    bus: 1500,
    train: 500,
    bike: 0,
    low: 1000,
    medium: 2000,
    high: 3000
  };

  // Calculate total carbon footprint
  var totalCarbonFootprint = carbonEmissions[transportation] + carbonEmissions[electricity] + carbonEmissions[heatUsage] + carbonEmissions[meatConsumption];

  // Display result
  var resultElement = document.getElementById('result');
  resultElement.innerHTML = "<p>Your estimated carbon footprint per year is: " + totalCarbonFootprint + " kilograms</p>";

  // Provide suggestions for high electricity and heat usage
  if (electricity === 'high') {
      resultElement.innerHTML += "<p>You have high electricity usage. Consider using solar or wind energy to reduce your carbon footprint.</p>";
  }
  if (heatUsage === 'high') {
      resultElement.innerHTML += "<p>You have high heat usage. Consider using heat pumps or biomass heaters to reduce your carbon footprint.</p>";
  }
}
