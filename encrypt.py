def makeGrid(k):
    letters = [chr(i) for i in range(97, 123)]
    alphebet = [chr(i) for i in range(97, 123)]
    gridStr = ""

    for i in k:
        if not i in letters:
            continue
        else:
            gridStr += i
            letters.remove(i)

    for i in alphebet:
        if not i in letters:
            continue
        elif len(gridStr) > 25:
            break
        else:
            if i == "j":
                if not "i" in letters:
                    continue
                else:
                    i = "i"
            gridStr += i
            letters.remove(i)

    res = list(gridStr)
    res = [res[i:i+5] for i in range(0, len(res), 5)]
    return res

def getCoords(char):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == char:
                return (y,x)
    return (0,0)

# inputs
key = "codingquest"
message = "please pick up some milk on thex wayx home"

spacePattern = [len(phrase) for phrase in message.split()]
message = message.replace(" ", "")
pairs:list = [message[i:i+2] for i in range(0, len(message), 2)]

grid = makeGrid(key)

for index, pair in enumerate(pairs):
    pos1 = getCoords(pair[0])
    pos2 = getCoords(pair[1])
    if pos1[0] != pos2[0] and pos1[1] != pos2[1]:
        pair = grid[pos1[0]][pos2[1]] + grid[pos2[0]][pos1[1]]

    elif pos1[0] == pos2[0]:
        pair = grid[pos1[0]][(pos1[1] + 1) % 5] + grid[pos1[0]][(pos2[1] + 1) % 5]

    elif pos1[1] == pos2[1]:
        pair = grid[(pos1[0] + 1) % 5][pos1[1]] + grid[(pos2[0] + 1) % 5][pos1[1]]

    pairs[index] = pair

count = 0
patternCount = 0
res = ""
for i in pairs:
    res += i
    count += 2
    if count == spacePattern[patternCount]:
        patternCount += 1
        res += " "
        count = 0

print(res)
