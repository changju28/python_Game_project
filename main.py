import engine

if __name__ == '__main__':
    engine.menu()
    mode = engine.level
    number_of_computer = engine.number_computer
    computer_arr = engine.arr_computer(number_of_computer)
    while True:
        try:
            print()
            player_num = int(input('숫자를 입력하세요: '))
            if player_num <= 3:
                result_1 = engine.player(player_num)
                if result_1:
                    print(result_1)
                    break
                result_2 = engine.computer(mode, number_of_computer)
                if result_2:
                    number_of_computer -= 1
                    if number_of_computer <= 0:
                        print(result_2)
                        break
            else:
                print('1~3 까지 숫자만 입력하세요.')
        except ValueError:
            print('잘못 입력 했습니다.')

