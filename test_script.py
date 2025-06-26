import speech_recognition as sr
import pyttsx3
import webbrowser
import smtplib
import schedule
import time

# Test speech recognition
def test_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source, timeout=5)
        try:
            text = recognizer.recognize_sphinx(audio)  # Use Sphinx instead of Google
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")

# Test text-to-speech
def test_tts():
    engine = pyttsx3.init()
    engine.say("Hello, your Python environment is set up correctly!")
    engine.runAndWait()

# Test webbrowser
def test_browser():
    webbrowser.open("https://www.python.org")
    print("Opened Python website in browser.")

# Test smtplib (simulated)
def test_email():
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        print("SMTP connection simulated successfully.")
    except Exception as e:
        print(f"SMTP simulation failed: {e}")

# Test schedule
def test_schedule():
    def job():
        print("Scheduled task executed!")
    schedule.every(5).seconds.do(job)
    print("Running scheduler for 10 seconds...")
    for _ in range(2):
        schedule.run_pending()
        time.sleep(5)

# Run all tests
if __name__ == "__main__":
    print("Testing libraries...")
    test_tts()
    test_browser()
    test_email()
    test_schedule()
    test_speech()  # Speak into your microphone when prompted