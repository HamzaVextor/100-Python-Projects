import speech_recognition as sr

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language='en-pk')
        print(f'User said: {query}')
    with open('text.txt', 'w') as f:
        f.write(query)
    return query

main()
