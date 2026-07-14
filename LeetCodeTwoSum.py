lis = [1,2,3,4,5,6,7,8,9]
target = int(input("Enter your target sum: "))
answerLis = []
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if (lis[i] + lis[j]) == target:
            answerLis.append(i)
            answerLis.append(j)
            answerLis.append("and")
            break
print(answerLis)