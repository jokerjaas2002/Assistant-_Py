# Assistant-_Py
Virtual Assistant
A Python-based virtual assistant that responds to text or voice commands, providing functionalities like telling the time, searching Wikipedia, checking the weather, setting reminders, and opening applications. The assistant supports English and is designed to run on Windows, with extensibility for other platforms.
Features

Greetings: Responds with time-based greetings (e.g., "Good morning!" or "Good evening!").
Time: Tells the current time in 12-hour format (e.g., "It's 9:25 AM").
Wikipedia Search: Searches Wikipedia for information on a given topic.
Weather: Retrieves weather information for a specified city using the OpenWeatherMap API.
Reminders: Sets timed reminders that trigger after a specified number of seconds.
Open Applications: Opens applications on Windows (e.g., Notepad).
Voice Input (Optional): Supports voice commands using a microphone.
Persistent Configuration: Saves user preferences (language, default weather city) in a JSON file.
Threaded Operations: Uses threads for non-blocking Wikipedia searches and reminders.

## Prerequisites

Python 3.7 or higher
A working microphone (for voice input)
Internet connection (for Wikipedia and OpenWeatherMap APIs)
An OpenWeatherMap API key

## Installation

Clone or download the repository:Clone this repository from GitHub:
git clone https://github.com/jokerjaas2002/virtual-assistant.git

Or download the Assitant.py file to your project directory (e.g., C:/Users/joel/OneDrive/Escritorio/Asistente Virtual/Assistant-_Py/).

Install dependencies:Install the required Python libraries using pip:
pip install speechrecognition pyttsx3 wikipedia-api requests


Configure the OpenWeatherMap API key:

Sign up at OpenWeatherMap to obtain a free API key.
Open Assitant.py and replace TU_CLAVE_API_AQUÍ with your API key:OPENWEATHER_API_KEY = "your-api-key-here"




## Ensure system requirements:

For voice input, ensure you have a working microphone.
For text-to-speech, ensure your Windows system has English voices installed (e.g., Microsoft David or Zira). If no English voice is found, the default system voice will be used.



## Usage

Run the assistant:Navigate to the project directory and execute the script:
python Assitant.py


## Interact with the assistant:

Text input: Type commands in the console.
Voice input: Uncomment the line command = listen() and comment out command = input("You: ") in the main() function of Assitant.py. Ensure a microphone is connected.


## Available commands:

hello or good morning: Receive a time-based greeting.
time: Get the current time (e.g., "It's 9:25 AM").
search [query]: Search Wikipedia for the specified topic (e.g., search python).
weather [city]: Check the weather for a city (e.g., weather London). Defaults to New York if no city is provided.
reminder [message] in [seconds] seconds: Set a reminder (e.g., reminder Meeting in 10 seconds).
open [app]: Open a Windows application (e.g., open notepad).
exit: Exit the assistant.

## Example interaction:
Assistant: Good morning! I'm your virtual assistant. Say 'hello', 'time', 'search [something]', 'weather [city]', 'reminder [message] in [seconds] seconds', 'open [app]', or 'exit'.
You: time
Assistant: It's 9:25 AM
You: search artificial intelligence
Assistant: Searching on Wikipedia...
Assistant: Artificial intelligence (AI), in its broadest sense, is intelligence exhibited by machines, particularly computer systems. It is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and take actions that maximize their chances of achieving their goals... (more on Wikipedia)
You: exit
Assistant: Goodbye! See you soon.



## Configuration

Preferences: The assistant saves preferences (language and default weather city) in asistente_config.json. The default configuration is:{"language": "en", "weather_city": "New York"}


Voice: The assistant attempts to use an English voice for text-to-speech. If none is available, it falls back to the system's default voice, and a warning is printed.

## Notes

Voice input: Requires a microphone and internet connection (uses Google Speech-to-Text). Uncomment the voice input line in main() to enable it.
Windows compatibility: The open command uses start for Windows. For macOS, modify the open_app function to use subprocess.run(["open", "-a", app]).
OpenWeatherMap API: Ensure your API key is valid. If the weather command fails, check your key or internet connection.
Wikipedia API: The assistant uses a User-Agent (MyVirtualAssistant/1.0 (jokerjaas2002)) as required by Wikimedia's policy.
File path: The script is named Assitant.py. Ensure the file name matches your project structure.

## Troubleshooting

No English voice found: Install additional English voices via Windows settings or use the default voice.
Weather API errors: Verify your OpenWeatherMap API key and internet connection.
Voice recognition errors: Ensure your microphone is working and the environment is not too noisy. Check your internet connection for Google Speech-to-Text.
Wikipedia errors: Ensure the User-Agent is correctly set and your internet connection is stable.

## Future Improvements

Add a graphical user interface (GUI) using Tkinter or PyQt.
Support multiple languages for commands and responses.
Integrate natural language processing (NLP) with libraries like spaCy for better command understanding.
Add more commands, such as sending emails or playing music.

## License
This project is for personal use and learning purposes. Ensure compliance with the OpenWeatherMap API terms and Wikimedia's User-Agent policy.
Contact
For issues or suggestions, contact jokerjaas2002 on GitHub.
  
