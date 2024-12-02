from character import Hero, Monster
from battle import Battle

def main():
    print("게임 시작")
    name = input("이름 입력:")
    role = input("직업 입력(전사/마법사/궁수)")
    hero = Hero(name,100,20,5,speed=12,role=role)
    print(hero)

    monster_pool = [
        Goblin(name: "고블린", hp: 50, speed: 10, attack: 10, defence: 2 )
        Goblin(name: "고블린", hp: 50, speed: 10, attack: 10, defence: 2 )
        Goblin(name: "고블린", hp: 50, speed: 10, attack: 10, defence: 2 )#더 적어야함
    ]
    battle = Battle()
    while hero.is_alive():
        monster = random.choice(monster_pool)
        print(f"\n  몬스터 {monster} 등장")
        print(monster.description())


    monster = Monster("고블린",30,10,2,speed=10, level=1)
    print(monster)
    battle = Battle()
    for i in range(5):
        battle.fight(hero,monster)
        monster.level_up()

    print(hero)

if __name__ == '__main__':
    main()