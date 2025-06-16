import speech_recognition as sr
import pyttsx3
import datetime
import sys
import wikipediaapi
import requests
import json
import threading
import time
import random
import subprocess

# Initialize the text-to-speech engine
engine = pyttsx3.init()
# Try to set an English voice (depends on system voices)
voices = engine.getProperty('voices')
for voice in voices:
    if "english" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break
else:
    print("Warning: No English voice found, using default voice.")

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initial configuration
CONFIG_FILE = "asistente_config.json"
OPENWEATHER_API_KEY = "TU_CLAVE_API_AQUÍ"  # Replace with your OpenWeatherMap API key
wikipedia = wikipediaapi.Wikipedia(
    user_agent='MyVirtualAssistant/1.0 (joelacosta712@gmail.com)',
    language='en'
)

# Varied greeting responses
GREETINGS = {
    "morning": ["Good morning!", "Great start to the day!", "Hello, ready for the morning?"],
    "afternoon": ["Good afternoon!", "Hey, how's your afternoon?", "Enjoying the day?"],
    "night": ["Good evening!", "Hello, ready for a night adventure?", "Hey, what's up tonight?"]
}

def load_config():
    """Load user preferences from a JSON file."""
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"language": "en", "weather_city": "New York"}

def save_config(config):
    """Save user preferences to a JSON file."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def speak(text):
    """Function for the assistant to speak."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def get_time():
    """Returns the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return f"It's {current_time}."

def search_wikipedia(query):
    """Search for information on Wikipedia."""
    page = wikipedia.page(query)
    if page.exists():
        return page.summary[:200] + "... (more on Wikipedia)"
    return f"I couldn't find information about '{query}' on Wikipedia."

def get_weather(city):
    """Query the weather using the OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&lang=en&units=metric"
    try:
        response = requests.get(url, timeout=5).json()
        if response.get("main"):
            temp = response["main"]["temp"]
            desc = response["weather"][0]["description"]
            return f"In {city}, it's {temp}°C with {desc}."
        return f"I couldn't get the weather for {city}."
    except requests.RequestException:
        return "Error fetching the weather."

def set_reminder(message, seconds):
    """Set a reminder in a separate thread."""
    def execute_reminder():
        time.sleep(seconds)
        speak(f"Reminder: {message}")
    threading.Thread(target=execute_reminder, daemon=True).start()
    return f"Reminder set for {seconds} seconds from now."

def open_app(app):
    """Open an application (Windows by default)."""
    try:
        # For Windows
        subprocess.run(["start", "", app], shell=True, check=True)
        return f"Opening {app}."
    except subprocess.CalledProcessError:
        return f"I couldn't open {app}."

def get_greeting():
    """Return a greeting based on the time of day."""
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        return random.choice(GREETINGS["morning"])
    elif 12 <= hour < 18:
        return random.choice(GREETINGS["afternoon"])
    else:
        return random.choice(GREETINGS["night"])

def process_command(command, config):
    """Process user commands."""
    command = command.lower().strip()
    
    if "hello" in command or "good morning" in command:
        return get_greeting()
    elif "time" in command:
        return get_time()
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            # Run search in a thread to avoid blocking
            def search_task():
                result = search_wikipedia(query)
                speak(result)
            threading.Thread(target=search_task, daemon=True).start()
            return "Searching on Wikipedia..."
        return "Please tell me what to search for."
    elif "weather" in command:
        city = command.replace("weather", "").strip() or config["weather_city"]
        return get_weather(city)
    elif "reminder" in command:
        try:
            parts = command.split("in")
            message = parts[0].replace("reminder", "").strip()
            seconds = int(parts[1].strip().split()[0])  # Example: "in 10 seconds"
            return set_reminder(message, seconds)
        except (IndexError, ValueError):
            return "Incorrect format. Use: 'reminder [message] in [seconds] seconds'."
    elif "open" in command:
        app = command.replace("open", "").strip()
        if app:
            return open_app(app)
        return "Please tell me which app to open."
    elif "exit" in command:
        return "Goodbye! See you soon."
    else:
        return "I didn't understand the command. Try 'hello', 'time', 'search [something]', 'weather [city]', 'reminder [message] in [seconds] seconds', 'open [app]', or 'exit'."

def listen(max_attempts=3):
    """Listen for a voice command with retries."""
    for _ in range(max_attempts):
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio, language="en-US")
                print(f"You: {command}")
                return command
            except sr.UnknownValueError:
                speak("I didn't understand, please try again.")
            except sr.RequestError:
                speak("Connection error, retrying...")
            except sr.WaitTimeoutError:
                speak("I didn't hear anything, please try again.")
    return "Too many failed attempts."

def main():
    """Main function of the assistant."""
    config = load_config()
    speak(f"{get_greeting()} I'm your virtual assistant. Say 'hello', 'time', 'search [something]', 'weather [city]', 'reminder [message] in [seconds] seconds', 'open [app]', or 'exit'.")
    
    while True:
        # Uncomment to use voice input
        # command = listen()
        
        # Text input (comment out if using voice)
        command = input("You: ")
        
        response = process_command(command, config)
        speak(response)
        
        if "exit" in command.lower():
            save_config(config)
            sys.exit()

if __name__ == "__main__":
    main()
    