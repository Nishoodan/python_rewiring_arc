#Count words in a sentence
#"I love Python" → 3

sentence = str(input("Enter sentence for counting words: ")).split(" ")
print(sum(1 for i in sentence))

#----------------------------------------------------------------------------------------#


#Sum of digits of a number
#1234 → 10
num1 = int(input("Enter number for adding/summing: "))

s = str(num1)
summ = 0

for i in range(len(s)):
    summ += int(s[i])
print(summ)




#Remove duplicates from a list
#[1,2,2,3,4,4] → [1,2,3,4]

num2 = set(input("Enter numbers to delete duplicates with comma ',' : "))

garbage = []
main_list = []
for i in num2:
    if i == "," :
        garbage.append(i)
    else:
        main_list.append(i)
garbage = []
print(main_list)
print(garbage)



