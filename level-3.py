##🔥 Level 3
#
##Check if a number is prime
num1 = int(input("Enter number to check prime number: "))
flag = False

for i in range(2,9):
    if num1 % i == 0:
        flag = True
    else:
        flag = False

if flag == True:
    print("not a prime number")
else:
    print("prime number")
#Find second largest number in a list

num1 = set(input("Enter numbers using comma',': ").split(","))
l =[]
for i in sorted(num1, reverse=True):
    l.append(int(i))
print(l[1])


#Reverse words in a sentence
#"I love Python" → "Python love I"

sentence = input("Enter sentence to reverse it: ").split(" ")

print(" ".join(sentence[::-1]))

