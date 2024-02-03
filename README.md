
# Voice-Activated Assistant with OpenAI

This project is a voice-activated assistant named "Frankie" that uses OpenAI's GPT model for generating responses to spoken queries. It utilizes Google's Web Speech API for speech recognition and the `pyttsx3` library for offline text-to-speech conversion.

## Prerequisites

Before running the assistant, ensure you have the following:

- Python 3.6 or newer installed on your system.
- An OpenAI API key. You can obtain one by signing up at [OpenAI](https://openai.com/).

## Setup

1. **Clone the Repository**  
   Clone this repository to your local machine or download the source code.

2. **Create a Virtual Environment**  
   Navigate to the project directory and create a virtual environment:
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - On Windows: `.env\Scriptsctivate`
   - On macOS/Linux: `source venv/bin/activate`

3. **Install Dependencies**  
   Install the required Python libraries using pip:
   ```bash
   pip install openai pyttsx3 SpeechRecognition
   ```

4. **Set Up Your OpenAI API Key**  
   For security reasons, it's best to set your OpenAI API key as an environment variable.  
   - On Windows (in Command Prompt):
     ```cmd
     setx OPENAI_API_KEY "Your-OpenAI-API-Key"
     ```
   - On macOS/Linux (in bash):
     ```bash
     echo 'export OPENAI_API_KEY="Your-OpenAI-API-Key"' >> ~/.bash_profile
     source ~/.bash_profile
     ```
   Replace `Your-OpenAI-API-Key` with your actual OpenAI API key.

## Running the Program

To run the assistant, activate your virtual environment if it's not already activated, then execute the main Python script:

```bash
python main.py
```

Upon running, the program will instruct you to say "Hey Frankie" to start recording your question, or "Exit" to quit. The assistant will process your spoken question, generate a response using the OpenAI API, and speak the response back to you.

## Troubleshooting

- **Microphone Access**: Ensure your system has microphone access enabled for Python or the terminal you're using.
- **API Key**: If the program exits with a message about the OpenAI API key not being found, double-check that your environment variable is correctly set.
- **Dependencies**: Make sure all dependencies were installed successfully without errors. Some libraries may require additional system dependencies.

## Contributing

Contributions to the project are welcome! Please feel free to fork the repository, make changes, and submit pull requests.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
