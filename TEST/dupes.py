'''receive = input('enter word here: ')

used = []
for x in receive:
    if x in used:
        continue
    else:
        #quit()
        used.append(x)

for x in used:
    print(f'{x}--', end = ' ')
print()


print(f'Unique Letters: {used}\nCount: {len(used)}')'''
tlist = [1,2,3]
blist = tlist
blist.remove(1)
print(f'blist: {blist} tlist: {tlist}')
