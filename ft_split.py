def ft_split(s: str, delim: str) -> list:
    arr = []
    word = ""
    for i in s:
       if i  == chr(3):
         break
       if i is delim:
            if word != "":
                arr.append(word)
            word = ""
            continue
       word = word+i
    if word != "":
        arr.append(word)   
    return(arr)

print(ft_split("let's       try it again   ", " "))