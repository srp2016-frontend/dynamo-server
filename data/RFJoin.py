import sys
import json
in_files = sys.argv[1:-2]
info = []
start_time = 32636
total_time = 0
x_offset = 6 * (len(in_files) - 1) 
for file in in_files:
    with open(file, 'r') as data:
        contents = data.read()
    lines = contents.split("\n")
    start_time = int(lines[0].split(" ")[2])
    xprev = -1
    yprev = -1
    timeprev = -1
    for line in lines:
        if line.strip() == "":
            continue
        items = line.split(" ")
        x = 6 - float(items[0]) + x_offset
        y = float(items[1])
        time = int(items[2]) - start_time + total_time
        if xprev != -1 and yprev != -1 and timeprev != -1:
            midx = (x + xprev) / 2
            midy = (y + yprev) / 2
            midtime = (time + timeprev) / 2
            info.append([midx, midy, midtime])
        xprev = x
        yprev = y
        timeprev = time
        info.append([x, y, time])
    total_time = int(lines[-2].split(" ")[2]) - start_time + total_time
    x_offset -= 6
with open(sys.argv[-2], 'w') as out:
    out.write(json.dumps(info))
info = info[1:]
for frame in info:
    frame[1] = 6 - frame[1]
with open(sys.argv[-1], 'w') as out:
    out.write(json.dumps(info))
