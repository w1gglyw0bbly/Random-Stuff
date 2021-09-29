techCompanies = ['Apple:Tim Cook', 'Amazon:Jeff Bezos', \
                  'Google:Sunder Pichai', \
                  'Microsoft:Satya Nadella', 'Facebook:Mark Zuckerberg', \
                  'Oracle:Larry Ellison', 'IBM:Arvind Krishna']

flag = False
hint = 0

response = input('Enter the name of an organization or CEO.\n\nIf you need a hint press Enter: ').lower()


if response == '':
    print('\nSome of the top tech-companies are Apple, Amazon, Google, Microsoft, Facebook, Oracle and IBM.\n')
    response = input('Enter the name of a CEO now: ').lower()
    hint = 1

for i in techCompanies:
    #checking for name of CEO
    if i.split(':')[0].lower() == response and hint == 0:
        print('Correct! ' + i.split(':')[1] + ' is the CEO of ' + i.split(':')[0])
        flag = True

    #checking for name of organization
    elif i.split(':')[1].lower() == response:
        print('Correct! ' + i.split(':')[1] + ' is the CEO of ' + i.split(':')[0])
        flag = True

if flag == False:
    print('Incorrect entry. The program ends here.')

