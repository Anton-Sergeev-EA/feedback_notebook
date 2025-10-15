import create_main_window # Подключение внешнего модуля отвечающего за
# главное окно приложения.
import handle_submit # Подключение внешнего модуля отвечающего за логику
# обработки отправки данных.
import ui_creator # Модуль для создания элементов пользовательского интерфейса.


def main():
    """
    Основная функция запуска приложения
    """
    try:
        # Инициализация главного окна.
        root = create_main_window.create_main_window()
        
        # Создание пользовательского интерфейса
        ui_components = ui_creator.create_ui(root)
        company_entry, position_entry, submit_button = ui_components
        
        # Настройка функциональности кнопки.
        submit_button.config(
            command=lambda: handle_submit.handle_submit(
                company_entry,
                position_entry
            )
        )
        
        # Запуск главного цикла обработки событий.
        root.mainloop()
    
    except Exception as e:
        print(f"Произошла ошибка при запуске приложения: {str(e)}")


if __name__ == "__main__":
    """
    Точка входа в приложение
    """
    main()
