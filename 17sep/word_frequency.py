with open ('C://Users//Administrator//Desktop//Programming methodology in python//project//17sep//story.txt','r') as f:
    r = f.read().lower()
    s = r.split()
    d = {}
    n = int(input("Enter the threshhold number: "))

    for i in range(len(s)):
        d[s[i]] = d.get(s[i],0)+1

    
    for word in d:
        if d[word] >= n:
            print(word, '-->', d[word])
