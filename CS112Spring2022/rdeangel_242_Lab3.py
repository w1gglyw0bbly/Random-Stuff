def pizza_coverage(r_pizza, r_pep, num_pep):
    #getting areas for pizza and pepperonis
    pizzaArea = 3.14159 * pow(r_pizza, 2)
    pepTotal = (3.14159 * pow(r_pep, 2)) * num_pep
    
    #getting the percentage of pepperoni compared to pizza
    percent = pepTotal / pizzaArea * 100
    
    #checking for customer satisfaction based on percentage
    if percent >= 75:
        print('happy customer')
    elif percent >= 50:
        print('neutral customer')
    else:
        print('sad customer')

#function test runs
pizza_coverage(5, 1, 10)
pizza_coverage(5, 1, 15)
pizza_coverage(5, 1, 20)
