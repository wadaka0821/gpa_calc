class Score:
    def __init__(self,name):
        self.filename = name

    def menu(self):
        options = {1:"登録済みスコアの確認",2:"スコアの登録",3:"GPAの計算",4:"終了"}
        while True:
            print("-------options("+self.filename+")-------")
            for i,j in options.items():
                print(str(i).ljust(3),"|",j.rjust(10))
            input()
