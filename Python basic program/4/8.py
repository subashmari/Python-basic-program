filename = input("Enter a file name: ")
c = 0
w = 0
l = 0
f1 = open(filename, 'w')
f1.write('Ethical Hacking\n')
f1.write('Cyber Security\n')
f1.write('Cyber Law\n')
f1.close()

f2 = open(filename, 'r')
data = f2.readlines()
print(data)
for i in data:
    c = c + len(i)
    w = w + len(i.split())
    l = l + 1

f2.close()
print('The number of characters are:', c)
print('The number of words are:', w)
print('The number of lines are:', l)
