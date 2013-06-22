# Imports
import webiopi

# Retrieve GPIO lib
GPIO = webiopi.GPIO

# -------------------- #
# Define Variables     #
# -------------------- #

OPEN=24        # Opening motor
CLOSE=23       # Closing motor
L1=18          # Lighting toggle (circuit 1)

# -------------------- #
# Functions            #
# -------------------- #

def c_open():
    GPIO.output(OPEN, GPIO.LOW)
    GPIO.output(CLOSE, GPIO.HIGH)

def c_close():
    GPIO.output(OPEN, GPIO.HIGH)
    GPIO.output(CLOSE, GPIO.LOW)

def c_stop():
    GPIO.output(OPEN, GPIO.LOW)
    GPIO.output(CLOSE, GPIO.LOW)
	
def light1_on():
	GPIO.output(L1, GPIO.HIGH)

def light1_off():
	GPIO.output(L1, GPIO.LOW)

# -------------------- #
# Macro definition     #
# -------------------- #

def curtain_open():
    c_open()

def curtain_close():
    c_close()
	
def curtain_stop():
    c_stop()
	
def l1_on():
	light1_on()
	
def l1_off():
	light1_off()
    
# -------------------- #
# Initialization       #
# -------------------- #

# Setup GPIOs
GPIO.setFunction(CLOSE, GPIO.OUT)
GPIO.setFunction(OPEN, GPIO.OUT)
GPIO.setFunction(L1, GPIO.OUT)

c_stop()
light1_off()

# -------------------- #
# Main server          #
# -------------------- #

# Instantiate the server on the port 8000, it starts immediately in its own thread
server = webiopi.Server(port=3333, login="user", password="password")

# Register the macros so you can call it with Javascript and/or REST API

server.addMacro(curtain_open)
server.addMacro(curtain_close)
server.addMacro(curtain_stop)
server.addMacro(l1_on)
server.addMacro(l1_off)

# -------------------- #
# Loop                 #
# -------------------- #

# Run our loop until CTRL-C is pressed or SIGTERM received
webiopi.runLoop()

# -------------------- #
# Termination          #
# -------------------- #

# Stop the server
server.stop()

# Reset GPIO functions
GPIO.setFunction(OPEN, GPIO.IN)
GPIO.setFunction(CLOSE, GPIO.IN)
GPIO.setFunction(L1, GPIO.IN)
