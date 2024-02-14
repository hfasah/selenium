#!/usr/bin/python3
file = open('topics.txt', 'r')
answer =file.readlines()
print((answer))
file.close()

myfile = open('myfile.txt', 'w')
for i in range (1,len(answer)):
      myfile.write(f'{i} {answer[i]}')
myfile.close()