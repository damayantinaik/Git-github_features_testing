fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in lst:
            continue
        lst.append(word)
        lst.sort()
print(lst[ :11])
print("Switch between branch, now I am in test branch")

Print('This is to check the changes-test purpose only')
print("This is for testing branch")
