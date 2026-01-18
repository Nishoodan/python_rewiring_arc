##Reverse a string
##Input: "python" → Output: "nohtyp"
word = str(input("Enter text to reverse it: "))
print(word[::-1])
print(word)  

#-------------------------------------------------------------------------------------------------------------#

##Check palindrome
##"madam" → True, "hello" → False
word1 = str(input("Enter word to check weather its palindrome: "))
print(word1 == word1[::-1])

#-------------------------------------------------------------------------------------------------------------#

#Count vowels in a string
#Input: "programming" → Output: 3
word2 = str(input("Enter word to count vowels : "))

#
#list1 = ["a","e","i","o","u","A","E","I","O","U"]
#count = 0
#for i in word2:
#    if i in list1:
#        count = count+1
#
#if count == 0:
#    print("No vowels")
#else:
#    print(count)


#oooooooooooooooooooooooorrrrrrrrrrrrrrrrrrrrrrrrrr

vowels = "aeiouAEIOU"
count = sum(1 for i in word2 if i in vowels)

if count == 0:
    print("No vowels")
else:
    print(count)

#-------------------------------------------------------------------------------------------------------------#

#Find the largest number in a list
#[4, 10, 2, 99, 23] → 99
print(max([4, 10, 2, 99, 23]))

#-------------------------------------------------------------------------------------------------------------#

#FizzBuzz (classic)
#Print numbers 1–100
#Multiple of 3 → "Fizz"
#Multiple of 5 → "Buzz"
#Both → "FizzBuzz"

for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print(i,"FizzBuzz")
    elif i % 3 == 0:
        print(i,"Fizz")
    elif i % 5 == 0:
        print(i,"Buzz")
    else:
        print(i)

#-------------------------------------------------------------------------------------------------------------#



