#Part 1
hours = int(input('Please input the hours:\n')) * 60 * 60
minutes = int(input('Please input the minutes:\n')) * 60
seconds = int(input('Please input the seconds:\n'))
totalTime = hours + minutes + seconds
print(f'The total time in seconds is:\n{totalTime}\n')

#Part 2
seconds2 = int(input('Please input the seconds:\n'))
hours2 = (seconds2 // 60) // 60
minutes2 = (seconds2 // 60) % 60
secondsRemainder = (seconds2 % 60) % 60
print(f'That is {hours2} hr(s) {minutes2} min(s) {secondsRemainder} sec(s)')
