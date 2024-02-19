import os
import time
import queue
import tempfile
import threading
import subprocess

from TTS.api import TTS
from ai_stream_interact.tts.tts_base import supress_printouts
from ai_stream_interact.tts.coqui_ai import TextToSpeechCoqui


def _get_texts():
    text = [
        "Once upon a time, in a small village nestled amidst rolling green hills, there lived a young girl named Anya. Anya was known throughout the village for her extraordinarygift of storytelling. She could weave tales that transported listeners to magical lands, filled with adventure?, myste?ry, and wonder",
        "Once upon a time, in a small village nestled amidst rolling green hills, there lived a young girl named Anya. Anya was known throughout the village for her extraordinarygift of storytelling. She could weave tales that transported listeners to magical lands, filled with adventure?, myste?ry, and wonder",
        "Once upon a time, in a small village nestled amidst rolling green hills, there lived a young girl named Anya. Anya was known throughout the village for her extraordinarygift of storytelling. She could weave tales that transported listeners to magical lands, filled with adventure?, myste?ry, and wonder"
    ]
    for t in text:
        yield t


def _speech_synthesis(tts, text_queue):
    while True:
        text = text_queue.get()
        with tempfile.TemporaryDirectory() as tmp:
            file_name = f"{tmp}/output.wav"
            with supress_printouts():
                tts.tts_to_file(
                    text,
                    file_path=file_name
                )
            devnull = open(os.devnull, 'w')
            subprocess.check_call(
                ["ffplay", "-nodisp", "-autoexit", file_name],
                stdout=devnull,
                stderr=devnull
            )



def main():

    texts = _get_texts()
    text_queue = queue.Queue()

    with supress_printouts():
        tts = TTS("tts_models/en/ljspeech/glow-tts")
    with supress_printouts():
        tts = TextToSpeechCoqui("tts_models/en/ljspeech/glow-tts")
    threading.Thread(target=tts.run, kwargs={"incoming_text_queue": text_queue}, daemon=True).start()
    # threading.Thread(target=_speech_synthesis, args=(tts, text_queue), daemon=True).start()
    for text in texts:
        print(text)
        text_queue.put(text)
        time.sleep(2)
    input("prompt:")

if __name__ == '__main__':
    main()
