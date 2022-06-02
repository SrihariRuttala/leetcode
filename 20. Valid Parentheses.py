string = input("Enter the string : ")
dic = {"(":")", "[":"]", "{":"}"}
stack = []
for i in range(len(string)):
    if string[i] in dic.keys():
        stack.append(string[i])
    elif len(stack)!=0:
        temp = stack.pop()
        if dic[temp] != string[i]:
            print("false")
            exit()
    else:
        print("false")
        exit()

if len(stack) == 0:
    print("true")
else:
    print("false")
