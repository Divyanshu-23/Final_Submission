import requests

# Replace with your actual WeatherAPI key
API_KEY = "915897ce445c4c35b91181741252202"
LOCATION = input("Enter the region to get the forecast")
CROP = input("Which crop do you want to plan for ?")

URL = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={LOCATION}&days=10&aqi=no&alerts=yes"


def get_crop_advice(day, crop):
    """Provide crop-specific farming advice based on weather conditions."""
    condition = day["day"]["condition"]["text"]
    max_temp = day["day"]["maxtemp_c"]
    min_temp = day["day"]["mintemp_c"]
    avg_humidity = day["day"]["avghumidity"]
    wind_speed = day["day"]["maxwind_kph"]
    rainfall = day["day"]["totalprecip_mm"]

    advice = []

    if crop.lower() == "tomato":
        if max_temp > 35:
            advice.append("⚠️ High heat stress! Irrigate and provide shade.")
        if min_temp < 10:
            advice.append("❄️ Cold stress risk! Protect young plants from frost.")
        if rainfall > 20:
            advice.append("🌧️ Excessive rain! Risk of fungal diseases (blight, mildew). Improve drainage.")
        if avg_humidity > 80:
            advice.append("💦 High humidity! Spray fungicides to prevent mildew.")
        if wind_speed > 40:
            advice.append("💨 Strong winds! Support weak stems to prevent damage.")

    elif crop.lower() == "maize":
        if max_temp > 35:
            advice.append("🔥 High heat reduces pollination. Apply mulch to conserve soil moisture.")
        if rainfall < 5:
            advice.append("🌞 Dry spell! Irrigate if possible to prevent yield loss.")
        if wind_speed > 50:
            advice.append("💨 Strong winds! Risk of lodging (falling plants). Use windbreaks.")
        if avg_humidity > 80:
            advice.append("💦 High humidity! Risk of fungal diseases like rust and blight.")

    elif crop.lower() == "cassava":
        if min_temp < 10:
            advice.append("❄️ Cold temperatures slow growth. Expect delayed tuber development.")
        if rainfall < 10:
            advice.append("🌞 Dry conditions! Mulch to retain soil moisture.")
        if rainfall > 50:
            advice.append("🌧️ Heavy rain! Risk of root rot. Improve drainage.")
        if wind_speed > 60:
            advice.append("💨 Strong winds! May uproot plants. Provide wind protection.")

    elif crop.lower() == "cashew":
        if max_temp > 35:
            advice.append("🔥 High temperatures reduce nut setting. Irrigate young trees.")
        if rainfall > 30:
            advice.append("🌧️ Excess rain can affect flowering and fruit setting.")
        if wind_speed > 50:
            advice.append("💨 Strong winds! Risk of flower drop. Provide windbreaks.")
        if avg_humidity > 85:
            advice.append("💦 High humidity! Risk of fungal infections on nuts.")

    return advice


def get_weather_forecast():
    """Fetch 10-day weather forecast and provide crop-specific farming advice."""
    try:
        response = requests.get(URL)
        data = response.json()

        if "forecast" in data:
            print(f"🌾 10-Day {CROP} Farming Forecast for {data['location']['name']}, {data['location']['country']}:\n")
            for day in data["forecast"]["forecastday"]:
                date = day["date"]
                condition = day["day"]["condition"]["text"]
                max_temp = day["day"]["maxtemp_c"]
                min_temp = day["day"]["mintemp_c"]
                avg_humidity = day["day"]["avghumidity"]
                wind_speed = day["day"]["maxwind_kph"]
                rainfall = day["day"]["totalprecip_mm"]

                print(f"📅 {date}: {condition}")
                print(f"   🌡️ Max Temp: {max_temp}°C, Min Temp: {min_temp}°C")
                print(f"   💧 Humidity: {avg_humidity}%, 🌬️ Wind Speed: {wind_speed} kph")
                print(f"   🌧️ Rainfall: {rainfall} mm")

                advice = get_crop_advice(day, CROP)
                if advice:
                    print("   🚜 Farming Advice:")
                    for tip in advice:
                        print(f"     - {tip}")

                print("\n" + "-" * 50 + "\n")
        else:
            print("Error fetching forecast:", data.get("error", {}).get("message", "Unknown error"))

    except Exception as e:
        print("An error occurred:", e)


# Call the function
get_weather_forecast()
