haystack = "hello"
needle = "ll"
needle_length = len(needle)

if needle == haystack:
    print("0")
    exit()

elif needle == "" or haystack == "":
    print(-1)
    exit()

for i in range(len(haystack) - needle_length+1):
    if haystack[i:i+needle_length] == needle:
        print(i)
        break