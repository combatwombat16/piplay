import RPi.GPIO as GPIO
import time
import socket

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(29,GPIO.OUT)
    GPIO.setup(31,GPIO.OUT)
    GPIO.setup(33,GPIO.OUT)
    GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def start_stop():
    GPIO.output(7,True)
    time.sleep(.5)
    GPIO.output(11,True)
    time.sleep(.25)
    GPIO.output(13,True)
    time.sleep(.25)
    GPIO.output(13,False)
    time.sleep(.25)
    GPIO.output(11,False)
    time.sleep(.25)
    GPIO.output(7,False)
    time.sleep(.5)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255',0))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

morse = {"a": ".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"}

def print_dot(pin):
    GPIO.output(pin,True)
    time.sleep(.1)
    GPIO.output(pin,False)
    time.sleep(.2)

def print_dash(pin):
    GPIO.output(pin,True)
    time.sleep(.35)
    GPIO.output(pin,False)
    time.sleep(.2)

def print_break(pin):
    GPIO.output(pin,True)
    time.sleep(.05)
    GPIO.output(pin,False)
    time.sleep(.05)

def print_morse_char(letter,pin,bpin):
    for dosh in morse[letter.lower()]:
        if dosh == ".":
            print_dot(pin)
        elif dosh == "-":
            print_dash(pin)
        else:
            continue
    time.sleep(.5)
    

def print_morse_message(message,pin,bpin,wpin):
    words = message.split(" ")
    for word in words:
        for letter in word:
            if letter.lower() in morse:
                print_morse_char(letter,pin,bpin)
            else:
                print_break(bpin) 
        print_break(wpin)

init()
start_stop()
triggered = False
input_message = input("Enter morse message:")
print_morse_message(input_message,33,31,29)
while not triggered:
    input_state = GPIO.input(12)
    if input_state == False:
        print_morse_message(get_ip(),33,31,29)
        time.sleep(.2)
        triggered = True
start_stop()

GPIO.cleanup()



