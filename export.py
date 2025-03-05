from openpyxl import Workbook
from datetime import datetime


def create_excel_file(title, count_records):
    # Создаем новую рабочую книгу (файл)
    wb = Workbook()

    # активный лист книги Excel
    sheet = wb.active
    sheet.title = "Лист1"

    # Записываем заголовки в ячейки
    sheet['A1'] = title
    sheet['A2'] = count_records

    # имя для файла экспорта в Excel
    excel_filename = 'result_' + datetime.now().strftime("%Y%d%m_%H%M") + '.xlsx'

    # Сохраняем файл на диск
    print(f'Экспорт результатов в файл {excel_filename}...')
    wb.save(excel_filename)

    return wb, excel_filename

