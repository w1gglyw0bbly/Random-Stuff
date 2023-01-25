def findMatches(matches):
    matchesCopy = []
    for i in matches:
        matchesCopy.append(i)
    matches.clear()
    for i in range(2, len(matchesCopy), 3):
        if matchesCopy[i] >= 80:
            matches.append(matchesCopy[i - 2 : i + 1])
    max = 0
    for i in range(len(matches)):
        if matches[i][2] > matches[max][2]:
            max = i
    matches[max].append('\u2665')
    return matches

#print(findMatches(['JS', 'M', 76, 'MS', 'M', 90]))

def cantRemeberName(inputX):
    checkedList = []
    inputXCopy = []
    for i in inputX:
        inputXCopy.append(i)
    inputX.clear()
    for i in range(len(inputXCopy)):
        count = 0
        for j in range(len(inputXCopy)):
            if inputXCopy[i][0] == inputXCopy[j][0]:
                count += 1
        if inputXCopy[i][0] in checkedList:
            continue
        inputX.append((inputXCopy[i][0], count))
        if inputXCopy[i][0] not in checkedList:
            checkedList.append(inputXCopy[i][0])
    return inputX
        
#print(cantRemeberName([['B111', 'DATE'], ['B111', 'DATE'], ['B222', 'DATE'], ['B111', 'DATE']]))

def combineInfo(profileInfo, datingTrack):
    for i in range(len(profileInfo)):
        for j in range(len(datingTrack)):
            if profileInfo[i][1] == datingTrack[j][0]:
                profileInfo[i] = [profileInfo[i][0], profileInfo[i][1], datingTrack[j][1]]
    return profileInfo

#print(combineInfo([['Anadi Saunders', 'B111'],['Thaddeus Huff', 'B222'], ['Deven Holden', 'B333']], [('B111', 4), ('B333', 2)]))

def setofNames(profiles, location):
    output = set()
    for i in profiles:
        if profiles[i][2] == location:
            output.add(profiles[i][0])
    return output

#print(setofNames({'B111':['Anahi Saunders', '53535531351', 'Fairfax'], 'B222':['Thaddeus Huff', '21414124', 'Washington DC']}, 'Fairfax'))