#!/bin/bash
# run the sleepy_boi.sh script in another terminal first
# then run this script with one of the following command line arguments:
# [start|stop|kill|interrupt]

# README: I use pkill here instead of kill, this is so I don't have to know the process ID of sleepy_boi.sh

#Start sleepy_boi.sh
if [ $1 == "start" ]; then
    pkill -18 sleepy_boi.sh

#Stop sleepy_boi.sh
elif [ $1 == "stop" ]; then
    pkill -19 sleepy_boi.sh

#Kill sleepy_boi.sh
elif [ $1 == "kill" ]; then
    pkill -9 sleepy_boi.sh

#Interrupt sleepy_boi.sh
elif [ $1 == "interrupt" ]; then
    pkill -2 sleepy_boi.sh
fi