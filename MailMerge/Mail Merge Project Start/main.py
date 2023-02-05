PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    #read就是read整個檔案

with open("./Input/Letters/starting_letter.txt") as letters_file:
    letter_contents = letters_file.read()
    #先拿到整個檔案的文字
    #再去跑回圈，把[name]替換成
    for name in names_file:
        letter_contents.replace(PLACEHOLDER, name.strip())
        #替換好之後就等於一封信寫好了，可以存入資料夾了
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}",mode="w") as completed_letter:
            completed_letter.write(letter_contents)
            #在這個被打開的文件中寫入letter content就ok囉!
