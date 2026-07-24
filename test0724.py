print("==== Linux ====")
print("==== 퀴즈 시작 =====")
print("==== end 버튼 0 ====")

import random as r

num_list = []
num_list2 = ["pwd", "date", "rm", "clear", "whoami"]

num_list.append("현재 작업중인 폴더의 경로를 출력하는 리눅스 명령어의 옳은 명칭은?")
num_list.append("현재 시간을 출력하는 명령어는?")
num_list.append("파일 또는 디렉터리를 삭제시키는 명령어는?")
num_list.append("터미널 화면을 지울 수 있게 해주는 명령어?")
num_list.append("현재 사용자 확인을 시켜주는 명령어는?")

while True:
    ok = 0          # 진행한 문제 수
    kor = 0         # 맞춘 문제 수
    quiz = r.sample(range(5), 3)

    while True:

        if ok == len(quiz):
            print("퀴즈 종료!")
            if kor == 3:
                print("등급 : A")
                print("모든 문제를 다 맞추셨습니다!")
            elif kor == 2:
                print("등급 : B")
                print("2문제 맞추셨습니다.")
            elif kor == 1:
                print("등급 : C")
                print("1문제 맞추셨습니다.")
            else:
                print("등급 : F")
                print("모든 문제를 틀리셨습니다.")
            break
        print(ok + 1, ".", num_list[quiz[ok]])
        print()
        i = input("문제의 정답은 : ")
        if i == "0":
            print("프로그램을 종료합니다.")
            exit()
        if i.lower() == num_list2[quiz[ok]]:
            print("정답")
            kor += 1
        else:
