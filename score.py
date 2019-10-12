import csv

class Score:
    def __init__(self,name):
        self.filename = name

    def menu(self):
        options = {1:"登録済みスコアの確認",2:"スコアの登録",3:"GPAの計算",4:"終了"}
        while True:
            print("-------options("+self.filename+")-------")
            for i,j in options.items():
                print(str(i).ljust(3),"|",j.rjust(10))
            print("------------------------------------")
            str1 = input()

            if str1 == "1":
                self.show_score()

    def show_score(self):
        with open(self.filename,"rw") as f:
            reader = csv.reader(f)
            for i in reader:
                print(i)
