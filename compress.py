def compress(s: str) -> str:
    if not s:
        return ""
    a = 1
    x = True
    string = ""
    for n in range(1, len(s)):
        if n == 0:
            a += 1
        elif s[n] == s[n-1] and n != 0:
            a += 1
            x = False
        else:
            string += s[n-1] + str(a)
            a = 1
    if x == True:
        return s
    string += s[-1] + str(a)
    return string

print(compress("aabcccccaaa")) 
print(compress("abcd"))  
print(compress("aa")) 
print(compress("a")) 
print(compress("")) 
  
            