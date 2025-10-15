import tkinter as tk # Cозданиt визуального интерфейса программы.


def create_main_window():
    """
    Создает и настраивает главное окно приложения
    :return: объект корневого окна Tkinter
    """
    # Параметры окна
    WINDOW_TITLE = "Блокнот для сохранения откликов"
    WINDOW_SIZE = "500x300"
    BACKGROUND_COLOR = "#f0f0f0"
    
    # Создание и настройка окна
    root = tk.Tk()
    _configure_window(root, WINDOW_TITLE, WINDOW_SIZE, BACKGROUND_COLOR)
    return root


def _configure_window(window, title, size, bg_color):
    """
    Настраивает параметры окна
    :param window: объект окна Tkinter
    :param title: заголовок окна
    :param size: размеры окна в формате "ширина*высота"
    :param bg_color: цвет фона
    """
    window.title(title)
    window.geometry(size)
    window.configure(bg=bg_color)
