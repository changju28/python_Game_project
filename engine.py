import random


num = 0 # 진행 번호
level = 'Easy' # 난이도 기본값 Easy
victory_num = [2, 6, 10, 14, 18, 22, 26, 30] # 승리 번호 리스트
number_computer = 1 # 컴퓨터 수

# 게임시작 메뉴 함수
def menu():
    print()
    try:
        menu_choice = int(input('게임 시작 (1) \n게임 설명 (2)\n게임 난이도 설정 (3)\n컴퓨터 수 설정 (4)\n:'))
        if menu_choice == 1:
            print('게임시작!')
        elif menu_choice == 2:
            menual()
        elif menu_choice == 3:
            game_level()
        elif menu_choice == 4:
            number_of_computer()
        else:
            print('잘못 입력 하였습니다.')

    except ValueError:
        print('잘못 입력 하였습니다.')


# 게임설명 함수
def menual(again=1):
    if again == 1:
        print('1부터 31 까지의 번호를 오름차순으로 각자 순서대로 부르는 게임')
        print('플레이어는 한차례에 3개 까지 숫자를 부를 수 있다.')
        print('설정 메뉴에서 컴퓨터 수 와 난이도를 설정 할 수 있다.')
    try:
        back_menu = int(input('뒤로가기 (1)'))
        if back_menu == 1:
            menu()
        else:
            print('잘못 입력 했습니다.')
            menual(2)
    except ValueError:
        print('잘못 입력 하였습니다.')
        menual(2)


# 게임난이도 설정 함수
def game_level():
    global level
    print('현재: {}'.format(level))

    level_num = int(input('Easy (1)\nHard (2)\n:'))
    if level_num == 1:
        level = 'Easy'
    elif level_num == 2:
        level = 'Hard'
    menu()


# 컴퓨터 수 설정 함수
def number_of_computer(again=1):
    global number_computer

    if again == 1:
        print('현재 컴퓨터 갯수: {}'.format(number_computer))

    try:
        number = int(input('컴퓨터 수 입력(최대 3): '))

        if number < 1:
            print('컴퓨터 갯수를 0이하로 설정할 수 없습니다.')
            number_of_computer(2)
        elif number > 3:
            print('컴퓨터 최대 갯수는 3 입니다.')
            number_of_computer(2)
        else:
            number_computer = number
            menu()

    except ValueError:
        print('잘못 입력 되었습니다.')
        number_of_computer(2)


# 사용자 게임 진행 함수
def player(n):
    global num
    for i in range(n):
        num += 1
        result = num_print(i, n, 'computer')
        if result:
            return result


# 컴퓨터명 생성 함수
def arr_computer(number_computer):
    arr = []
    for i in range(number_computer):
        arr.append(i+1)
    return arr

# 난이도 별 컴퓨터 진행 함수
def computer(level, number_of_computer):
    global num

    # 이지모드
    if level == 'Easy':
        for i in range(number_of_computer):
            random_num = random.randint(1, 3)
            print('컴퓨터({}) 차례'.format(i+1))
            for j in range(random_num):
                num += 1
                result = num_print(j, random_num, 'player')
                if result:
                    print()
                    print('컴퓨터({}) 탈락!'.format(i+1))
                    num = 0
                    return result
    # 하드모드
    elif level == 'Hard':
        for i in range(number_of_computer):
            target_num = find_target_num()
            random_num = random.randint(1, 3)
            print('컴퓨터({}) 차례'.format(i + 1))
            if target_num == num:
                    for j in range(random_num):
                        num += 1
                        result = num_print(j, random_num, 'player')
                        if result:
                            print()
                            print('컴퓨터({}) 탈락!'.format(i + 1))
                            num = 0
                            return result

            else:
                target = target_num - num
                for i in range(target):
                    num += 1
                    result = num_print(i, target, 'player')
                    if result:
                        print()
                        print('컴퓨터({}) 탈락!'.format(i + 1))
                        num = 0
                        return result


# 승리 공식 숫자를 찾는 함수
def find_target_num():
    target_num = 0
    for i in victory_num:
        if num <= i:
            target_num = i
            break
    return target_num


# 출력 함수
def num_print(start, end, winner):
    if num >= 31:
        print(num)
        return '{} 승리!!'.format(winner)
    else:
        if start == end - 1:
            print(num)
        else:
            print(num, end=', ')
