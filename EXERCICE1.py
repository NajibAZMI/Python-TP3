from math import pow
def id1(a,b):
             return  pow((a-b),2)  
def id2(a,b):
        return (a+b)*(a+b)
def id3(a,b):
        return (a+b)*(a-b)
print("({}+{})({}-{})={}".format(4,1,4,1,id3(4,1)))  
