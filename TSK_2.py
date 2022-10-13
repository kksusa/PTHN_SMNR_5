def ReadData(filename):
    with open(filename) as dataStorage:
        input = dataStorage.read()
    return input

def SaveData(text, filename):
    with open(filename, "w", encoding = "utf-8") as dataStorage:
        dataStorage.write(text)
        dataStorage.close()

def RLEdecompress(rle):
    text = ""
    while rle != "":
        rle[0]
        text = text + int(rle[1]) * rle[0]
        rle = rle[2:]
    print("Декомпрессия прошла успешно.")
    return text

def RLEcompress(text):
    output = text
    size1 = len(text)
    rle = ""
    while text != "":
        count = 0
        current = text[0]
        for i in range(len(text)):
            if text[i] == current: count += 1
            else: break
        text = text[count:]
        rle = rle + current + str(count)
    size2 = len(rle)
    print(f"Степень сжатия фразы {output} в виде {rle} составляет {round((size2 / size1 * 100), 2)} %.")
    return rle

rleFile = RLEcompress(ReadData('dataIN.txt'))
SaveData(rleFile, 'rle.txt')
textFile = RLEdecompress(rleFile)
SaveData(textFile, 'dataOUT.txt')