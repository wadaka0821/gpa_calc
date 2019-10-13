import csv

class Gpa_calc:
    gpa_evaluate_set = {"1":{"S":4,"A":3,"B":2,"C":1,"F":0},
                        "2":{"S":4,"A":3,"B":2,"C":1},
                        "3":{"S":4.3,"A":4,"B":3,"C":2,"F":0},
                        "4":{"S":5,"A":4,"B":3,"C":2,"F":0}}

    def __init__(self,name):
        self.filename = name
        self.option = "1"
        self.gpas = dict()

    def menu(self):
        while True:
            str1 = input("計算したいオプション番号を入力してください\n")
            if str1 in Gpa_calc.gpa_evaluate_set:
                self.option = str1
                if str1 not in self.gpas:
                    self.calc()
                self.show()
                break
            else:
                print("入力されたオプション番号に誤りがあります")
                continue

    def calc(self):
        temp_gpa = 0
        temp_unit = 0

        with open(self.filename,"r") as f:
            reader = csv.reader(f)
            print(reader)
            for i in reader:
                print(i)
                if i[1] in Gpa_calc.gpa_evaluate_set[self.option]:
                    temp_gpa += Gpa_calc.gpa_evaluate_set[self.option][i[1]]*int(i[2])
                    temp_unit += int(i[2])
        self.gpas.update({self.option:temp_gpa/temp_unit})

    def show(self):
        print("%2f" % self.gpas[self.option])
