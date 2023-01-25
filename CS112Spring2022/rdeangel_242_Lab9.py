def word_counter(fileInput, fileOutput):
    file = open(fileInput, 'r')
    lines = file.readlines()
    file.close()
    lineWordCount = []
    for x in range(2, len(lines)):
        count = 0
        for y in lines[x]:
            if y == ' ':
                count += 1
        lineWordCount.append(count + 1)
    output = lines[0] + lines[1]
    for x in range(len(lineWordCount)):
        if x == len(lineWordCount) - 1:
            output += 'Words: ' + str(lineWordCount[x])
        else:
            output += 'Words: ' + str(lineWordCount[x]) + '\n'
    fileO = open(fileOutput, 'w')
    fileO.write(output)
    fileO.close()

word_counter('fileInput.txt', 'fileOutput.txt')
