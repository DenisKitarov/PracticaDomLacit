"""
#1
list=input().split()
list2=[]
i = 0
x = len(list)
while i < x:
    if list[i].isdigit == True :
      if int(list[i])%2 == 0:
        list2.append(int(symbol))
        x -= 1  
    i+=1 

print(list2)




#2
#print(" ".join(input().split()[::2]))

#3
print(*(i for i in  input().split() if int(i) >= 0))


#4
spis=(map(int, input().split()))

spisSpisok = [[], [], [],[]]
m = int(input())
spisSpisok[0] = [i for i in spisok if i % m == 0]
spisSpisok[1] = [i for i in spisok if i % m == 1]
spisSpisok[2] = [i for i in spisok if i % m == 2]
print(spisSpisok)

#6
spis = [3, 4.1, 2]
#[2, 3, 4.1]
spis.sort()
final = []
a = (spis[0], spis[1])
final.append(a)
b = (spis[1], spis[2])
final.append(b)
c = (spis[0], spis[2])
final.append(c)
print(final) 

#7

list=input().split()
dictionary = { }
i = 0
while i < len(list):
    dictionary[list[i]] = list[i+1]
    i+=2
print(dictionary)
"""