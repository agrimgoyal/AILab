import time as tm
start = tm.time()
f = open('file.txt','r')
i = 0
dic = {}
for x in f:
    x = x.strip()
    x = x.lower()
    words = x.split(' ')
    for word in words:
        if word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1
print(dic)
end = tm.time()
print(end - start)