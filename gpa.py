import re
import  score.Score as Score

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
            str1 = input("追加したいファイル名を入力してください(csv形式)\n")
            find = re.search(r".+\.csv",str1)
            if find:
                filename.append([str1,Score(str1)])
                break
            else:
                print("ファイル名に誤りがあります")
    elif str1 == "2":
        str1 = input("削除したいファイルのインデックスを入力してください(複数の場合は半角スペース区切り)\n")
        str1 = sorted(str1.split(),reverse=True)
        for i in str1:
            try:
                del filename[int(i)-1]
            except:
                print("入力されたインデックスに誤りがあります")
    elif str1 == "3":
        str1 = input("操作したいファイルのインデックスを入力してください\n")
        try:
            filename[int(str1)-1][1].menu()
        except:
            print("入力されたインデックスに誤りがあります")
    elif str1 == "4":
        break
    else:
        print("入力されたオプション番号に誤りがあります")
