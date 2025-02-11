from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEATHERSTACK_API_KEY = "YOUR_API_KEY"
WEATHERSTACK_API_URL = "http://api.weatherstack.com/current"

WEATHERSTACK_API_URL = "http://api.weatherstack.com/current"

@app.route("/get_weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City not provided"}), 400

    params = {
        "access_key": WEATHERSTACK_API_KEY,
        "query": city
    }

    response = requests.get(WEATHERSTACK_API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if "current" in data:
            weather = f"{data['current']['weather_descriptions'][0]}, {data['current']['temperature']}°C"
            return jsonify(weather)
        else:
            return jsonify({"error": "Invalid city or API issue"}), 500
    else:
        return jsonify({"error": "Failed to fetch weather data"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
