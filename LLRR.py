s = input(); 
countL = 0;
countR = 0;
result = []
temp = ""
for ch in s:
    temp += ch

    if ch == "L":
        countL += 1
    else:
        countR += 1
    if countR == countL:
        result.append(temp)
        temp = ""

print(len(result))
for x in result :
    print(x)

    
