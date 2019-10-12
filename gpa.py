import re

def check_filename(name):
    find = re.search(r".+\.csv",name)
    if find:
        return True
    else:
        return False

filename = list()
options = ["ファイルの追加","ファイルの削除","ファイル操作","終了"]
while True:
    print("-----------working space-----------")
    if filename == list():
        print("Nothing")
    for i,j in enumerate(filename,1):
        print(str(i).ljust(3),"|",j)
    print("--------------options--------------")
    for i,j in enumerate(options,1):
        print(str(i).ljust(3),"|",j.center(15))
    input()
