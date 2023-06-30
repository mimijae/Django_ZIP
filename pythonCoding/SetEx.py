# # 집합(set)
# # 중복 안됨, 순서없음

# my_set = {1,2,3,3,3}
# print(my_set) # {1, 2, 3}

# java = {"유재석","김태호","양세형"}
# python=set(["유재석","박명수"])

# #교집합(java와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# #합집합 (java 할 수 있거나 python 할수 있는 개발자)
# print(java|python)
# print(java.union(python))

# # 차집합(java 할수 있지만 python은 할 줄 모르는 개발자)
# print(java- python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# # java를 까먹음
# java.remove("김태호")
from random import *
users=range(1,21)
users=list(users)

shuffle(users)

winners = sample(users,4) # 4명을 추출

print("치킨 {0}".format(winners[0]))
print("커피 {0}".format(winners[1:]))