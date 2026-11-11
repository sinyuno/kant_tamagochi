# 펫 한마리를 표현하는 클래스

import random

class Pet:
    #클래스 변수
    count = 0   # 지금까지 입양한 펫 수를 기록

    def __init__(self, name):
        self.name = name    # 이름
        self.hunger = 30    # 배고픔 (0 ~ 100)
        self.happy = 70     # 행복도 (0 ~ 100)
        self.energy = 70    # 에너지 (0 ~ 100)
        self.alive = True
        Pet.count += 1

    def __str__(self):
        state = self.mood() if self.alive else "떠남"
        return (f"{self.name} {state}\n"
                f" 배고픔: {self.bar(self.hunger)} {self.hunger:>3}\n"
                f" 행복도: {self.bar(self.happy)} {self.happy:>3}\n"
                f" 에너지: {self.bar(self.energy)} {self.energy:>3}\n")

    def mood(self):
        if self.hunger >= 80 or self.happy <= 20: return "😭"
        if self.happy >= 70 and self.hunger <= 40: return "😁"
        return "😑"

    def bar(self, value):
        # 0 ~ 100 값을 10칸의 막대로 변환
        filled = value // 10
        return "*" * filled + "-" * (10 - filled)
    
    # 공통 메서드
    def _clamp(self, value):
        # 값의 범위를 (0 ~ 100) 유지
        if (value < 0): return 0
        if (value > 100): return 100
        return value

    def _change(self, hunger=0, happy=0, energy=0):
        # 상태값은 반드시 이 메서드를 사용한다.
        self.hunger = self._clamp(self.hunger + hunger)
        self.happy = self._clamp(self.happy + happy)
        self.energy = self._clamp(self.energy + energy)

    # 밥주기
    def feed(self):
        if self.hunger <= 10:
            print(f"{self.name}: 배불러요~")
            return False
        self._change(hunger=-30, happy=5)
        print(f"{self.name}에게 밥을 줬습니다. 냠냠!!")

    # 놀아주기
    def play(self):
        if self.energy < 20:
            print(f"{self.name}: 너무 피곤해요...")
            return False
        self._change(hunger=10, happy=25, energy=-20)
        print(f"{self.name}와 신나게 놀았습니다.")
        return True
    # 잠자기
    def sleep(self):
        self._change(hunger=5, energy=40)
        print(f"{self.name}가 잠들었어요. zZ")
        return True

    # 시간 경과
    def pass_time(self):
        # 하루 지날때 마다 상태값 자연 감소
        self._change(hunger=10, happy=-10, energy=-5)
        # 즐거운 이벤트를 확율계산 (20%)
        if (random.randint(1,5) == 1):
            self._change(happy=15)
            print(f"{self.name} 숨겨진 장난감을 찾았어요.")

        if self.hunger >= 100 or self.happy <= 0:
            self.alive = False


# ------ 테스트 코드 -------
choco = Pet("초코")
dubu = Pet("두부")

print("입양한 펫 수:", Pet.count)

day = 1

while choco.alive:
    choco.pass_time()
    print(f"{day}일차 : 배고픔 {choco.hunger}, 행복도 {choco.happy}")
    day += 1

print(choco)