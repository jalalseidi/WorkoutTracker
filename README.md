# Workout Tracker

This Python script integrates the [Nutritionix API](https://www.nutritionix.com/) and [Sheety API](https://sheety.co/) to track workout data, store it in Google Sheets, and monitor fitness progress.

## 🚀 Features

- Uses **Natural Language Processing (NLP)** to interpret exercise descriptions.
- Fetches exercise details such as **calories burned**, **duration**, and **exercise type** from the Nutritionix API.
- Logs workout data into Google Sheets using Sheety API.
- Automates tracking without the need for manual entry.

## 🛠 Setup

### 1️⃣ Prerequisites

- Python 3.x installed
- `requests` library (install it using `pip install requests`)
- Nutritionix API credentials (App ID & API Key)
- Sheety API access for Google Sheets integration

### 2️⃣ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/workout-tracker.git
   cd workout-tracker
   ```
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Update API credentials in the script:
   ```python
   APP_ID = "your_nutritionix_app_id"
   API_KEY = "your_nutritionix_api_key"
   BEARER_TOKEN = "your_sheety_bearer_token"
   SHEETY_URL = "your_sheety_api_endpoint"
   ```

## 🔧 Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. Enter the exercises you performed when prompted.
3. The script will:
   - Fetch details from the Nutritionix API.
   - Log them in Google Sheets via Sheety API.
   - Display the logged data in the terminal.

## 📌 API Endpoints Used

- **Nutritionix API** (to get exercise details)
  - `POST /v2/natural/exercise`
- **Sheety API** (to store data in Google Sheets)
  - `POST /{sheety_project_id}/workouts`

## 🎯 Future Enhancements

- Add an authentication system for multiple users.
- Implement a graphical user interface (GUI).
- Automate logging using a scheduled task.

## 📜 License

This project is open-source and available under the MIT License.

