class testdict():
    testpost = {'userid':123,'Name':'Raghul','Practice':'Testing'}
    print("Original Dictionary: ", testpost)

    if "Practice" in testpost:
        del testpost["Practice"]
        print("Updated Dictionary: ", testpost)

if __name__ == '__main__':
    testdict()
