def main():
    student_dict = {'Jane Doe' : [80, 93, 76],
                    'Mickey Plumber' : [56, 100, 89],
                    'John Baker' : [90, 85, 67]}    
    answer = find_max_average(student_dict)
    print(f'Max average: (\'{answer[0]}\', {answer[1]})')

def average(student_dict):
    averages = {}
    for x in student_dict:
        averageSum = 0
        for y in student_dict[x]:
            averageSum += y
        averageSum /= 3
        averages[x] = averageSum
    return averages

def find_max_average(student_dict):
    averages = average(student_dict)
    maxVal = 0
    student = ''
    for x in averages:
        if (y := averages.get(x)) > maxVal:
            maxVal = y
            student = x
    return [student, maxVal]
     
main()
