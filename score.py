import csv
import re
import gpa_calc

class Score:
    options = {1:"登録済みスコアの確認",2:"スコアの登録",3:"GPAの計算",4:"終了"}
    score_list = ["S","A","B","C","F"]

    def __init__(self,name):
        self.filename = name
        self.gpa = gpa_calc.Gpa_calc(self.filename)

    def menu(self):
        while True:
            print("-------options("+self.filename+")-------")
            for i,j in Score.options.items():
                print(str(i).ljust(3),"|",j.rjust(10))
            print("------------------------------------")
            str1 = input()

            if str1 == "1":
                self.show_score()
            elif str1 == "2":
                self.set_score()
            elif str1 == "3":
                self.gpa.menu()
            elif str1 == "4":
                break
            else:
                print("入力されたオプション番号に誤りがあります")


    def show_score(self):
        print("-----------------------------")
        with open(self.filename,"r") as f:
            reader = csv.reader(f)
            for i in reader:
                print(i)
        print("-----------------------------")

    def set_score(self):
        scores = input("（講義名）:（評価[F-S]）:（単位数）で入力してください（複数のときは半角スペースで区切る）\n")
        scores = scores.split()
        error = list()
        with open(self.filename,"a") as f:
            writer = csv.writer(f)

            for i in scores:
                temp = re.split(r"[:：]",i)
                if len(temp) != 3 or temp[1] not in Score.score_list:
                    error.append(i)
                else:
                    writer.writerow(temp)

        if error != list():
            print("登録エラーがあります")
            for i in error:
                print(error)
