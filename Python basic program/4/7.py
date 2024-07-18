filename = input("Enter a file name: ")
f1 = open(filename, 'w')
f1.write('Ethical Hacking\n')
f1.write('Cyber Security\n')
f1.write('Cyber Law\n')
f1.close()

f1 = open(filename, 'r')
data = f1.readlines()
print(data)
for i in data:
    print(i[::-1])
f1.close()
