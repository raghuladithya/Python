a = [10,20,10,40,50,50,30]
def remove(duplicates):
    finallist = []
    for num in duplicates:
        if num not in finallist:
            finallist.append(num)
    return finallist
a.sort()
print(remove(a))
