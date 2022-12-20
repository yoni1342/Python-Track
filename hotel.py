from collections import Counter
def Hotel():
    k = int(input())
    roomNum = input().split(" ")
    Hash = Counter(roomNum)
    for i in Hash:
        if Hash[i] != k:
            print(i)
            break
Hotel()