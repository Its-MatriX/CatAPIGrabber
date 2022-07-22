import requests, json, colorama, threading
from os.path import split, sep
from os import name, system
from time import sleep

clear = lambda: system('cls') if name == 'nt' else 'cllear'

folder = str(split(__file__)[0])

clear()

while True:

    print(f'{colorama.Fore.GREEN}Что вы хотите выкачать?')
    print(f'1 - {colorama.Fore.YELLOW}CatAPi')
    print(f'{colorama.Fore.GREEN}2 - {colorama.Fore.YELLOW}DogAPi')

    selection = input(
        f'{colorama.Fore.GREEN}[{colorama.Fore.YELLOW}>{colorama.Fore.GREEN}] '
    )

    if selection == '1':
        ApiAPI = "https://api.thecatapi.com/v1/images/search"
        break
    elif selection == '2':
        ApiAPI = "https://api.thedogapi.com/v1/images/search"
        break
    else:
        print('Некорректный выбор!')

fname = 'cat_urls.txt' if selection == '1' else 'dog_urls.txt'

index = 1

downloaded = []

def Loop(threadID):
    print(colorama.Fore.YELLOW +
            f'Поток №{threadID} запущен' +
            colorama.Fore.WHITE)
    sleep(2)
    global index, file
    while True:
        try:
            ReturnJSON = requests.get(ApiAPI, timeout=3).text
            Json = json.loads(ReturnJSON)

            Image = Json[0]["url"]

            if Image in downloaded:
                print(colorama.Fore.RED +
                      f'Не удалось добавить: {Image} уже есть в этом списке!' +
                      colorama.Fore.WHITE)
                continue

            if 'https://' not in Image and 'http://' not in Image:
                print(colorama.Fore.RED +
                    f'Не удалось добавить: {Image} не содержит http(s)!' +
                    colorama.Fore.WHITE)
                continue

            extension = Image.split('.')[-1]

            if extension not in ['jpg', 'png', 'gif']:
                print(colorama.Fore.RED +
                    f'Не удалось добавить: {Image} не содержит требуемого расширения!' +
                    colorama.Fore.WHITE)
                continue

            file = open(folder + sep + fname, 'a')
            file.write(Image + '\n')
            file.close()

            downloaded.append(Image)

            print(colorama.Fore.GREEN +
                  f'[{index}] Записано успешно: {Image} добавлен!' +
                  colorama.Fore.WHITE)

            index += 1
        except:
            print(colorama.Fore.RED +
                  f'Не удалось записать: {Image} - неизвестная ошибка!' +
                  colorama.Fore.WHITE)
            continue


for x in range(1, 51):
    threading.Thread(target=lambda: Loop(x)).start()
