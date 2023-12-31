# Программирование на языке высокого уровня (Python).
# Задание №______. Вариант !!!
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!


import time


class Заказ:
    """Класс Заказ содержит информацию о заказе."""

    # Переменная класса для определения номера заказа
    счетчик_заказов = 0

    def __init__(self):
        """Конструктор класса."""
        # Хранит экземпляры класса Пицца и его потомков
        self.заказанные_пиццы = []
        Заказ.счетчик_заказов += 1

    def __str__(self):
        """Вернуть содержимое заказа и его сумму.

        Формат вывода:

        Заказ №2
        1. Пицца: Пепперони | Цена: 350.00 р.
           Тесто: тонкое Соус: томатный
           Начинка: пепперони, сыр моцарелла
        2. Пицца: Барбекю | Цена: 450.00 р.
           Тесто: тонкое Соус: барбекю
           Начинка: бекон, ветчина, зелень, сыр моцарелла
        Сумма заказа: 800.00 р.

        """
        raise NotImplementedError
        # Уберите raise и добавьте необходимый код

        return res

    def добавить(self, пицца):
        """Добавить пиццу в заказ."""
        raise NotImplementedError
        # Уберите raise и добавьте необходимый код

    def сумма(self):
        """Вернуть сумму заказа."""
        raise NotImplementedError
        # Уберите raise и добавьте необходимый код

    def выполнить(self):
        """Выполнить заказ.

        Для каждой пиццы в заказе: подготовить, испечь, нарезать и упаковать.
        Сообщить, что заказ готов и пожелать приятного аппетита.

        Для визуального эффекта, каждое действие осуществляется с "задержкой",
        используя time.sleep(1).

        Формат вывода:

        Заказ поступил на выполнение...
        1. Пепперони
        Начинаю готовить пиццу Пепперони
          - замешиваю тонкое тесто...
          - добавляю соус: томатный...
          - и, конечно: пепперони, сыр моцарелла...
        Выпекаю пиццу... Готово!
        Нарезаю на аппетитные кусочки...
        Упаковываю в фирменную упаковку и готово!

        Заказ №2 готов! Приятного аппетита!
        """
        raise NotImplementedError
        # Уберите raise и добавьте необходимый код
