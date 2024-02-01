
# Speech Recognition and Response Project

This project utilizes speech recognition to transcribe audio input from the user, generates a response using OpenAI's GPT model, and reads the response back to the user using text-to-speech.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Windows 10 or later
- Python 3.8 or newer installed

## Installation

Follow these steps to set up the project environment on Windows:

### 1. Clone the Repository

Clone the project repository to your local machine using Git:

```
git clone [repository-url]
cd [local-repository]
```

Replace `[repository-url]` with the URL of the project's repository and `[local-repository]` with the name of the folder where you cloned the project.

### 2. Create a Virtual Environment

Open a command prompt in the project directory and run:

```
python -m venv venv
```

Activate the virtual environment:

```
.\venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```
pip install openai pyttsx3 SpeechRecognition PyAudio
```

#### Installing PyAudio

If you encounter any issues installing PyAudio with pip, you may need to install a precompiled PyAudio wheel for Windows. Download the appropriate `.whl` file from [Christoph Gohlke's Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it using:

```
pip install path/to/PyAudio-*.whl
```

Replace `path/to/PyAudio-*.whl` with the actual path to the downloaded `.whl` file.

### 4. Set Up OpenAI API Key

1. Obtain an API key from [OpenAI](https://openai.com/).
2. Set the API key as an environment variable on your system:

For a temporary setup, in your command prompt, run:

```
set OPENAI_API_KEY=your_api_key_here
```

For a permanent setup, search for "Environment Variables" in Windows search and add `OPENAI_API_KEY` as a new system variable.

Replace `your_api_key_here` with your actual OpenAI API key.

## Running the Program

With the virtual environment activated and the OpenAI API key set, you can run the program by executing:

```
python main.py
```

Ensure your microphone is properly configured and say "Hey Frankie" to activate the recording, followed by your question or command.

## Troubleshooting

- **PyAudio Installation Issues:** Ensure you have the Microsoft Visual C++ Build Tools installed. If PyAudio still fails to install, use the precompiled `.whl` method as described above.
- **Microphone Not Recognized:** Check your system's sound settings to ensure your microphone is set as the default recording device.

## Contributing

Instructions for how contributors can help with your project.

## License

Specify the license under which your project is made available.
