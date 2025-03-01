from LxmlSoup import LxmlSoup
import requests

# ссылка на ЦИАН Горно-Алтайск
LINK = 'https://gorno-altaysk.cian.ru/cat.php'

# Запрос для поиска (можно запрашивать на вводе)
REGION = 4719  # Республика Алтай, Горно-Алтайск
MIN_PRICE = 5000000
MAX_PRICE = 8000000
MIN_AREA = 30
MAX_AREA = 80
ROOM1 = 1  # 1 комн.
ROOM2 = 1  # 2 комн.
# ROOM3 = 1 # 3 комн.

## headers (прикидываемся браузером Chrome)
HEADERS = {'Content-Type': 'text/html; charset=utf-8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/133.0.0.0 Safari/537.36'}

# Данные для запроса
DATA = {'currency': 2,
        'deal_type': 'sale',
        'engine_version': 2,
        'offer_type': 'flat',
        'minprice': MIN_PRICE,
        'maxprice': MAX_PRICE,
        'region': REGION,
        'mintarea': MIN_AREA,
        'maxtarea': MAX_AREA,
        'room1': ROOM1,
        'room2': ROOM2,
        # 'room3': ROOM3,
        }


def get_info_from_site(link, data, headers):
	# посылаем GET запрос на сервер
	response = requests.get(LINK, params=DATA, headers=HEADERS)

	# смотрим возврат кода GET запроса
	status_code = response.status_code

	if status_code == 200:
		print('Server: 200 OK')
		get_parsing_data(response)
		return
	print("Server error: ", status_code)
	exit(1)


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

		print(title_result[0].text())
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

		for i, link in enumerate(links):
			url = link.get('href')
			# price = soup.find('span', class_ ='').text()
			print(f'{i} - {url}')


if __name__ == "__main__":
	get_info_from_site(LINK, DATA, HEADERS)
