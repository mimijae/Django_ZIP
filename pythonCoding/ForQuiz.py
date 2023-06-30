from random import *

cnt=0 # 총 탑승 승객수 

for i in range(1,51): #1~50 이라는 수 (승객)
    time=randrange(5,51)# 5분에서 50분 시간 소요
    if 5<=time<=15: # 5~15 분 이내 손님 매칭 성공 탑승 승객 수 증가
        print("[0] {0}번째 손님 (소요시간 :{1})".format(i,time))
        cnt+=1
    else: # 매칭 실패
        print("[] {0}번째 손님 (소요시간 :{1})".format(i,time))

print("총 탑승 승객 : {0}".format(cnt))