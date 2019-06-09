nterms = 10
n1 = 0
n2 = 1
count = 0
if nterms < 0:
    print("Please enter the positive integer")
elif nterms == 1:
    print("Please enter fibinocci numbers", nterms,":")
    print(n1)
else:
    print("Please enter fibinocci numbers", nterms,":")
    while count < nterms:
        print(n1,end="")
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1
