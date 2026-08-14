import os
from datetime import datetime
from collections import defaultdict

import requests
from dotenv import load_dotenv


API_URL = "https://api.openweathermap.org/data/2.5/forecast"
CITY = "Jakarta,ID"


def get_weather_forecast():
    load_dotenv()

    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        raise ValueError("OPENWEATHER_API_KEY is not configured.")

    params = {
        "q": CITY,
        "appid": api_key,
        "units": "metric",
    }

    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


def get_daily_forecast(data):
    daily_forecast = defaultdict(list)

    for item in data["list"]:
        date = datetime.fromtimestamp(item["dt"]).date()
        daily_forecast[date].append(item)

    result = []

    for date, forecasts in sorted(daily_forecast.items()):
        if len(result) >= 5:
            break

        # Use the forecast closest to 12:00 PM
        selected = min(
            forecasts,
            key=lambda x: abs(
                datetime.fromtimestamp(x["dt"]).hour - 12
            )
        )

        temperature = selected["main"]["temp"]
        description = selected["weather"][0]["description"]

        result.append({
            "date": date.strftime("%Y-%m-%d"),
            "temperature": temperature,
            "description": description,
        })

    return result


def main():
    try:
        data = get_weather_forecast()
        forecast = get_daily_forecast(data)

        print("Jakarta Weather Forecast - Next 5 Days")
        print("-" * 50)

        for item in forecast:
            print(
                f"{item['date']} | "
                f"{item['temperature']:.1f}°C | "
                f"{item['description'].title()}"
            )

    except requests.HTTPError as error:
        print(f"HTTP Error: {error}")
        print(f"Response: {error.response.text}")

    except requests.RequestException as error:
        print(f"Failed to retrieve weather data: {error}")

    except ValueError as error:
        print(f"Configuration error: {error}")


if __name__ == "__main__":
    main()