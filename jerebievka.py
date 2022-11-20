import random  # Подключение модуля для работы со случайной генерацией чисел
import logging  # Подключение модуля для логирования

# Добавление логирования
logging.basicConfig(
    filename="lottery.log",
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(app)s - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
)
logger = logging.getLogger("LOGGER")
logger = logging.LoggerAdapter(logger, {"app": "тестовое приложение"})
# Диалог с пользователем
print('Для проведения жеребьевки необходимо ввести количество (бочек) пользователей для жеребьевки.'
      '\nДалее при нажатии клавиши Enter будут по порядку выводится номера бочек')

while True:  # Ввод данных и их проверка
    logger.info('Программа запустилась')
    try:
        n = int(input('Введите количество пользователей (бочек) для жеребьевки: '))
    except ValueError:
        print('Данные введены некорректно. Попробуйте снова.')
        logger.error('Данные введены некорректно.')
        continue
    if n <= 0:
        print('Введены отрицательные значения. Попробуйте снова.')
        logger.error('Данные введены некорректно.')
        continue
    logger.info(f'Пользователь ввел  количество пользователей равное: {n}')

    arr = list()  # Создание списка чисел
    for i in range(n):  # Заполнение списка чисел от 1 до n
        arr.append(i+1)

    # Вывод случайных чисел путем удаления уже выпавших
    for j in range(n):
        rand = random.randint(0, len(arr) - 1)
        print(f'Число бочки под номером {j+1}: ', arr[rand])
        logger.info(f'На консоль выведено число {j+1} бочки : {arr[rand]} ')
        arr.pop(rand)
        input('Нажмите Enter для того чтобы вытащить следующее число')

    break  # Выход из цикла
logger.info('Программа завершила работу')
input('\nНажмите ENTER чтобы закрыть программу.')
