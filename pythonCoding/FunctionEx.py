# def open_account():
#     print("새로운 계좌가 생성되었습니다")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance+money))
#     return balance+money

# def withdraw(balance, money):
#     if balance >=money:
#         print("츨금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance-money))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다 잔액은 {0} 입니다".format(balance))
#         return balance
    
# def withdraw_night(balance, money):
#     commssion=100
#     print("{0}".format(balance-money-commssion))
#     return commssion, balance-money-commssion


# balance =0
# balance = deposit(balance,1000)
# # balance = withdraw(balance,2000)
# # balance = withdraw(balance,500)

# commssion, balance=withdraw_night(balance,500)
# print(commssion, balance)


# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t 나이: {1} \t 사용언어: {2}".format(name,age,main_lang))

# profile("유재석")

# def profile2(name, age, main_lang):
#     print("이름 : {0}\t 나이: {1} \t 사용언어: {2}".format(name,age,main_lang))

# profile(name="유재석",age=17,main_lang="파이썬")
# profile(age=17,name="유재석",main_lang="파이썬")

# # 가변인자
# def profile3(name, age, *language):
#     print("이름 : {0}\t 나이: {1} \t ".format(name,age), end=" ")
#     for lang in language:
#         print(lang,end=" ")
#     print()

# profile3("유재석", 20, "Python", "Java", "C", "C++","C#","JavaScript")

# profile3("김태호",25,"Kotlin","Swift")

def std_weight(height,gender):
    if gender == "남자":
        return height*height*22
    elif gender == "여자":
         return height*height*21

height = 175
gender="남자"
weight=round(std_weight(height/100,gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다".format(height,gender,weight))