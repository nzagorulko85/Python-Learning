# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Table:
    """
    Класс, описывающий стол как предмет мебели.

    Attributes:
        height (float): Высота стола в метрах
        area (float): Площадь столешницы в квадратных метрах
        max_load (float): Максимальная нагрузка в килограммах
    """

    def __init__(self, height: float, area: float, max_load: float):
        """
        Инициализирует стол с заданными характеристиками.

        Args:
            height: Высота стола в метрах (должна быть > 0 и в разумных пределах)
            area: Площадь столешницы в квадратных метрах (должна быть > 0)
            max_load: Максимальная нагрузка в килограммах (должна быть > 0)

        Examples:
            >>> table = Table(0.75, 1.5, 50.0)
            >>> table.height
            0.75
        """
        if not 0.4 <= height <= 1.5:
            raise ValueError("Высота стола должна быть в пределах 0.4-1.5 метра")
        if area <= 0:
            raise ValueError("Площадь должна быть положительным числом")
        if max_load <= 0:
            raise ValueError("Максимальная нагрузка должна быть положительным числом")

        self.height = height
        self.area = area
        self.max_load = max_load
        self.current_load = 0.0
        self.occupied_area = 0.0

    def place_item(self, weight: float, area_required: float) -> bool:
        """
        Размещает предмет на столе.

        Args:
            weight: Вес предмета в килограммах
            area_required: Площадь, занимаемая предметом в квадратных метрах

        Raises:
            ValueError: Если вес или площадь отрицательные
        """
        if weight < 0:
            raise ValueError("Вес предмета не может быть отрицательным")
        if area_required < 0:
            raise ValueError("Занимаемая площадь не может быть отрицательной")
        ...


    def adjust_height(self, new_height: float) -> bool:
        """
        Регулирует высоту стола.

        Args:
            new_height: Новая высота стола в метрах

        Raises:
            ValueError: Если новая высота вне допустимого диапазона
        """
        if not 0.4 <= new_height <= 1.5:
            raise ValueError("Высота стола должна быть в пределах 0.4-1.5 метра")

        self.height = new_height
        return True

    def clear_table(self) -> None:
        """
        Очищает стол от всех предметов.

        """
        self.current_load = 0.0
        self.occupied_area = 0.0


class Wall:
    """
    Класс, описывающий стену в здании.

    Attributes:
        length (float): Длина стены в метрах
        height (float): Высота стены в метрах
        material (str): Основной материал (кирпич, бетон, гипсокартон)
    """

    def __init__(self, length: float, height: float, material: str):
        """
        Инициализирует стену с заданными параметрами.

        Args:
            length: Длина стены (должна быть > 0)
            height: Высота стены (должна быть > 0)
            material: Материал стены (непустая строка)

        Raises:
            ValueError: Если параметры не соответствуют ограничениям

        Examples:
            >>> wall = Wall(4.0, 2.5, "кирпич")
            >>> wall.length
            4.0
        """
        if length <= 0:
            raise ValueError("Длина стены должна быть положительной")
        if height <= 0:
            raise ValueError("Высота стены должна быть положительной")
        if not material or not material.strip():
            raise ValueError("Материал стены не может быть пустой строкой")

        self.length = length
        self.height = height
        self.material = material

    def change_length(self, new_length: float) -> bool:
        """
        Изменяет длину стены.

        Args:
            new_length: Новая длина стены в метрах (должна быть > 0)

        Raises:
            ValueError: Если новая длина не является положительным числом

        """
        if new_length <= 0:
            raise ValueError("Длина стены должна быть положительной")
        ...


    def change_height(self, new_height: float) -> bool:
        """
        Изменяет высоту стены.

        Args:
            new_height: Новая высота стены в метрах (должна быть > 0)

        Raises:
            ValueError: Если новая высота не является положительным числом
        """
        if new_height <= 0:
            raise ValueError("Высота стены должна быть положительной")
        ...

    def calculate_area(self) -> float:
        """
        Рассчитывает площадь стены.

        Returns:
            float: Площадь стены в квадратных метрах
        """
        ...


class Backpack:
    """
    Класс, описывающий рюкзак для переноски вещей.

    Attributes:
        capacity (float): Вместимость в литрах
        material (str): Материал изготовления
        compartments (int): Количество отделений
    """

    def __init__(self, capacity: float, material: str, compartments: int):
        """
        Инициализирует рюкзак с заданными характеристиками.

        Args:
            capacity: Вместимость в литрах (должна быть > 0)
            material: Материал изготовления (непустая строка)
            compartments: Количество отделений (должно быть ≥ 1)

        Raises:
            ValueError: Если параметры не соответствуют ограничениям

        Examples:
            >>> backpack = Backpack(30.0, "нейлон", 3)
            >>> backpack.capacity
            30.0
        """
        if capacity <= 0:
            raise ValueError("Вместимость должна быть положительной")
        if not material or not material.strip():
            raise ValueError("Материал не может быть пустой строкой")
        if compartments < 1:
            raise ValueError("Количество отделений должно быть не менее 1")

        self.capacity = capacity
        self.material = material
        self.compartments = compartments
        self.items = []
        self.occupied_volume = 0.0

    def pack_item(self, item_name: str, volume: float) -> float:
        """
        Упаковывает предмет в рюкзак.

        Args:
            item_name: Название предмета для упаковки
            volume: Объем предмета в литрах

        Returns:
            float: Оставшаяся свободная вместимость в литрах

        Raises:
            ValueError: Если объем предмета отрицательный или превышает доступное место
        """
        if volume < 0:
            raise ValueError("Объем предмета не может быть отрицательным")
        if volume > (self.capacity - self.occupied_volume):
            raise ValueError("Предмет не помещается в рюкзак")
        ...

    def unpack_item(self, item_name: str) -> tuple[str, float]:
        """
        Достает предмет из рюкзака.

        Args:
            item_name: Название предмета для извлечения

        Returns:
            tuple: Кортеж (название предмета, его объем)

        Raises:
            ValueError: Если указанный предмет отсутствует в рюкзаке
        """
        if item_name not in self.items:
            raise ValueError("Предмета нет в рюкзаке")
        ...



if __name__ == "__main__":
    doctest.testmod()
    pass
