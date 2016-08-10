#!/bin/sh
python3 RFJoin.py dataOut* dataProcessB.txt dataProcessBFlip.txt
cat info | python3 RFProcess.py dataProcessB.txt dataProcessBFlip.txt > /dev/null 
