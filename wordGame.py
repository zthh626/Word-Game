#!/usr/bin/env python3

import logging
import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
import random

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)

dictionary = open('words.txt', 'r')
words = []
for line in dictionary:
    words += line.split('/n')
dictionary.close()

def lettergame(x):
    y = str(x[0])
    print (y)
    print(len(y))
    letter = y[len(y) - 1: len(y)]
    print (letter)
    z = randomNum(letter)
    print (z)
    word = words[z]
    print(word)
    return word

def randomNum(x):
    print(x)
    letter = x.upper()
    if(letter == 'A'):
        return random.randint(1, 30808)
    elif(letter == 'B'):
        return random.randint(30808, 55069)
    elif(letter == 'C'):
        return random.randint(55069, 93964)
    elif(letter == 'D'):
        return random.randint(93964, 116703)
    elif(letter == 'E'):
        return random.randint(116703, 133503)
    elif(letter == 'F'):
        return random.randint(133503, 149344)
    elif(letter == 'G'):
        return random.randint(149344, 163785)
    elif (letter == 'H'):
        return random.randint(163785, 182417)
    elif (letter == 'I'):
        return random.randint(183543, 199344)
    elif(letter == 'J'):
        return random.randint(199344, 203488)
    elif (letter == 'K'):
        return random.randint(203488, 209642)
    elif (letter == 'L'):
        return random.randint(209642, 223713)
    elif(letter == 'M'):
        return random.randint(223713, 248881)
    elif (letter == 'N'):
        return random.randint(248881, 265031)
    elif (letter == 'O'):
        return random.randint(265031, 280068)
    elif (letter == 'P'):
        return random.randint(280068, 320979)
    elif (letter == 'Q'):
        return random.randint(320979, 324187)
    elif (letter == 'R'):
        return random.randint(324187, 345439)
    elif (letter == 'S'):
        return random.randint(345439, 396001)
    elif (letter == 'T'):
        return random.randint(396001, 421217)
    elif (letter == 'U'):
        return random.randint(421217, 444996)
    elif (letter == 'V'):
        return random.randint(444996, 451785)
    elif (letter == 'W'):
        return random.randint(451785, 463441)
    elif (letter == 'X'):
        return random.randint(463441, 464049)
    elif(letter == 'Y'):
        return random.randint(182417, 183542)
    elif (letter == 'X'):
        return random.randint(464049, 465872)

def main():
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')
    assistant = aiy.assistant.grpc.get_assistant()
    button = aiy.voicehat.get_button()
    with aiy.audio.get_recorder():
        status_ui.status('ready')
        aiy.audio.say('Say a word')
        print('Say a word')
        button.wait_for_press()
        status_ui.status('listening')
        print('Listening...')
        text = assistant.recognize()
        reply = (lettergame(text))
        aiy.audio.say(reply)
        while True:
            button.wait_for_press()
            status_ui.status('listening')
            print('Listening...')
            text = assistant.recognize()
            if text:
                if text == 'goodbye':
                    status_ui.status('stopping')
                    print('Bye!')
                    break
                if str(text[0])[0: 1] != reply[len(reply) - 1: len(reply)]:
                    print(str(text[0])[0: 1])
                    print((reply[len(reply)] - 1) - len(reply))
                    print('you lose')
                    aiy.audio.say('you lose')
                    break
                reply = (lettergame(text))
                aiy.audio.say(reply)

if __name__ == '__main__':
    main()