from openpyxl import Workbook
from datetime import datetime


def create_excel_file(title, count_records):
    print('Экспорт результатов в файл excel...')

    # Создаем новую рабочую книгу (файл)
    wb = Workbook()

    # активный лист книги Excel
    sheet = wb.active
    sheet.title = "Лист1"

    # Записываем заголовки в ячейки
    sheet['A1'] = title
    sheet['A2'] = count_records

    # имя для файла экспорта в Excel
    excel_filename = 'result_' + datetime.now().strftime("%Y%d%m_%H%M"
                                                         ) + '.xlsx'

    # Сохраняем файл на диск
    wb.save(excel_filename)

    return wb, excel_filename


def write_row_to_workbook(data: dict, excel_wb: Workbook):
    # активный лист книги
    sheet = excel_wb.active

    for i, k in data.items():
        sheet[f'A{i + 2}'] = i
        sheet[f'B{i + 2}'] = k[0]

    return
