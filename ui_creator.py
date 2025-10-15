import tkinter as tk # Для виджетов.
from tkinter import ttk # Более стилизованные виджеты.


def create_ui(root):
    """
    Создает пользовательский интерфейс приложения.
    :param root: корневой виджет приложения.
    :return: кортеж с виджетами (company_entry, position_entry, submit_button).
    """
    # Параметры для виджетов
    FONT = ("Arial", 12) # Задает шрифт для всех виджетов.
    ENTRY_WIDTH = 30 # Ширина полей ввода.
    PADDING = "20" # Отступы.
    GRID_PAD = 5 # Отступы между виджетами.
    
    # Создание основной структуры (Фрейма).
    main_frame = ttk.Frame(root, padding=PADDING) # Создается контейнер
    # main_frame с заданными отступами.
    main_frame.pack(expand=True, fill=tk.BOTH) # Метод pack размещает фрейм,
    # заполняя все доступное пространство.
    
    # Функция для создания лейбла и ввода
    def create_label_entry(frame, label_text, row):
        """
           Создает пару Label + Entry.
           Использует grid для размещения виджетов.
           sticky=tk.W выравнивает метку по левому краю.
           """
        label = ttk.Label(frame, text=label_text, font=FONT)
        entry = ttk.Entry(frame, font=FONT, width=ENTRY_WIDTH)
        
        label.grid(row=row, column=0, padx=GRID_PAD, pady=GRID_PAD,
                   sticky=tk.W)
        entry.grid(row=row, column=1, padx=GRID_PAD, pady=GRID_PAD)
        
        return entry
    
    # Создаем элементы интерфейса.
    company_entry = create_label_entry(main_frame, "Название компании:", 0)
    position_entry = create_label_entry(main_frame, "Должность:", 1)
    
    # Создаем кнопку.
    submit_button = ttk.Button(main_frame, text="Далее")
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)
    
    return company_entry, position_entry, submit_button
