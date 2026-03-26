# 🧠 AERO - AI Voice Assistant

## 📌 Project Overview

AERO is a Python-based AI voice assistant capable of understanding voice commands and performing useful tasks such as searching the web, playing music, retrieving weather information, reading news headlines, telling jokes, and executing system commands.

The assistant uses speech recognition to capture voice input, processes the command using natural language patterns, and responds using text-to-speech technology.

This project demonstrates the integration of speech recognition, natural language processing, API integration, and automation to build an interactive AI system.

## 🎯 Features

AERO supports multiple commands including:

• Voice command recognition
• Wake word detection ("Hey Aero")
• Play music from YouTube
• Wikipedia information search
• Google search
• Weather information retrieval
• News headlines
• Tell jokes
• Open websites
• System commands (shutdown/restart)
• Voice responses using text-to-speech

## ⚙️ Technologies Used

Python
SpeechRecognition
pyttsx3
Wikipedia API
OpenWeatherMap API
NewsAPI
pywhatkit
requests
tkinter
python-dotenv

## 🧠 How It Works

The assistant follows this workflow:

Voice Input → Speech Recognition → Command Processing → Action Execution → Voice Response

The assistant listens for the wake word “Hey Aero”.
The spoken command is converted into text using Google Speech Recognition.
The command is analyzed to determine the intended action.
The assistant executes the requested task.
A response is delivered using a text-to-speech engine.

## 📊 Supported Commands

Examples of commands you can give to AERO:

Hey Aero
What time is it
Play Imagine Dragons
Who is Elon Musk
Open YouTube
Search machine learning
What is the weather
Tell me a joke
Give me the news
Shutdown computer
Restart computer
Stop

## 🚀 Installation

Clone the repository:

git clone https://github.com/SahilSinghG/Aero-Voice-Assistant-using-Deep-Learning.git

Navigate to the project folder:

cd aero-voice-assistant

Install dependencies:

pip install -r requirements.txt

## 🔑 Environment Variables

Create a .env file in the project directory and add your API keys:

WEATHER_API_KEY=openweather_api_key
NEWS_API_KEY=news_api_key

These keys are loaded securely using python-dotenv.

▶️ Run the Assistant

Start the voice assistant using:

python app.py

Say the wake word:

Hey Aero

Then give your command.

## 📂 Project Structure

aero-voice-assistant

│

├── app.py

├── requirements.txt

├── README.md

├── .env

└── .gitignore

## 📌 Skills Demonstrated

This project demonstrates several AI and software development skills:

Speech Recognition
Voice Interaction Systems
API Integration
Python Automation
AI Assistant Development
Secure Environment Variable Management

## 🔮 Future Improvements

Possible enhancements include:

Wake word detection using deep learning
Integration with smart home devices
ChatGPT-based conversational AI
Desktop GUI interface
Mobile app integration

## 👨‍💻 Author

Sahil Singh

Machine Learning & AI Enthusiast

GitHub:
https://github.com/SahilSinghG
