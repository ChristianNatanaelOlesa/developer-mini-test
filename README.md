# Developer Mini Test

This repository contains my solution for the **Developer Recruitment Mini Test**.

The project consists of two programming tasks:

1. Small Program
2. Jakarta Weather Forecast

---

## Tech Stack

- Python 3.10+
- Requests
- Python Dotenv
- OpenWeatherMap API

---

## Project Structure

```text
mini-test/
│
├── small_program.py
├── weather_forecast.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Requirements

Before running the project, make sure you have:

- Python 3.10 or later
- An OpenWeatherMap API key

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd mini-test
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

For macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

The weather forecast task requires an OpenWeatherMap API key.

The API key is intentionally **not included in the source code or repository**.

### 1. Create a `.env` file

Create a file named `.env` in the project root:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

### 2. Environment Variable Example

The repository includes `.env.example`:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Copy the example file and replace the value with your own API key.

> The actual `.env` file is excluded from Git using `.gitignore` to prevent exposing the API key.

---

# Test 1 - Small Program

## Description

Create an array/list containing numbers from 1 to 100 and print the numbers in reverse order.

The program follows these rules:

- Prime numbers are not printed.
- Numbers divisible by 3 are replaced with `Foo`.
- Numbers divisible by 5 are replaced with `Bar`.
- Numbers divisible by both 3 and 5 are replaced with `FooBar`.
- The output is printed horizontally.

## Run

```bash
python small_program.py
```

## Implementation

The program uses:

- A prime number checking function.
- A separate function to process each number.
- A loop that iterates from 100 down to 1.
- A list to collect the processed results before printing them horizontally.

The `FooBar` condition is evaluated before the individual `Foo` and `Bar` conditions so that numbers divisible by both 3 and 5 are handled correctly.

---

# Test 2 - Jakarta Weather Forecast

## Description

This program retrieves weather forecast data for Jakarta using the OpenWeatherMap API.

The requirements are:

- Display the weather forecast for Jakarta.
- Display the forecast for the next 5 days.
- Show only one temperature per day.
- Do not expose the API key in the source code.

## Run

```bash
python weather_forecast.py
```

## API

The application uses the OpenWeatherMap 5-day / 3-hour forecast endpoint:

```text
https://api.openweathermap.org/data/2.5/forecast
```

The API key is loaded from the `OPENWEATHER_API_KEY` environment variable.

Example request parameters:

```text
q=Jakarta,ID
appid=<API_KEY>
units=metric
```

---

## Temperature Selection

The OpenWeatherMap forecast API provides multiple forecast points throughout each day.

To satisfy the requirement of displaying only one temperature per day, this implementation selects the forecast point **closest to 12:00 PM local time** for each day.

This provides a consistent rule for selecting a single temperature from the available forecast data.

---

## Example Output

```text
Jakarta Weather Forecast - Next 5 Days
--------------------------------------------------
2026-08-14 | 32.2°C | Broken Clouds
2026-08-15 | 35.9°C | Clear Sky
2026-08-16 | 32.7°C | Broken Clouds
2026-08-17 | 32.8°C | Broken Clouds
2026-08-18 | 31.6°C | Overcast Clouds
```

> The actual weather conditions and temperatures will vary depending on the latest data returned by the OpenWeatherMap API.

---

## Error Handling

The weather application handles several possible errors:

### Missing API Key

If `OPENWEATHER_API_KEY` is not configured:

```text
Configuration error: OPENWEATHER_API_KEY is not configured.
```

### HTTP/API Error

If the API request fails:

```text
HTTP Error: ...
Response: ...
```

### Network Error

If the API cannot be reached:

```text
Failed to retrieve weather data: ...
```

---

## Security

The OpenWeatherMap API key is stored in an environment variable instead of being hard-coded in the source code.

The `.env` file is excluded from Git through `.gitignore`.

The repository only contains `.env.example` as a template:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

This prevents accidentally exposing credentials in the public repository.

---

## Dependencies

The project uses the following Python packages:

### Requests

Used to send HTTP requests to the OpenWeatherMap API.

### Python Dotenv

Used to load environment variables from the `.env` file.

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## Notes

Both mini test tasks are implemented as independent Python programs and can be executed separately.

### Small Program

```bash
python small_program.py
```

### Weather Forecast

```bash
python weather_forecast.py
```

No API key is required for the Small Program.

The Weather Forecast task requires a valid OpenWeatherMap API key configured through the `.env` file.

---

## Author

**Christian Natanael Olesa**

Developer Candidate - Stamps Recruitment Process
