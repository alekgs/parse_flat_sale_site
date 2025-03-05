# ссылка на ЦИАН Горно-Алтайск
LINK = 'https://gorno-altaysk.cian.ru/cat.php'

# Запрос для поиска (можно запрашивать на вводе)
REGION = 4719  # Республика Алтай, Горно-Алтайск
MIN_PRICE = 5000000  # минимальная цена
MAX_PRICE = 8000000  # максимальная цена
MIN_AREA = 30  # минимальная площадь
MAX_AREA = 80  # максимальная площадь
ROOM1 = 1  # 1 комн.
ROOM2 = 0  # 2 комн.
# ROOM3 = 1         # 3 комн и т.д.

## headers для get-запроса
HEADERS = {'Content-Type': 'text/html; charset=utf-8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/133.0.0.0 Safari/537.36'}

# формируем данные для get-запроса
DATA = {
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
		}
