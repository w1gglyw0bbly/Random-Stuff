def displayGoods(items):
    print('Goods Available: ')
    for x in items:
        print(x)

def main():
    with open('inven.txt') as x:
        items = x.read().split('\n')

    displayGoods(items)

if __name__ == '__main__':
    main()
