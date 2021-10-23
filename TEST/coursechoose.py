#write your while loop, menu option here
def main():
    course_list, checkout_list = ['Fundamentals of Python:14.88', 'Full Stack Development:12.99', 'Cyber Security:10.99', 'Descriptive Statistics using R:20.0'], []
    print('*********** Welcome to Course checkout system ***********')
    while 1 == 1:
        sel = int(input('Available options:\n1: View Courses\n2: Add course\n3: Delete a course\n4: Checkout\n5: Exit\n\nEnter option: '))
        if sel == 1:
            print('******* List of Courses available *******\n\nTitle--Price\n------------------------')
            for x in course_list:
                cart = ''
                cart += x.split(':')[0] + '--$' + x.split(':')[1]
                print(cart)
            print('********************************\n')
                

main()
