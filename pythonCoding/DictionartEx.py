cabinet = {3:"유재석",100:"김태호"}
print(cabinet[3])
# 대괄호를 써서 키의 값을 가져올때는 키가 없을때는 오류가발생하여 프로그램을 강제종료한다
print(cabinet.get(3))
# 하지만 get을 쓰면 프로그램을 강제종료시키지않고 None을 출력한다

print(cabinet.get(3,"사용가능"))

print(3 in cabinet) # True

# 새 손님
cabinet["c-20"]="조세호"

# 간 손님(삭제)
del cabinet["유재석"]

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

#모든값 삭제
cabinet.clear()

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

(name,age,hobby) = ("김종국", 20, "코딩")
print(name,age,hobby)