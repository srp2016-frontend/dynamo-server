#!/bin/sh
python3 RFJoin.py dataOut* dataProcessB.txt
cat brian | python3 RFProcess.py dataProcessB.txt > /dev/null 