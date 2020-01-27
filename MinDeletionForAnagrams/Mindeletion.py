

def count_remove(strings, charac):
    count =0
    i = strings.find(charac)
    while(i>=0):
        count = count+1
        strings1 = strings[0:i] + strings[i+1:]
        strings = strings1
        i = strings.find(charac)
    return count

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    sum = 0
    check = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    a = a.lower()
    b = b.lower()
    for i in range(0, len(check)):
        c1 = count_remove(a, check[i])
        c2 = count_remove(b, check[i])
        diff = c1-c2
        sum = sum + abs(diff)
    return sum


if __name__ == '__main__':

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)

