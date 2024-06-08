'''Напишите функцию, которая принимает на вход строку -
абсолютный путь до файла. Функция возвращает кортеж из трёх элементов:
путь, имя файла, расширение файла.'''

path = input('Введите абсолютный путь до файла: ')

def find_path(path: str) -> tuple[str]:
    *adress, name_extension = path.split('\\')
    name, extension = name_extension.split('.')
    adress = '/'.join(adress)

    return (adress, name, extension)

print(find_path(path))