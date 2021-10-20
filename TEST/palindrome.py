'''word = input('Write it: ')

newWord = ''
for i in reversed(range(len(word))):
    newWord += word[i]

print(word + ' ' + newWord)
if word == newWord:
    print(True)
'''
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False



#print(valid_parentheses('hi(hi)()'))
#print(valid_parentheses(''))
#print(valid_parentheses('hi())('))
#print(valid_parentheses('('))
#print(valid_parentheses(')'))
print(valid_parentheses('())(()'))
'''
test = 'testString'
test = test[1:-1]

print(test)'''


