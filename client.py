from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

SERVER_URL = "http://192.168.100.4:5001/get_weather"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 400px;
            margin: 50px auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }
        input, select, button {
            width: calc(100% - 20px);
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        button {
            background: #28a745;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background: #218838;
        }
        .weather-info {
            margin-top: 20px;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Weather App</h1>
        <form action="/weather" method="post">
            <input type="text" name="city" placeholder="Enter city name" required>
            <select name="unit">
                <option value="m">Metric (°C, km/h)</option>
                <option value="f">Imperial (°F, mph)</option>
            </select>
            <select name="language">
                <option value="en">English</option>
                <option value="es">Spanish</option>
                <option value="fr">French</option>
                <option value="de">German</option>
            </select>
            <button type="submit">Get Weather</button>
        </form>
        {% if weather_data %}
            <div class="weather-info">
                <h3>Weather in {{ city }}</h3>
                <p>{{ weather_data }}</p>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/weather", methods=["POST"])
def get_weather():
    city = request.form.get("city")
    unit = request.form.get("unit", "m")
    language = request.form.get("language", "en")

    params = {"city": city, "unit": unit, "lang": language}
    response = requests.get(SERVER_URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return render_template_string(HTML_TEMPLATE, weather_data=weather_data, city=city)
    else:
        return render_template_string(HTML_TEMPLATE, weather_data="Error fetching weather data", city=city)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

