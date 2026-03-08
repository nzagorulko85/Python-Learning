if __name__ == "__main__":

    class Device:
        """
        Базовый класс для электронных устройств.

        Атрибуты:
            brand (str): производитель устройства (неизменяемый).
            model (str): модель устройства (неизменяемый).
            _power (bool): состояние питания (включено/выключено). Инкапсулирован как защищённый,
                            чтобы предотвратить прямое изменение извне. Доступ осуществляется через
                            методы turn_on() и turn_off().

        Методы:
            turn_on(): включает устройство.
            turn_off(): выключает устройство.
            get_info(): возвращает базовую информацию об устройстве.
        """

        def __init__(self, brand: str, model: str) -> None:
            """
            Инициализирует устройство с заданными брендом и моделью.
            По умолчанию устройство выключено.
            """
            self._brand = brand
            self._model = model
            self._power = False

        @property
        def brand(self) -> str:
            """Геттер для бренда (неизменяемый)."""
            return self._brand

        @property
        def model(self) -> str:
            """Геттер для модели (неизменяемый)."""
            return self._model

        def turn_on(self) -> None:
            """Включает устройство."""
            self._power = True

        def turn_off(self) -> None:
            """Выключает устройство."""
            self._power = False

        def is_on(self) -> bool:
            """Возвращает текущее состояние питания."""
            return self._power

        def get_info(self) -> str:
            """
            Возвращает строку с основной информацией об устройстве.
            Может быть перегружен в дочерних классах.
            """
            power_status = "включено" if self._power else "выключено"
            return f"{self.brand} {self.model} ({power_status})"

        def __str__(self) -> str:
            """Неформальное строковое представление для пользователей."""
            return self.get_info()

        def __repr__(self) -> str:
            """Официальное строковое представление для разработчиков."""
            return f"Device(brand={self.brand!r}, model={self.model!r})"


    class Smartphone(Device):
        """
        Дочерний класс, представляющий смартфон.

        Добавленные атрибуты:
            os (str): операционная система (неизменяемая).
            camera_mp (int): разрешение камеры в мегапикселях (с проверкой типа и значения).

        Расширяет функциональность базового класса:
            - конструктор расширен новыми параметрами
            - перегружен метод get_info() для включения специфической информации
            - перегружены магические методы __str__ и __repr__ для отражения новых атрибутов
        """

        def __init__(self, brand: str, model: str, os: str, camera_mp: int) -> None:
            """
            Инициализирует смартфон. Расширяет конструктор базового класса.
            """
            super().__init__(brand, model)
            self._os = os
            self.camera_mp = camera_mp

        @property
        def os(self) -> str:
            """Геттер для операционной системы (неизменяемая)."""
            return self._os

        @property
        def camera_mp(self) -> int:
            """Геттер для разрешения камеры."""
            return self._camera_mp

        @camera_mp.setter
        def camera_mp(self, value: int) -> None:
            """
            Сеттер для разрешения камеры с проверкой типа и положительного значения.
            Инкапсуляция обеспечивает корректность данных.
            """
            if not isinstance(value, int):
                raise TypeError("Разрешение камеры должно быть целым числом")
            if value <= 0:
                raise ValueError("Разрешение камеры должно быть положительным")
            self._camera_mp = value

        def get_info(self) -> str:
            """
            Перегруженный метод. Добавляет информацию об ОС и камере.
            Причина перегрузки: необходимо отобразить специфические для смартфона характеристики,
            которые отсутствуют в базовом классе.
            """
            base_info = super().get_info()
            return f"{base_info}, OS: {self.os}, камера: {self.camera_mp} Мп"

        def take_photo(self) -> str:
            """
            Новый метод, специфичный для смартфона.
            Возвращает строку, имитирующую съёмку фото.
            """
            if not self.is_on():
                return "Смартфон выключен. Невозможно сделать фото."
            return f"Сделано фото с разрешением {self.camera_mp} Мп."

        def __str__(self) -> str:
            """
            Перегружен для более детального пользовательского описания.
            """
            return self.get_info()

        def __repr__(self) -> str:
            """
            Перегружен для точного воссоздания объекта.
            """
            return (f"Smartphone(brand={self.brand!r}, model={self.model!r}, "
                    f"os={self.os!r}, camera_mp={self.camera_mp})")
