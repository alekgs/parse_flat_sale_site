from LxmlSoup import LxmlSoup
from export import create_excel_file

def get_parsing_data(response):
	### далее парсим результат
	soup = LxmlSoup(response.text)

	# ищем заголовок запроса
	title_result = soup.find_all('h1',
	                             class_='_93444fe79c--color_text-primary'
	                                    '-default--vSRPB _93444fe79c--'
	                                    'lineHeight_36px--K6dvk _93444fe79c'
	                                    '--fontWeight_bold--BbhnX _93444fe79c'
	                                    '--fontSize_28px--P1gR4 _93444fe79c'
	                                    '--display_block--KYb25 _93444fe79c'
	                                    '--text--e4SBY _93444fe79c'
	                                    '--text_letterSpacing__normal'
	                                    '--tfToq'
	                             )
	print(title_result[0].text())

	# ищем имя класса с количеством полученных записей
	flats_count = soup.find_all('h5',
	                            class_='_93444fe79c--color_text-primary-'
	                                   'default--vSRPB _93444fe79c--'
	                                   'lineHeight_20px--fX7_V _93444fe79c'
	                                   '--fontWeight_bold--BbhnX '
	                                   '_93444fe79c--fontSize_14px--reQMB '
	                                   '_93444fe79c--display_block--KYb25 '
	                                   '_93444fe79c--text--e4SBY _93444fe79c'
	                                   '--text_letterSpacing__normal--tfToq'
	                            )

	print(flats_count[0].text())

	# Описание
	offer_title = soup.find_all('span',
	                            class_='_93444fe79c--color_text-primary-'
	                                   'default--vSRPB _93444fe79c--'
	                                   'lineHeight_28px--KFXmc _93444fe79c'
	                                   '--fontWeight_bold--BbhnX _93444fe79c'
	                                   '--fontSize_22px--sFuaL _93444fe79c'
	                                   '--display_block--KYb25 _93444fe79c'
	                                   '--text--e4SBY _93444fe79c--'
	                                   'text_letterSpacing__normal--tfToq'
	                            )

	# for i, title in enumerate(offer_title):
	# 	t = title.text()
	# 	price = soup.find_all('span', class_='')[i].text()
	# 	print(f'{i} - {t}, {price}')

	# ссылки на найденные квартиры
	links = soup.find_all('a', class_='_93444fe79c--link--VtWj6')

	wb, excel_file = create_excel_file(title_result[0].text(),
	                                   flats_count[0].text())
	sheet = wb.active

	for i, link in enumerate(links, start=1):
		url = link.get('href')

		# price = soup.find('span', class_ ='').text()
		print(f'{i} - {url}')

		# записываем строку в excel
		sheet[f'A{i + 2}'] = i
		sheet[f'B{i + 2}'] = url

	# сохраняем файл excel
	wb.save(excel_file)
	print(f'Экспорт завершен.')

	return
