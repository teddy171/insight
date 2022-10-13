from datetime import timedelta
import os
import subprocess

import whisper
from transformers import MarianTokenizer, MarianMTModel

def translation(src, trg, text):
    '''translation any text from src to trg'''

    model_name = f"Helsinki-NLP/opus-mt-{src}-{trg}"
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    batch = tokenizer([text], return_tensors="pt")

    generated_ids = model.generate(**batch, max_length=512)
    return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

def generate_subtitle(video_full_path):
    '''extract text from video's audio, translation, then generate subtitle in srt format'''

    model = whisper.load_model("base") # Change this to your desired model
    print("Whisper model loaded.")
    (file_path, file_name) = os.path.split(video_full_path)
    (name, suffix) = os.path.splitext(file_name)

    try:
        os.mkdir(f"{file_path}/.cache/")
    except FileExistsError:
        pass

    audio_path = f"{file_path}/.cache/{name}.wav"
    srt_path = f"{file_path}/.cache/{name}.srt"
    cmd_line = f"ffmpeg -i \"{video_full_path}\" \"{audio_path}\""     #extract audio from video

    subprocess.call(cmd_line, shell=True)
    print("Already extract audio.")

    transcribe = model.transcribe(audio=audio_path, fp16=False)
    segments = transcribe['segments']

    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text'].strip()
        text += ("\n" + translation("en", "zh", text))
        segment_id = segment['id']+1
        segment = f"{segment_id}\n{startTime} --> {endTime}\n{text}\n\n"

        with open(srt_path, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)

        if segment_id % 20 == 0:
            print(f"Already complete the {segment_id}th subtitle")

    return srt_path

def merge_subtitle(video_path, subtitle_path):
    '''Use ffempeg to merge subtitles to video'''
    (video_dir, file_name) = os.path.split(video_path)
    (video_name, suffix) = os.path.splitext(file_name)

    cmdLine = f"ffmpeg -i \"{video_path}\" -vf subtitles=\"{subtitle_path}\" \"{video_dir}/{video_name}(with-subtile){suffix}\""
    subprocess.call(cmdLine, shell=True)

if __name__ == "__main__":
    video_full_path = input("Please input the target video below\n")
    
    subtitle_full_path = generate_subtitle(video_full_path)

    merge_choice = input("Do you want to merge the subtitle to the video now?(y/n)")
    if merge_choice == "y":
        merge_subtitle(video_full_path, subtitle_full_path)
