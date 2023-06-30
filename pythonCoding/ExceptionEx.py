
try:
    print("나누기 전용 계산기입니다")
    nums=[]
    nums.append(int(input("첫 번재 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))  
    nums.append(int(nums[0]/nums[1]))
    print("{0}/{1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("잘못된 입력입니다")
except ZeroDivisionError as arr:
    print(arr)
except Exception as err:
    print(err)

# 사용자정의 예외처리
class BigNumberError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

# 에러 발생시키기
try:
    print("나누기 전용 계산기입니다")
    nums=[]
    nums.append(int(input("첫 번재 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))  
    nums.append(int(nums[0]/nums[1]))
    if nums[0] >= 10 or nums[1] >= 10:
        raise BigNumberError("{0} {1}".format(nums[0],nums[1]))
    print("{0}/{1} = {2}".format(nums[0],nums[1],nums[2]))   
except ValueError:
    print("잘못된 입력입니다") 
except BigNumberError as arr:
    print("잘못된 입력입니다")
    print(arr)
finally:
    print("계산이 완료되었습니다") # 무조건 실행되는 문장

