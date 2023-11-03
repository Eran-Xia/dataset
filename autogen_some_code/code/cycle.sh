#!/bin/bash
while true
do
    python3 /home/wind/Desktop/projects/autogen_some_code/code/chat.py -t math-solution
    if [ $? -eq 0 ]; then
        break
    else
        echo "Rerun"
    fi
    sleep 60
done