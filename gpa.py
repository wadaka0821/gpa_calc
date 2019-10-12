import re

filename = list()
options = {1:"ファイルの追加",2:"ファイルの削除",3:"ファイル操作",4:"終了"}
while True:
    print("-----------working space-----------")
    if filename == list():
        print("Nothing")
    for i,j in enumerate(filename,1):
        print(str(i).ljust(3),"|",j)
    print("--------------options--------------")
    for i,j in options.items():
        print(str(i).ljust(3),"|",j.center(15))
    print("-----------------------------------")

    str1 = input()
    if str1 == "1":
        while True:
            str1 = input("追加したいファイル名を入力してください(csv形式)")
            find = re.search(r".+\.csv",str1)
            if find:
                filename.append(str1)
                break
            else:
                print("ファイル名に誤りがあります")
