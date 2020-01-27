import os

# Complete the isBalanced function below.
def isBalanced(s):
    outflag = False
    flag = True
    while(flag):
        #print("s while : "+s)
        s = s.strip()
        i = s.rfind("(")
        j = s.rfind("[")
        k = s.rfind("{")
        l = s.rfind(")")
        m = s.rfind("]")
        n = s.rfind("}")
        #print("0---ijk "+str(i) + " " + str(j)+ " "+ str(k))
        if i>j and i>k:     #inner most is "("
            #print("s skip:"  + s[i+1:])
            x = s.find(")", i+1)
            y = s.find("]", i+1)
            z = s.find("}", i+1) 
            #print("1--- xyz "+str(x) + " " + str(y)+ " "+ str(z))
            if (x<y or y==-1) and (x<z or z==-1) and x>i: #() matched
                local = s[0:i] + s[x+1:]
                s = local
                #print("s : " + s)
            else:
                #print("s : " + s)
                outflag = False
                flag = False
        elif j>i and j>k:   #inner most is "["
            #print("s skip:"  + s[j+1:])
            x = s.find(")", j+1)
            y = s.find("]", j+1)
            z = s.find("}", j+1) 
            #print("2--- xyz "+str(x) + " " + str(y)+ " "+ str(z))
            if (y<x or x==-1) and (y<z or z==-1) and y>j: #[] matched
                local = s[0:j] + s[y+1:]
                s = local
                #print("s : " + s)
            else:
                #print("s : " + s)
                outflag = False
                flag = False
        elif k>i and k>j:   #inner most is "{"
            #print("s skip:"  + s[k+1:])
            x = s.find(")", k+1)
            y = s.find("]", k+1)
            z = s.find("}", k+1) 
            #print("3--- xyz "+str(x) + " " + str(y)+ " "+ str(z))
            if (z<x or x==-1) and (z<y or y==-1) and z>k: #{} matched
                local = s[0:k] + s[z+1:]
                s = local
                #print("s : " + s)
            else:
                #print("s : " + s)
                outflag = False
                flag = False
        elif i==-1 and j==-1 and k==-1 and l==-1 and m==-1 and n==-1:
            flag = False
            outflag = True
        else:
            flag = False
            outflag = False

    return outflag

if __name__ == '__main__':

    t = int(input())
    for t_itr in range(t):
        s = input()
        #print("start s :" + s)
        resultflag = isBalanced(s)
        #resultflag = True
        if resultflag:
            result = "YES"
        else:
            result = "NO"
        print(result)
