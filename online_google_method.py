import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
from contextlib import suppress

color="\033[1;32m"

lines = "________________________"


def transcribe_audio_file(path: str) -> str:
    """
    Transcribe the audio file located at `path` into text.

    Args:
        path (str): The path to the audio file.

    Returns:
        str: The transcribed text.
    """
    # Create a speech recognition object.
    recognizer = sr.Recognizer()

    # Open the audio file using pydub.
    sound = AudioSegment.from_file(path)

    # Split audio sound where silence is 500 milliseconds or more.
    chunks = split_on_silence(sound,
                              min_silence_len=500,
                              silence_thresh=sound.dBFS - 14,
                              keep_silence=500)

    # Create a directory to store the audio chunks.
    folder_name = "audio-chunks"
    os.makedirs(folder_name, exist_ok=True)

    # Transcribe each chunk and append the text to `whole_text`.
    whole_text = ""
    for i, chunk in enumerate(chunks, start=1):
        # Export the chunk and save it to the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        chunk.export(chunk_filename, format="wav")

        # Recognize the chunk and append the text to `whole_text`.
        with sr.AudioFile(chunk_filename) as source:
            audio = recognizer.record(source)
            try:
                print("Extracting text..")
                text = recognizer.recognize_google(audio)
                print(text)
            except sr.UnknownValueError:
                pass
            else:
                whole_text += f"{text.capitalize()}. "

        # Remove the chunk file.
        with suppress(FileNotFoundError):
            os.remove(chunk_filename)

    # Remove the audio chunks folder.
    with suppress(OSError):
        os.rmdir(folder_name)

    return whole_text.strip()


def online_file_option():
    # Prompt the user to enter the path to the audio file.
    path = input("Enter path to audio file: ")
    # Transcribe the audio file.
    print("Transcribing audio file...")
    text = transcribe_audio_file(path)
    print(f"{color}\n{lines}\n\nTranscription complete. Extracted text: \"{text}\"\n{lines}")

    # Save the transcribed text to a file.
    with open("extracted_text.txt", "w") as f:
        f.write(text)

    print("Transcribed text saved to extracted_text.txt")


def online_speech_to_text_option():
    # initialize the recognizer
    r = sr.Recognizer()

    # set the path of the PocketSphinx speech recognition model files

    # set the path of the audio file to be recognized

    # open the audio file
    with sr.Microphone() as source:
        # record audio data from the source
        print("Please wait. Calibrating microphone...")
        # listen for 5 seconds and create the ambient noise energy level
        r.adjust_for_ambient_noise(source, duration=5)
        print("Say something!")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(f"\n{lines}\n\nTranscription complete. Extracted text: \"{text}\"\n{lines}")
            with open("extracted_text.txt", "w") as f:
                f.write(text)
                print("Transcribed text saved to extracted_text.txt")
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print("Error: " + str(e))
