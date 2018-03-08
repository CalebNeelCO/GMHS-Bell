# GMHS BELL

A python program that sounds a bell based on a pre set schedule. The bell is triggered off of Raspberry PI3 GPIO. 

## Circuit Diagram

Setup:
A pcb made with a relay with both a NO and NC option. The bell is Hooked up to the normally open side of the realy. When there is 5 Min till the next item in the schedule it triggers the Raspberry PI's GPIO Pin 18 for 3 seconds. 

![circuit diagram](http://calebneel.com/relay_005_400x195.gif)
