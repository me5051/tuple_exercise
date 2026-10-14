# # name = "John Doe"
# # print ("Welcome, " + name + "!")
# # def print_lyrics():
# #     print("i'm a lumberjack, and I'm okay")
# #     print("I sleep all night and I work all day")    

# # print_lyrics()

# # def repeat_lyrics():
# #     print_lyrics()
# #     print_lyrics()

# # repeat_lyrics()

# # import math
# # r = 5
# # vol = (4/3) * math.pi * r**3
# # print("Volume:", vol)

# # cover_price = 24.95
# # discount = 40 / 100
# # shipping_first = 3
# # shipping_additional = 0.75
# # total_books = 60

# # wholesale_price = cover_price * (1 - discount)
# # book_cost = wholesale_price * total_books
# # shipping_cost = shipping_first + (shipping_additional * (total_books - 1))

# # total_cost = book_cost + shipping_cost
# # print("Total Cost:", total_cost)

# # start_hour = 6
# # start_minute = 52

# # easy = 8 * 60 + 15
# # tempo = 7 * 60 + 12

# # tempo_time = easy + (3 * tempo) + easy
# # total_minutes =  start_minute + (tempo_time // 60)
# # hour = start_hour + (total_minutes // 60)
# # minute = total_minutes % 60
# # print("get home by:", hour, ":", minute)




# # def print_twice(bruce):
# #     print(bruce)
# #     print(bruce)

# # print_twice("Mama")

# # def cat_twice(part1, part2):
# #     cat = part1 + part2
# #     print_twice(cat)

# # line1 = "mama mi "
# # line2 = "mama di."
# # cat_twice(line1,line2)


# # def right_justify(s):
# #     spaces = 70 - len(s)
# #     print(" " * spaces + s)
    
# # right_justify("monty")

# # def do_twice(f):
# #     f()
# #     f()
    
# # def print_spam():
# #     print("spam")
    
# # do_twice(print_spam)

# # def do_twice(f, maga):
# #     f(maga)
# #     f(maga)
    
# # def print_spam(maga):
# #     print(maga)
    
# # do_twice(print_spam, "maga")


# # def do_twice(f, mage):
# #     f(mage)
# #     f(mage)
    
# # def print_twice(bruce):
# #     print(bruce)
# #     print(bruce)
    
# # do_twice(print_twice, "mage")

# # def do_twice(f, mame):
# #     f(mame)
# #     f(mame)
    
# # def print_twice(bruce):
# #     print(bruce)
# #     print(bruce)
   
# # def do_four(f, mame):
# #     do_twice(f, mame)
# #     do_twice(f, mame)
    
# # do_four(print_twice, "mame") 

# # def print_grid():
# #     print("+ - - - - + - - - - +")
# #     print("|         |             |")
# #     print("|         |             |")
# #     print("|        -------------  |")
# #     print("|           ~     ~     |")
# #     print("|       |  ---   ---    |")
# #     print("|       |      >        |")
# #     print("|       |               |")
# #     print("+ - - - - + - - - - - - +")
# #     print("|         me         |")
# #     print("|         |         |")
# #     print("+ - - - - + - - - - +")
    
# # print_grid()

# # def do_twice(f, mave):
# #     f(mave)
# #     f(mave)

# # def do_four(f, mave):
# #     do_twice(f, mave)
# #     do_twice(f, mave)
    
# # def print_row(mave):
# #     print(mave)                             ##grid
    
# # def print_grid(mave):
# #     print("+ - - - - + - - - - +")
# #     do_four(print_row, "|         |         |")
# #     print("+ - - - - + - - - - +")
# #     do_four(print_row, "|         |         |")
# #     print("+ - - - - + - - - - +")
# #     do_four(print_row, "|         |         |")
    
# # print_grid(None)

# # a = 44
# # b = 23

# # def is_greater(a, b):
# #     print(a > b)
# # is_greater(23, 44)

# # def gert(rum, b):
# #     print(rum // b)
# #     print(rum % b)
# #     print(b // rum)
# #     print(b % rum)
# # gert(33, 44)

# # def countdown(n):               ## recursion #
# #     if n<= 0:
# #         print("blastoff:")
# #     else:
# #        print(n)
# #        countdown(n-1)
       
# # countdown(5) 

# # ## EVEN ODD CHECKER
# # num = int(input("Enter a number: "))
# # def is_even(n):
# #     if n % 2 == 0:
# #         print("True")
# #     else:
# #         print("False")
# # is_even(num)       

# # ##  VOTING
# # age = int(input("Enter your age: "))
# # def age_vote(age):
# #     if age >= 18:
# #         print("eligible to vote")
# #     else:
# #         print("not eligible to vote")
# # age_vote(age)

# ## GRADE CHECKER
# # marks = int(input("Enter your marks: "))
# # def check_marks(score):
# #     if score >= 70:
# #         print("A")
# #     elif score >= 60:
# #         print("B")
# #     elif score >= 50:
# #         print("C")
# #     elif score >= 45:
# #         print("D")
# #     elif score < 45:
# #         print("F")
# # check_marks(marks)    

# ## LOGIC OP
# # age = int(input("Enter your age: "))
# # income = int(input("Enter your income: "))
# # def loan_checks(age, income):
# #     if age >= 21 and income >= 50000:
# #         print("eligible for loan")
# #     else:
# #         print("not eligible for loan")

# # loan_checks(age, income)

# ## PASSWORD CHECKER
# # password = input("Enter your password: ")
# # def check_password(password):
# #     if len(password) >= 8 and any(char.isdigit() for char in password):
# #         print("Strong password")
# #     else:
# #         print("Weak password")
# # check_password(password)

# # name = "tgat"
# # print( name [1]) 

# # index = 0
# # while index < len(name):
# #     letter = name[index]
# #     print(letter)
# #     index = index + 2
    
# # for letter in name:
# #     print(letter)
    
# # prefixes = "JKLMNOPQ"
# # suffix = "ack"

# # for letter in prefixes:
# #     print(letter + suffix)

# # a = "Monty Python"
# # print(a[4:12])

# # word = "banana"
# # letter = "n"

# # def find(word, letter):
# #     index = 0
# #     while index < len(word):
# #         if word[index] == letter:
# #             return index
# #         index = index + 1
# #     return -1

# # d = (find(word, letter))
# # print(d)

# # word = "banana"
# # word = word.upper()
# # print(word)


# # def f_m_s(str1):
# #     first = str1[0]
# #     middle = str1[len(str1) //2]
# #     last = str1[-1]
# #     print(first + middle + last)
# # str1 = "JAMES"
# # f_m_s(str1)

# # str2 = "JhonDipPeta"
# # first = str2[4]
# # middle = str2[len(str2) //2]
# # last = str2[6]
# # print(first + middle + last)

# # str3 = "JaSonAy"
# # first = str3[2]
# # middle = str3[len(str3) //2]
# # last = str3[4]
# # print(first + middle + last)

# # s1 = "Ault"
# # s2 = "Kelly"
# # s3 = s1[0:2] + s2 + s1[2:4]
# # print(s3)

# # s1 = "America"
# # s2 = "Japan"
# # s3 = s1[0] + s2[0] + s1[3] + s2[2:5]
# # print(s3)

# # word = "tutor joes"
# # word = word.upper()
# # print(word)

# # word = "tutor joes"
# # word = word.lower()
# # print(word)



# list1 = ["M", "na", "i", "Ke"]
# # for i in list1:
# #     print(i)
# list1[1]= 6
# print(list1)

# list1[2]= "is"
# print(list1)

# def lst():
#     list2 = [20, 30, 40, 50, 60]
#     total = 0
#     for num in list2:
#         total += num
#     print(total)
# lst()

# def lst2():
#     list1 = ["m", "na", "i", "me"]
#     res = []
#     for s in list1:
#         res.append(s.capitalize())
#     print(res)
# lst2()

# def lst3():
#     list1 = ["M", "na", "i", "me"]
#     res = []
#     for s in list1:
#         res.append(s.islower())
#     return res          
# print(lst3())


def lst2():
    list1 = ["m", "na", "i", "me"]
    res = []
    for s in list1:
     res.append(s.capitalize())
    print(res)
lst2()




    
