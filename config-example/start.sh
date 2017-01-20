#!/bin/bash

echo "Starting Finch..."
dbus-launch screen -S rainbow -dmLU -t 0 finch
echo "Waiting 20 sec..."
sleep 20
echo "Starting 1st bridge..."
screen -S rainbow -X screen -t 1
screen -S rainbow -p 1 -X stuff $'../rainbow-bridge.py bots.conf\n'
#echo "Starting 2nd bridge..."
#screen -S rainbow -X screen -t 2
#screen -S rainbow -p 2 -X stuff $'../rainbow-bridge.py people.conf\n'
