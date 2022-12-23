import os.path

def add_cont(text, name_file):
    if os.path.isfile(name_file):
        text_spl = text.split()
        with open(name_file, "ta") as file:
            n = 1
            for txt in text_spl:
                if n % 3 == 0:
                    file.write(txt + "; \n")
                else:
                    file.write(txt + " ")
                n += 1
    else:
        y_or_n = input("Такого файла не существует. Введите y если хотите создать")
        if y_or_n == "y":
            open(name_file, 'tw')
        add_cont(text, name_file)
def output_cont(name_file):
    choise = int(input("Введите 1 что бы вывести все значени в строчку с разделителем * и ** \n или введите любое другое значение что бы вывести построчно"))
    with open(name_file, "tr") as file:
        if choise == 1:
            f = file.read()
            f = f.replace('\n', '')
            f = f.replace(';', '**')
            f = f.replace(' ', '*')
            print(f)
        else:
            print(file.read())

def  repl_cont(name_rep_cont, name_file, repl):
    with open(name_file, 'r+') as file:
        f = file.read()
    with open(name_file, 'w') as file:
        file.write(str(f).replace(name_rep_cont, repl))

def delete_cont(name_dell_cont, name_file):
    with open(name_file, 'r+') as file:
        lines = file.readlines()
        f = file.read()
        for line in lines:
            if line.find(name_dell_cont) != -1:
                del_line = line
        if bool(del_line):
            print(del_line)
            with open(name_file, 'w') as file:
                file.write(str(f).replace(del_line, ''))
        else:
            print("Такого контакта не существует")
key = True
while key:
    key = int(input("1 - Добавить контакт(-ы);\n2 - Вывести контакты\n3 - Редактировать контакт\n4(не работает) - удалить контакт\n0 - выйти\n"))
    os.system('cls')
    match key:
        case 1:
            text = input("Введите контакт(-ы)")
            name_file = input("Введите название файла")
            add_cont(text, name_file)
        case 2:
            name_file = input("Введите название файла")
            output_cont(name_file)
        case 3:
            text = input("Введите старое значение контакт")
            new_text = input("Введите новое значение контакт")
            name_file = input("Введите название файла")
            repl_cont(text, name_file, new_text)
        case 4:
            text = input("Введите удаляемый контакт")
            name_file = input("Введите название файла")
            delete_cont(text, name_file)



