import argparse
import logging

logging.basicConfig(filename='loggingERROR_create_rect.log', level=logging.ERROR, encoding='utf-8')
logger = logging.getLogger(__name__)


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise ValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise ValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


# Функция для запуска из командной строки

def main():
    parser = argparse.ArgumentParser(description='Создание экземпляра класса Rectangle')
    parser.add_argument('--width', help='ширина', required=True, type=float)
    parser.add_argument('--height', help='высота', required=True, type=float)  # required=True указывает, что данный аргумент командной строки является обязательным для ввода пользователем

    args = parser.parse_args()

    try:
        rect = Rectangle(args.width, args.height)
        print(rect)

    except ValueError as e:

        logger.error(f"Ошибка при создании объекта: {e}")
        print(f"Не удалось создать объект: {e}")


if __name__ == "__main__":
    main()

