import speech_recognition as sr

def main():
    # Create a recognizer object
    r = sr.Recognizer()

    # Open the microphone as a source for audio input
    with sr.Microphone() as source:
        # Set a pause threshold for recognizing speech (1 second)
        r.pause_threshold = 1

        # Record audio from the microphone
        audio = r.listen(source)

        # Use Google's speech recognition API to convert audio to text (language set to 'en-pk')
        query = r.recognize_google(audio, language='en-pk')

        # Print the recognized text to the console
        print(f'User said: {query}')

    # Open a file named 'text.txt' and write the recognized text to it
    with open('text.txt', 'w') as f:
        f.write(query)

    # Return the recognized text
    return query

# Call the main function to start speech recognition
main()
