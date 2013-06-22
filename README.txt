Code for using your Raspberry Pi to make your home a SmartHome.


---- Features ----

Use a web interface, powered by JavaScript to control the GPIO pins. Built
with a secure login to stop unauthorised access. Uses a library included
with the WebIOPi software availible here, https://code.google.com/p/webiopi/
Currently, it uses three pins, #23 and #24 for motor control to open and
close curtains and pin #18 for triggering relay to switch mains sockets on
and off. Consists of a server file written in python, and a GUI in the form
of a webpage with JavaScript.


---- Installation ----

From your networked Raspberry Pi you will need to run "sudo apt-get install
git-core". This installs Git which is used to pull this code off of GitHub.
Next, after that has completed, run "git clone
git://github.com/Jamie-/SmartHome.git". Now you have the files to run and
use the software. (Note, you must have WebIOPi installed [tested with
version 0.6.0]). Navigate to your cloned directory with "cd SmartHome" and
run (Must have "python-dev" installed) "sudo python home_auto_server.py".
Using a browser, go to "<pi's IP address>:3333" from another computer on the
network, or go to "localhost:3333" on your Pi's GUI browser. The defualt
port is "3333" but this can be changed by editing the python script. When
you go to this address, it will ask you to login. Username is "user" and 
password is "password" by default but as again, this can easily be changed
by editing the python script. You are now good to go!


---- Wiring ----

GPIO pin #23 is linked to the "Open" button.
GPIO pin #24 is linked to the "Close" button.
Only one of these two can be active at once for H-Bridge control. This can
yet again be easily edited by editing the python script.
The "Stop" button pulls pins #23 and #24 low again when clicked.
GPIO pin #18 is linked to the "L1 On" and "L1 Off" buttons.
More configurations can be added by editing the server pyhton script and the
"index.html" file.


---- Future Dev ----

Add more options for GPIO control.
Make a settings/config file for easily changing port number and login.


---- Help ----

If you encounter any issues installing it, drop and email to
"github@jami.org.uk" and I'll try to help you. When asking for help, include
details of your setup and configuration to help me solve the problem. Also
submit any bugs to that address.


Jamie