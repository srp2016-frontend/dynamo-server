import sys
import json
in_files = sys.argv[1:-1]
info = []
start_time = 32636
total_time = 0
x_offset = 6 * (len(in_files) - 1) 
for file in in_files:
    with open(file, 'r') as data:
        contents = data.read()
    lines = contents.split("\n")
    start_time = int(lines[0].split(" ")[2])
    for line in lines:
        if line.strip() == "":
            continue
        items = line.split(" ")
        x = float(items[0]) + x_offset
        y = float(items[1])
        time = int(items[2]) - start_time + total_time
        info.append([x, y, time])
    total_time = int(lines[-2].split(" ")[2]) - start_time + total_time
    x_offset -= 6
with open(sys.argv[-1], 'w') as out:
    out.write(json.dumps(info))