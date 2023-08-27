# origin file name&source
originFile = input("Input origin file source:")

# open file
fileReader = open(originFile, 'r', encoding='utf-8')

# split file
newName = ''
newSource = input("Input new file source:")

'''
Default
读取每一行内容，将其放入新的txt文件中，并按数字顺序命名文件
每行开头都有数字和顿号，因此以顿号为切片分割位置
'''
while True:
    eachLine = fileReader.readline()
    if not eachLine:
        break
    number = eachLine.split("、")[0]
    newName = newSource + number + ".txt"

    if '0' <= eachLine[0] <= '9':
        with open(newName, "w") as newfile:
            newfile.write(eachLine.split('、')[-1])
fileReader.close()