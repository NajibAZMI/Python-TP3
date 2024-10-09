def maxAB(a,b):
                    return a if a>b else b
def maxList(Liste):
        max_v=Liste[0]
        for i in range(len(Liste)):
                max_v=maxAB(max_v,Liste[i])
        return max_v
a=float(input("a="))
b=float(input("b="))

print(f"max({a},{b})={maxAB(a,b)}")
list1=[1,9,3,12,18,4]

print(list1)
print(f"max de list est : {maxList(list1)}")