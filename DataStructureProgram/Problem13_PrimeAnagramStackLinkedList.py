from DataStructureProgram.Stack import *
s=Stack()
s1 = Stack()


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

for i in range(2,
               1000+1):
    if prime_or_not(i):
        s.push(str(i))


for i in range(s.size()-1):
    for j in range(s.size()):
        if anagram(s.element_at(i),s.element_at(j)) and i != j :
            s1.push(s.element_at(i))
            break

for i in range(s1.size()):
    print(s1.pop(), end=" ")
