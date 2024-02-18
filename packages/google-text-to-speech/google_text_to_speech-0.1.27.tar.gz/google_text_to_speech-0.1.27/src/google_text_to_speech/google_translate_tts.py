"""Module for converting text to speech using Google Translate TTS."""

import os
import re
import threading
import tempfile
import requests
from playsound import playsound

# Constants
SPLIT_POINTS = [
    ",",
    ";",
    " i ",
    " ali ",
    " ili ",
    " međutim ",
    " zato ",
    " jer ",
    " kao ",
    " dok ",
    " kada ",
]
MAX_LENGTH = 200
TTS_URL = "https://translate.google.com/translate_tts"
AUDIO_SUFFIX = ".mp3"


def generate_url(text, lang):
    """
    Generate the URL for the Google TTS API.

    :param text: Text to be converted to speech.
    :param lang: Language code for the TTS.
    :return: URL string.
    """
    encoded_text = requests.utils.quote(text)
    return f"{TTS_URL}?ie=UTF-8&tl={lang}&client=tw-ob&q={encoded_text}"


def play_and_remove_file(file_path):
    """
    Play an audio file and remove it after playing.

    :param file_path: Path to the audio file.
    """
    try:
        playsound(file_path)
    finally:
        os.remove(file_path)


def split_long_sentence(sentence, max_length=200):
    """
    Split a long sentence into parts, retaining punctuation at the end of each part.

    :param sentence: The sentence to split.
    :param max_length: Maximum length of each part.
    :return: List of sentence parts.
    """
    parts = []
    current_part = ""
    current_length = 0
    words = sentence.split()

    for word in words:
        # Check if adding the next word would exceed the max_length
        if current_length + len(word) + 1 > max_length:
            # Find the last suitable split point in the current part
            last_split_point = max(
                current_part.rfind(split_point) for split_point in SPLIT_POINTS
            )
            if last_split_point > 0:
                # Include the split point in the first part
                split_index = last_split_point + 1
                parts.append(current_part[:split_index].strip())
                current_part = current_part[split_index:].strip() + " "
            else:
                # If no suitable split point, split at the current position
                parts.append(current_part.strip())
                current_part = ""
            current_length = len(current_part)

        current_part += word + " "
        current_length += len(word) + 1

    # Add the final part if it's not empty
    if current_part:
        parts.append(current_part.strip())

    return parts


def split_text(text, max_length=MAX_LENGTH):
    """
    Split text into smaller parts.

    :param text: Text to be split.
    :param max_length: Maximum length of each part.
    :return: List of text parts.
    """
    sentences = re.split(r"(?<=[.!?]) +", text)
    parts = []

    for sentence in sentences:
        if len(sentence) <= max_length:
            parts.append(sentence)
        else:
            parts.extend(split_long_sentence(sentence, max_length))

    return parts


def play_tts(text, lang):
    """
    Play text-to-speech for the given text and language.

    :param text: Text to be converted to speech.
    :param lang: Language code for the TTS.

    Raises:
    requests.RequestException: If there's an issue with the network or fetching the audio.
    IOError: If there's an issue writing the audio file.
    RuntimeError: If other unexpected issues occur.
    """
    parts = split_text(text)

    for part in parts:
        url = generate_url(part, lang)
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with tempfile.NamedTemporaryFile(
                delete=False, suffix=AUDIO_SUFFIX
            ) as audio_file:
                audio_file.write(response.content)
                temp_audio_file = audio_file.name

            play_thread = threading.Thread(
                target=play_and_remove_file, args=(temp_audio_file,)
            )
            play_thread.start()
            play_thread.join()
        except requests.RequestException as e:
            print(f"Error fetching audio: {e}")
        except IOError as e:
            print(f"Error writing audio file: {e}")
        except RuntimeError as e:
            print(f"Unexpected error: {e}")


# Example usage
# play_tts("Your text here", "language_code")
