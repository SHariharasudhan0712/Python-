dict = {"a": ["A", "B", "C"], "b": ["D", "E", "F"]}

for i in dict["a"]:
    for j in dict["b"]:
        temp = i + j
        print(temp)
        print(temp[-1:] + temp[:-1])
