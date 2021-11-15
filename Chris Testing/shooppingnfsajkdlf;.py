def build_dict_by_id(products):
    productDict = {}
    for x in products:
        item = x.split(',')
        key = item[0]
        item.remove(key)
        productDict[key.lower()] = item
    return productDict

def build_dict_by_category(products):
    productDict = {}
    for x in products:
        things = x.split(',')
        if things[1] in productDict:
            productDict[things[1].lower()].append(things[0])
        else:
            productDict[things[1].lower()] = [things[0]]
    return productDict

def checkout(cart,dict_ID):
    total = 0
    for x in cart:
        total += float(dict_ID[x][2])
    return total

def build_list_by_ratings(dict_category, dict_ID, user_category, min_rating):
    ratings_list = []
    for product_id in dict_category[user_category]:
        if float(dict_ID[product_id.lower()][3]) > min_rating:
            ratings_list.append(product_id)
    return ratings_list

def main():
    products = ['B001,book,Patriot Games, 15.95, 3.75', 'B002,book,Origin, 19.95, 2.5', 'C001,clothing,Armani Suit, 800.00, 3.5',
          'B003,book,Animal Farm, 9.97, 4', 'B004,book,Grant, 22.50, 4.2', 'F001,food,Moose Drool Ale 6-pack, 9.95, 4.6',
          'C002,clothing,Pants, 39.95, 2.7', 'B005,book,Prairie Fires, 18.95, 1.2','C003,clothing,Vasque Hiking Boots, 109.00, 2.3',
          'C004,clothing,Wool Hat, 14.00, 4.5', 'F002,food,Jumbo shrimp, 12.50, 4','C005,clothing,Wrangler Jeans, 24.50, 4.1',
          'B005,book,Ragtime, 17.25,3','F003,food,Fusili - 16 oz., 2.95, 4', 'C006,clothing,Nike T-shirt, 19.00, 5',
          'C007,clothing,Gore-Tex Gloves, 39.00, 0.1','C008,clothing,North Face Fleece Jacket, 89.95, 4.3',
          'C009,clothing,Nationals Logo Sweatshirt, 49.00, 2.9','F004,food,Lamb Chops, 21.95, 4.95',
          'C010,clothing,New Balance Trail Runners,69.95, 3.6','B006,book,Future Shock, 8.95, 2.5']

    dict_ID = build_dict_by_id(products)
    dict_category = build_dict_by_category(products)
    cart = []
    
    while True:
        #Intro
        print('Welcome to shopping at Shoppers Stop!\nWe sell products in the following categories: [\'book\', \'clothing\', \'food\']')
        user_input = input('Please input a category name or input \'checkout\' to quit: ').lower()
        
        #Checking for checkout or category
        if user_input == 'checkout':
            #Print cart and total then quit
            print('Thanks for shopping at Shoppers Stop. You purchased the following product(s): ')
            for x in cart:
                print(f'{x.upper()} {dict_ID[x]}')
            total = checkout(cart, dict_ID)
            print(f'The amount is: ${total}')
            break
        elif user_input in dict_category:
            #Ask user for ratings
            user_inputYN = input('Would you like to see products in this cateogry filtered by minimum customer ratings (0-5)? Y/N: ').lower()
            if user_inputYN == 'y':
                #Ask user for min rating
                user_inputRating = float(input('Please enter the minimum rating: '))
                productsRated = build_list_by_ratings(dict_category, dict_ID, user_input, user_inputRating)
                #Print results by min rating
                for x in productsRated:
                    print(f'Product ID: {x}, Information: {dict_ID[x.lower()]}')
            elif user_inputYN == 'n':
                #Print out all products under category
                for x in dict_category[user_input]:
                    print(f'Product ID: {x}, Information: {dict_ID[x.lower()]}')
            
            #Ask user for product to add to cart
            user_inputCart = input('Please input product ID or type any key to return: ')
            
            #Add to cart and print item specifics
            if user_inputCart.lower() in dict_ID:
                cart.append(user_inputCart.lower())
                print(f'{user_inputCart} added to cart')
                continue

main()
