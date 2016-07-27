import random
import math
items = ["Brian DeLeonardis","Jack Dates", "Anthony Fasano", "Anthony Hamill", "Brandon Guglielmo", "Chase Moran", "Daniel Collins", "Kevin DeStefano", "Matthew Kumar", "Ryan Goldstein", "Tina Lu"]
with open('countries', 'r') as data:
    nations = data.read().split('\n')
positions = []
for i in range(len(items)):
    positions.append([])
    velocity = random.randrange(25, 45)
    angle = (random.random() - 0.5) / 10
    x = 40
    y = (i + 1) * 40
    for j in range(20):
        positions[i].append((x, y))
        x += math.cos(angle) * velocity
        y += math.sin(angle) * velocity
string = "["
for j in range(20):
    string += "\n\"["
    for i in range(len(items)):
        item = items[i]
        x,y = positions[i][j]
        country = random.choice(nations)
        while country.strip() == "":
            random.choice(nations)
        string += "new Item(" + str(x) + ", " + str(y) + ", '" + items[i] + "', 18, '" + country + "', 'Athlete'),"
    string += "]\","
string += "]"
print(string)
