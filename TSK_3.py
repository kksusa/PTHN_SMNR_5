text = input("Введите текст: ")
if "абв" in text.lower():
    i = 0
    while i <= len(text) and "абв" in text.lower():
        if text[i:i+3].lower() == "абв":
            text = text[:i] + text[(i + 3):]
            i = 0
        else: i += 1
    print(f'Текст после удаления связки "абв": {text}')
else: print('В Вашем тексте нет связки "абв" с учётом всех регистров.')