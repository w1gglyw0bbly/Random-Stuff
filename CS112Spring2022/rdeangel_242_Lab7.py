def cut_list(number_list):
    results = []
    for x in number_list:
        if x not in results:
            results.append(x)
    return results

def odd_even(sumVar):
    if sumVar % 2 == 0:
        return 0
    return 1

def sum_number(number_list):
    number_list = cut_list(number_list)
    total = 0
    for x in number_list:
        total += x
    #if result is even
    if odd_even(total) == 0:
        print('Sum: ' + str(total) + ' (this is an even number)')
    #if result is odd because it is the only other option
    else:
        print('Sum: ' + str(total) + ' (this is an odd number)')
