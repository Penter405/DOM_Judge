result=[]#list -> set -> str
ever=[]
question=""
def recursion(word:list,towalk:int):
    global question
    if str(word) in ever:
        return 0
    ever[-1].add(str(word))
    if towalk>=len(question):
        result[-1].append("".join(word))
        return 0
    #print(word,towalk)
    for rs in range(len(word)):
        #print("for loop")
        #insert here
        word2=word.copy()
        word2.insert(rs,question[towalk])
        recursion(word2,towalk+1)
    word2=word.copy()
    word2.append(question[towalk])
    recursion(word2,towalk+1)
    #append here

while True:
    try:
        question=input()
    except:
        break
    result.append(list())
    ever.append(set())
    recursion([],0)
    #print(result)
bot=-1
#print(result)
for rs in result:
    bot+=1
    if bot!=0:
        print("")
    print("\n".join(rs))

    