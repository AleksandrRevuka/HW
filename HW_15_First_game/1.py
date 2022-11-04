number = ''
s = "4*9"
counter = -1
print(s[counter:])
while len(s):
    if s[counter:] in '*+/-':
        break
    else:
        number = s[counter:] + number
        s = s[:counter]
number = s + '-' + number
print(number)
