# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_no))

# # 대기번호 : 0
# # 대기번호 : 1
# # 대기번호 : 2
# # 대기번호 : 3
# # 대기번호 : 4

# for waiting_no in range(5):
#     print("대기번호 : {0}".format(waiting_no))

# # 대기번호 : 0
# # 대기번호 : 1
# # 대기번호 : 2
# # 대기번호 : 3
# # 대기번호 : 4

# for waiting_no in range(1,6):
#     print("대기번호 : {0}".format(waiting_no))

# # 대기번호 : 1
# # 대기번호 : 2
# # 대기번호 : 3
# # 대기번호 : 4
# # 대기번호 : 5

# starbucks = ["아이언맨","토르","그루트"]

# for customer in starbucks:
#     print("{0} 커피 준비됐습니다".format(customer))

# customer ="토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person=input("이름이 어떻게되세요?")

# absent = [2,5] # 결석
# ni_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue # continue는 아래 코드들을 실행시키지 않고 다음 반복으로 계속 진행함
#     elif student in ni_book:
#         print("오늘 수업 여기까지 {0}는 교무실로 따라와".format(student))
#         break # 바로 반복문을 끝냄
#     print("{0} 책을 읽어봐".format(student))

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101,102,103,104
students=[1,2,3,4]
students= [i+100 for i in students]
print(students)

#학생 이름을 길이로 변환
students=["Iron man","Thor","I am groot"]

students=[len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students=["Iron man","Thor","I am groot"]
students=[i.upper() for i in students]
print(students)