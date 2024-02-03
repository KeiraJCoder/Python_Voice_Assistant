# Import necessary libraries
import openai  # Used for accessing the OpenAI GPT models via the API.
import pyttsx3  # Text-to-speech library for Python, works offline.
import speech_recognition as sr  # For speech recognition to transcribe audio to text.
import os  # To access environment variables for secure API key storage.
import sys  # Used for system-specific functions, like exiting the program.

# Attempt to securely retrieve the OpenAI API Key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is available, exit if not to ensure API access is secured
if not openai.api_key:
    print("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    sys.exit(1)  # Exits the program if the API key is not set.

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to transcribe audio file content to text using Google's Web Speech API
def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()  # Initialize the recognizer
    with sr.AudioFile(filename) as source:  # Open the audio file
        audio = recognizer.record(source)  # Record the audio from the file
    try:
        # Attempt to recognize the speech in the audio file
        return recognizer.recognize_google(audio)
    except Exception as e:
        # Print any error that occurs during transcription and return None
        print(f'Error in transcribing audio: {e}')
        return None

# Function to generate a response from OpenAI based on the input prompt
def generate_response(prompt):
    try:
        # Use the OpenAI API to generate a chat completion response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the model to use
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        # Return the text content of the response
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        # Print any error that occurs during response generation
        print(f'Error in generating response: {e}')
        return "I'm sorry, I couldn't generate a response."

# Function to use the text-to-speech engine to speak out the response
def speak_text(text):
    engine.say(text)  # Queue the text for speech
    engine.runAndWait()  # Process the speech queue and wait for completion

# Main function to run the assistant
def main():
    while True:  # Continuous loop to process voice commands
        print("Say 'Hey Frankie' to start recording your question, or 'Exit' to quit.")
        with sr.Microphone() as source:  # Use the default microphone as the audio source
            recognizer = sr.Recognizer()  # Initialize the recognizer
            audio = recognizer.listen(source)  # Listen for the first phrase and extract it into audio data
            try:
                # Recognize speech using Google's Web Speech API
                transcription = recognizer.recognize_google(audio)
                # Check for the exit command to break the loop
                if transcription.lower() == "exit":
                    print("Exiting program.")
                    break
                # Activation phrase to proceed with capturing a question
                elif transcription.lower() == "hey frankie":
                    filename = 'input.wav'  # Temporary file to store audio
                    print("Say your question....")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1  # Optional: Adjust pause threshold
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)  # Listen again for the question
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())  # Save the question audio to a file

                    # Transcribe the audio file to text
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print(f"You said: {text}")  # Echo the transcribed text
                        response = generate_response(text)  # Generate a response using the OpenAI API
                        print(f"Frankie says: {response}")  # Print the response
                        speak_text(response)  # Speak out the response
            except Exception as e:
                print(f"An error occurred: {e}")  # Print any errors during the process

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly
