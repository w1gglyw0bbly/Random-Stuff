def main():
    course_list, checkout_list = ['Fundamentals of Python:14.88', 'Full Stack Development:12.99', 'Cyber Security:10.99', 'Descriptive Statistics using R:20.0'], []
    print('*********** Welcome to Course checkout system ***********\n')
    #Staring loop for interface
    while 1 == 1:
        sel = int(input('Available options:\n1: View Courses\n2: Add course\n3: Delete a course\n4: Checkout\n5: Exit\n\nEnter option: '))
        #1st option
        if sel == 1:
            print('******* List of Courses available *******\n\nTitle--Price\n------------------------')
            for x in course_list:
                print(f'{x.split(":")[0]}--${x.split(":")[1]}')
            print('********************************\n')
        #2nd option
        elif sel == 2:
            item = input('Enter course title to add to cart: ').lower()
            checkout_list.append(item)
            yourCart(course_list, checkout_list, False)
        #3rd option 
        elif sel == 3:
            item = input('\nEnter course title to delete: ').lower()
            #Item to reomve is in cart
            if item in checkout_list:
                for y in course_list:
                    if item == y.split(":")[0].lower():
                        checkout_list.remove(item)
                        print(f'{y.split(":")[0]}\n{y.split(":")[0]} deleted from cart\n')
                        continue
            #Item to remove not in cart
            else:
                for y in course_list:
                    if item == y.split(':')[0].lower():
                        print(f'{y.split(":")[0]}\n{y.split(":")[0]} not in your cart\n')
            yourCart(course_list, checkout_list, False)
        #4th option
        elif sel == 4:
            yourCart(course_list, checkout_list, True)
        #5th option
        elif sel == 5:
            print('******** Thank you for shopping with us ********')
            break

#Helper function for printing out cart contents  
def yourCart(course_list, checkout_list, checkout):
    print('******** Your Cart ********\nTitle--price')
    for x in checkout_list:
        for y in course_list:
            if x == y.split(':')[0].lower():
                print(f'{y.split(":")[0]}--${y.split(":")[1]}')
    if checkout == True:
        total = 0
        for x in checkout_list:
            for y in course_list:
                if x == y.split(':')[0].lower():
                    total += float(y.split(':')[1])
        print(f'Your Total: {round(total, 2)}')
    print('*********************************\n')

main()
