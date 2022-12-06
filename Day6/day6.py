def parseTxt():
    f = open('Day6/day6.txt', encoding='utf8',mode = 'r')
    #f = open('Day6/test.txt', encoding='utf8',mode = 'r')
    dataStream = f.read().strip('\n')
    print(dataStream)
    stop = 0
    for index, packet in enumerate(dataStream):
        if index+13 > len(dataStream):
            continue
        else:
            if stop != 1:
                buffer = set(dataStream[index:index+4])
                if len(buffer) == 4:
                    part1 = index+4
                    stop = 1
        
            buffer = set(dataStream[index:index+14])
            if len(buffer) == 14:
                part2 = index+14
                break

    f.close()
    return part1, part2

marker, marker2 = parseTxt()
print(marker, marker2)

