import tkinter as tk # Импортируем библиотеку tkinter для создания
# GUI-приложений.
from tkinter import messagebox # Импортируем модуль messagebox для
# всплывающих окон.
from company_checker import check_company # Импортируем функцию проверки
# компании.
import save_company # Импортируем модуль для сохранения данных.


def handle_submit(company_entry, position_entry):
    """
    Обрабатывает отправку формы с данными о компании и должности

    :param company_entry: виджет ввода названия компании
    :param position_entry: виджет ввода должности
    """
    try: # Получение и очистка данных.
        company_name = _get_cleaned_input(company_entry)
        position = _get_cleaned_input(position_entry)
        
        # Проверка обязательных полей
        _validate_required_fields(company_name, position)
        
        # Проверка существования компании
        if check_company(company_name):
            messagebox.showinfo("Уведомление",
                                "Вы уже отправляли отклик в эту компанию!")
            return
        
        # Сохранение данных
        if save_company.save_company(company_name, position):
            messagebox.showinfo("Успех", "Компания и должность добавлены")
        else:
            raise Exception("Ошибка при сохранении данных")
    
    except ValidationError as e:
        messagebox.showwarning("Предупреждение", str(e))
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
    finally:
        # Очистка полей
        company_entry.delete(0, tk.END)
        position_entry.delete(0, tk.END)


class ValidationError(Exception):
    """Пользовательское исключение для ошибок валидации"""
    pass


def _get_cleaned_input(entry_widget):
    """Получает и очищает ввод от пробелов"""
    return entry_widget.get().strip()


def _validate_required_fields(company_name, position):
    """Проверяет обязательные поля на заполненность"""
    if not company_name:
        raise ValidationError("Введите название компании")
    if not position:
        raise ValidationError("Введите должность")
