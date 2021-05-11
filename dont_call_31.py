import random

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
computer_choice = 0
sequence = 0
target_number = 0

for i in range(0 ,9):
    while True:
        a = random.randint(0,8)
        b = random.randint(0,8)
        if a != b:
            break
    change_a = number_list[a]
    change_b = number_list[b]
    number_list[a] = change_b
    number_list[b] = change_a
    # random_number = random.randint(0,8)
    # temp = number_list[random_number]
    #

print("1부터 9까지의 칸에 숫자가 랜덤으로 지정되어 있습니다.")
player_choice = int(input("1~9까지의 수 중 원하시는 숫자를 선택해주세요."))
player_choice = player_choice - 1

while True:
    computer_choice = random.randint(0,8)
    if player_choice != computer_choice:
        break

if number_list[player_choice] > number_list[computer_choice]:
    print("플레이어는", number_list[player_choice], ", 컴퓨터는", number_list[computer_choice], "으로 플레이어의 선공입니다.")
    sequence = 0
else:
    print("플레이어는", number_list[player_choice], ", 컴퓨터는", number_list[computer_choice], "으로 컴퓨터의 선공입니다.")
    sequence = 1

while target_number < 31:
    if sequence == 0:
        number_call = int(input("1~3중 부르실 숫자 갯수를 말해주세요."))
        if number_call == 1:
            print(number_call, "개의 숫자를 불렀습니다.")
            for i in range(0,number_call):
                target_number = target_number + 1
                print(target_number)

        elif number_call == 2:
            print(number_call, "개의 숫자를 불렀습니다.")
            for i in range(0, number_call):
                target_number = target_number + 1
                print(target_number)

        else:
            print(number_call, "개의 숫자를 불렀습니다.")
            for i in range(0, number_call):
                target_number = target_number + 1
                print(target_number)

        sequence = 1
    else:
        number_call = random.randint(1,3)
        if number_call == 1:
            print(number_call, "개의 숫자를 불렀습니다.")
            for i in range(0, number_call):
                target_number = target_number + 1
                print(target_number)

        elif number_call == 2:
            print(number_call, "개의 숫자를 불렀습니다.")
            for i in range(0, number_call):
                target_number = target_number + 1
                print(target_number)

        else:
            print(number_call, "개의 숫자를 불렀습니다.")
            for i in range(0, number_call):
                target_number = target_number + 1
                print(target_number)

        sequence = 0

if sequence == 1:
    print("컴퓨터의 승리입니다.")
else:
    print("플레이어의 승리입니다.")