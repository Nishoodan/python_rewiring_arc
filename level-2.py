#Count words in a sentence
#"I love Python" → 3

#sentence = str(input("Enter sentence for counting words: ")).split(" ")
#print(sum(1 for i in sentence))

#----------------------------------------------------------------------------------------#


#Sum of digits of a number
#1234 → 10
num1 = int(input("Enter number for adding/summing: "))
summ = 0
l = len(str(num1))
s = str(num1)

for i in range(len(s)):
    summ += int(s[i])
print(summ)




#Remove duplicates from a list
#[1,2,2,3,4,4] → [1,2,3,4]