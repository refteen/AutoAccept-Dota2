import cv2  # Нейросеть которая видит заданную ей картинку вновь
import numpy as np  # NumPy предоставляет эффективные и быстрые математические вычисления
import pyautogui  # Библиотека позволяет программно управлять мышью и клавиатурой
import time  # Библиотека time для работы со временем и задержкой между проверкой кнопки принять
import tkinter as tk  # Библиотека tkinter для создания простого окна
import sys

# Функция для принятия игры
def accept_game():
    accept_button_location = None
    # Снимаем скриншот экрана
    while accept_button_location is None:
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        # Загружаем изображение кнопки принятия
        accept_button_image = cv2.imread('knopka.png', cv2.IMREAD_COLOR)
        # Сравниваем скриншот с изображением кнопки
        result = cv2.matchTemplate(screenshot, accept_button_image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        # Если совпадение найдено, нажимаем на кнопку
        if max_val > 0.8:
            accept_button_location = np.where(result >= max_val)

            accept_button_center = (
                int(accept_button_location[1] + accept_button_image.shape[1] / 2),
                int(accept_button_location[0] + accept_button_image.shape[0] / 2)
            )

            x, y = accept_button_center

            print("Кнопка принятия найдена! Принимаем игру...")
            pyautogui.click(x, y)
            sys.exit()
        else:
            # Если совпадение не найдено, ждем 1 секунду и повторяем
            print("Кнопка принятия не найдена. Ждем 1 секунду и повторяем...")
            time.sleep(1)


def start_automatic_acceptance():
    print("Автоматическое принятие игры включено")
    accept_game()


# Создание основного окна
root = tk.Tk()
root.title("Автоматическое принятие игры")

# Создание кнопки для запуска автоматического принятия игры
start_button = tk.Button(root, text="Включить автопринятие", command=start_automatic_acceptance)
start_button.pack()

# Основной цикл работы окна

root.mainloop()
