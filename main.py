class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.skills = []

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.level += 1
            self.exp = 0
            print("Level UP!")

    def add_skill(self, skill):
        self.skills.append(skill)

    def info(self):
        print(f"{self.name} | Level: {self.level} | EXP: {self.exp}")
        print("Skills:", self.skills)

def run():
    hero = Character("Warrior")

    while True:
        print("\n1. Exp olish\n2. Skill qo‘shish\n3. Info\n4. Chiqish")
        c = input("Tanlang: ")

        if c == "1":
            hero.gain_exp(int(input("EXP: ")))
        elif c == "2":
            hero.add_skill(input("Skill: "))
        elif c == "3":
            hero.info()
        else:
            break

run()
