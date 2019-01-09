from DataStructureProgram.Queue import *


def prime_or_not(num):
    for i in reversed((range(2 , int(num/2)+1))):
        if num%i==0:
            return False
    return True


def anagram(val1,val2):
    val1=sorted(val1)
    val2=sorted(val2)
    if val1==val2:
        return True
    else:
        return False


q = Queue()
q1 = Queue()
for i in range(2,1000+1):
    if prime_or_not(i):
        q.enqueue(str(i))

for i in range(q.size()-1):
    for j in range(q.size()):
        if anagram(q.element_at(i),q.element_at(j)) and i!=j :
            q1.enqueue(q.element_at(i))
            break
for i in range(q1.size()):
    print(q1.de_queue(),end=" ")
