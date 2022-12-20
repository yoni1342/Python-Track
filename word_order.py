# Enter your code here. Read input from STDIN. Print output to STDOUT

def word_order():
    s = int(input())
    words = []
    for i in range(s):
        word = input()
        words.append(word) 
    Hash = {}
    for i in range(len(words)):
        if words[i] in Hash:
            Hash[words[i]]+=1
        else:
            Hash[words[i]] = 1
    print(len(Hash))
    for i in Hash:
        print(Hash[i],end=" ")
       
word_order()