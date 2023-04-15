import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO
from picamera import PiCamera
camera = PiCamera()
sensorPin = 36 
mainID = -1001193557017
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
def handle(msg):
    curr = False
    prev = False
    chat_id = msg['chat']['id']
    command = msg['text']
    print(chat_id)
    if chat_id == mainID:
        print(chat_id)
        bot.sendMessage(str(mainID),'Device Activated')
        print ('Got command: %s' % command)
        while True:
            time.sleep(2)
            curr = prev
            curr = GPIO.input(sensorPin)
            if curr != prev:
                if curr:
                    camera.start_preview()
                    camera.capture('/home/pi/Telegram/images/image.jpg')
                    camera.stop_preview()
                    bot.sendPhoto(chat_id,open('/home/pi/Telegram/images/image.jpg', 'rb'))
                    time.sleep(1)
    elif chat_id != mainID:
        bot.sendMessage(chat_id,'YOU ARE NOT AUTHORIZED')
bot = telepot.Bot('ENTER_BOT_TOKEN_HERE')
bot.sendMessage(str(mainID),'Device Standby')
bot.message_loop(handle)
print ('I am listening...')
while 1:
    time.sleep(10)
