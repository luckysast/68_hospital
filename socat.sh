#!/bin/bash
echo "Start socat server with server.py"
while [ 1 ]
do
socat TCP-LISTEN:1488,reuseaddr,fork EXEC:./server.py
done
