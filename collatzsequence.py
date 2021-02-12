def collatzsequence(maxvalue):
    oldlistofn = [1]
    ivalue = 1
    for i in range(1,maxvalue+1,2):
        n = i
        newlistofn = [i]
        while n > 1:
            if n%2 == 0:
                n = int(n/2)
                newlistofn.append(n)
            else:
                n = (3*n) + 1
                newlistofn.append(n)
        if len(newlistofn) > len(oldlistofn):
            oldlistofn = newlistofn
            ivalue = i
    print("A starting value of " + str(ivalue) + " has a chain length of " + str(len(oldlistofn)) + " terms.")

collatzsequence(40)