url = "http://naver.com"

python = url.replace("http://","") # 규칙1

python = python[0:python.index(".")] # 규칙2

password = "{}{}{}!".format(python[0:3], len(python), python.count("e")) #규칙3

print("{0}의 생성된 비밀번호는 {1} ".format(url,password))