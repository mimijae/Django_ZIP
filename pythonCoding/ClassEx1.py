# class Unit:
#     def __init__(self,name,hp,damage):
#         self.name=name
#         self.hp = hp
#         self.damage=damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

# marin1=Unit("마린",40,5)
# marin2=Unit("마린",40,5)
# tank=Unit("탱크",150,35)

# wraith1 = Unit("레이스",80,5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# wraith2 = Unit("빼앗은레이스",80,5)
# wraith2.clocking = True

# if wraith2.clocking ==True:
#     print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))

# 공격유닛
# class AttackUnit:
#     def __init__(self, name,hp, damage):
#         self.name=name
#         self.hp=hp
#         self.damage=damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name,location,self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp-=damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
#         if self.hp<=0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")

# firebat1.damaged(25)

# firebat1.damaged(25)

# 상속

class Unit:
    def __init__(self,name,hp,speed):
        self.name=name
        self.hp = hp
        self.speed=speed
    def move(self, location):
        print("[지상유닛]")
        print("{0} : {1} 방향으로 갑니다. [속도 {2}]".format(self.name,location,self.speed))

class AttackUnit(Unit):
    def __init__(self, name,hp, speed,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage=damage

# 날수있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name,location,self.flying_speed))

# 공중 공격 유닛 클래스

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage,flying_speed):
        AttackUnit.__init__(self,name, hp, 0,damage) # 지상 스피드 0
        Flyable.__init__(self,flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


vulture = AttackUnit("벌쳐",80,10,20)
battlecruiser = FlyableAttackUnit("배틀 크루저", 500,25,3)

vulture.move("11시")
battlecruiser.move("9시")

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass

# supply_depot = BuildingUnit("서플라이 디폿",500,"7시")

# def game_start():
#     print("알림 새로운 게임을 시작합니다.")

# def game_over():
#     pass


# game_start()
# game_over()
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name,hp,0)
        self.location=location

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self,"탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.seize_mode ==False:
            print("{0}: 시즈모드로 전환합니다.".format(self.name))
            self.damage*=2
            self.seize_mode=True

        else:
            print("{0}: 시즈모드로 해제합니다.".format(self.name))
            self.damage/=2
            self.seize_mode=False
