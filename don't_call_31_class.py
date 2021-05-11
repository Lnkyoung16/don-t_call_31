import random

class do_not_call_31:
    def __init__(self):
        self.target_number = 0
        self.sequence = 0
        self.number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player_choice = 0
        self.computer_choice = 0
        self.number_call = 0
        self.game_over = 0

    def choose_number_call(self):
        while True:
            number_call = int(input("1~3까지의 숫자 중 하나를 선택하세요."))
            if number_call < 0 or number_call > 3:
                print("3 이하의 0 이상의 수를 불러주세요.")
            else:
                self.number_call = number_call
                break

    def number_call_result(self):
        if self.sequence == 0:
            print("플레이어는", self.number_call, "개의 숫자를 불렀습니다.")
        else:
            print("컴퓨터는", self.number_call, "개의 숫자를 불렀습니다.")
        for i in range(0, self.number_call):
            self.target_number = self.target_number + 1
            print(self.target_number)
            # target number, sequence 가 class 속성정보 사용되어야함

    def call_random_number(self):
        self.number_call = random.randint(1,3)

    def sequence_change(self):
        if self.sequence == 0:
            self.sequence = 1
        else:
            self.sequence = 0

    def player_choose_sequence(self):
        print("1부터 9까지의 칸에 숫자가 랜덤으로 지정되어 있습니다.")
        self.player_choice = int(input("1~9까지의 수 중 원하시는 숫자를 선택해주세요."))
        self.player_choice = self.player_choice - 1

    def computer_choose_sequence(self):
        while True:
            self.computer_choice = random.randint(0, 8)
            if self.player_choice != self.computer_choice:
                break

    def number_comparison(self):
        if self.number_list[self.player_choice] > self.number_list[self.computer_choice]:
            print("플레이어는", self.number_list[self.player_choice], ", 컴퓨터는", self.number_list[self.computer_choice], "으로 플레이어의 선공입니다.")
            self.sequence = 0
        else:
            print("플레이어는", self.number_list[self.player_choice], ", 컴퓨터는", self.number_list[self.computer_choice], "으로 컴퓨터의 선공입니다.")
            self.sequence = 1

    def number_shuffle(self):
        for i in range(0, 9):
            while True:
                a = random.randint(0, 8)
                b = random.randint(0, 8)
                if a != b:
                    break
            change_a = self.number_list[a]
            change_b = self.number_list[b]
            self.number_list[a] = change_b
            self.number_list[b] = change_a

    def win_validator(self):
        if self.target_number > 30:
            self.game_over = 1

    def winner_validator(self):
        if self.sequence == 1:
            print("컴퓨터의 승리")
        else:
            print("플레이어의 승리")

    def game_start(self):
        obj = self
        obj.number_shuffle()
        obj.player_choose_sequence()
        obj.computer_choose_sequence()
        obj.number_comparison()
        while obj.game_over == 0:
            if obj.sequence == 0:
                obj.choose_number_call()
            else:
                obj.call_random_number()
            obj.number_call_result()
            obj.sequence_change()
            obj.win_validator()
        obj.winner_validator()

do_not_call_31().game_start()