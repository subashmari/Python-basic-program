filename = input("Enter a file name: ")
f1 = open(filename, 'w')
f1.write('Ethical Hacking\n')
f1.write('Cyber Security\n')
f1.write('Cyber Law\n')
f1.close()

f1 = open(filename, 'r')
data = f1.read()
a = list(set(data))
a.sort()  # sort the list in place
print(a)
f1.close()

for i in a:
    if i != ' ':  # exclude spaces from the count
        count = data.count(i)
        print("{} has occurred {} times".format(i, count))
