from macos_speech import Synthesizer
import random

speaker = Synthesizer()


def voices():
    for voice in speaker.voices:
        print(str(voice.name))
        speaker.voice = voice
        speaker.say(str(voice.name))
    pass
pass


def canada_question_mark():
    speaker.voice = "Good"
    speaker.say("ABCDEFGHJLKLMNOPQRSTUA")
pass

myinput = int(input("1 or 2"))

if myinput == 1:
    voices()
pass
if myinput == 2:
    canada_question_mark()
else:
    print("not works")
    exit(1)
