# VocalGenius - Voice Assistant

## Overview
**VocalGenius** is a Python-based voice assistant that uses speech recognition and text-to-speech functionalities to assist users with various tasks, such as playing games, setting reminders, searching the web, managing to-do lists, and much more. It includes both text and speech command modes, offering flexibility in user interaction.

## Features
- **Speech Recognition**: Recognizes user commands via voice input using the `speech_recognition` library.
- **Text-to-Speech**: Provides spoken responses with a female voice using the `pyttsx3` library.
- **Date and Time**: Provides the current date and time on request.
- **Wikipedia Search**: Fetches and reads summaries from Wikipedia.
- **To-Do List Management**: Add, view, remove, and clear tasks in a to-do list.
- **Game Selection**: Allows the user to play a random game from a set of pre-installed Python games.
- **Music Search**: Opens Spotify and searches for songs by artist and title.
- **Reminders**: Set reminders to notify users of events or tasks at a specified time.
- **Health Tips for Elders**: Provides health-related tips tailored to elderly users.
- **Motivational Quotes**: Delivers a daily motivational quote.
- **Symptom Checker**: Retrieves health information based on symptoms by searching Wikipedia.
- **Calculator**: Performs basic arithmetic calculations based on user input.

## Installation
To run **VocalGenius**, ensure you have Python installed on your system, along with the required libraries:

### Required Libraries:
1. `pyttsx3` (Text-to-Speech)
2. `speech_recognition` (Speech Recognition)
3. `wikipedia` (Wikipedia API)
4. `webbrowser` (Open web pages)
5. `random` (Random selection)
6. `subprocess` (Run external Python scripts)
7. `datetime` (Date and Time operations)
8. `re` (Regular expressions for parsing calculations)
9. `threading.Timer` (For scheduling reminders)

Install the dependencies via pip:
```bash
pip install pyttsx3 SpeechRecognition wikipedia
```

## Usage

1. **Run the Script**:
   Simply execute the Python script.
   ```bash
   python vocalgenius.py
   ```

2. **Choose Mode**:
   Upon startup, **VocalGenius** will ask if you prefer text or speech commands. 
   - **Text mode**: Type your commands in the console.
   - **Speech mode**: Speak commands, and the assistant will recognize them.

3. **Supported Commands**:
   - **Time**: "What is the time?"
   - **Date**: "What is today's date?"
   - **Wikipedia Search**: "Search [topic] on Wikipedia."
   - **Open Website**: "Open YouTube" or "Open Google."
   - **Play Game**: "Play a game."
   - **Set Reminder**: "Set a reminder for [HH:MM]."
   - **Play Music**: "Play [song] by [artist]."
   - **Check Symptoms**: "Check symptoms for [symptom]."
   - **Motivation**: "Give me today's motivation."
   - **Calculator**: "Calculate [expression]."
   - **To-Do List**:
     - "Add a task [task]."
     - "View tasks."
     - "Remove task [task number]."
     - "Clear tasks."
   - **Health Tips for Elders**: "Give me a health tip."

4. **Exit**:
   - Say or type "Exit" to quit the assistant.

## Example Usage

**In Text Mode**:
```
Type your command: What is the time?
The time is 03:45 PM
```

**In Speech Mode**:
```
Listening...
Recognizing...
User said: What is the time?
The time is 03:45 PM
```


## License
This project is open-source and available for modifications and contributions.
 

