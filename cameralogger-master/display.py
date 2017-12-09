# code modified, tweaked and tailored from code by bertwert
# on RPi forum thread topic 91796
import RPi.GPIO as theGPIO

theGPIO.setmode(theGPIO.BCM)

# GPIO ports for the 7seg pins
segments =  (11,17,23,8,7,10,18,25)

def initDisplay():
    for segment in segments:
        theGPIO.setup(segment, theGPIO.OUT)
        theGPIO.output(segment, 0)
 
num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}
 
def displayNumber(number):
    try:
        numIdx = str(number)
        for loop in range(0,7):
            theGPIO.output(segments[loop], num[numIdx][loop])
    except:
        print ("Unexpected error:{0}:{1}".format(e.errno, e.strerror))
        theGPIO.cleanup()
        raise
    
