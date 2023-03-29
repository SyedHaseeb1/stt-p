import speech_recognition as sr

lines = "________________________"
color="\033[1;32m"


def offline_file_option():
    # initialize the recognizer
    r = sr.Recognizer()

    # set the path of the audio file to be recognized
    audio_path = input(f"{color}Enter audio file path: ")

    # open the audio file
    with sr.AudioFile(audio_path) as source:
        # record audio data from the source
        print("Transcribing audio file...")
        audio_data = r.record(source)
        # recognize speech using PocketSphinx
        try:
            text = r.recognize_sphinx(audio_data, language='en-US')
            print(f"{color}\n{lines}\n\nTranscription complete. Extracted text: \"{text}\"\n{lines}")
            with open("extracted_text.txt", "w") as f:
                f.write(text)
                print("Transcribed text saved to extracted_text.txt")
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print("Error: " + str(e))
