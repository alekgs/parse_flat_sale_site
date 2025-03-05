import requests



def get_info(link: str, data: dict, headers: dict) -> str or None:
	"""
	Функция отправляет get-запрос, анализирует ответ от сайта и возвращает
	результат
	"""

	# посылаем GET запрос на сервер
	with requests.Session() as session:
		response = session.get(link, params=data, headers=headers)

		# смотрим возврат кода GET запроса
		status_code = response.status_code

		if status_code == 200:
			print('Server: 200 OK')
			return response
		else:
			exit(f'Server error: {status_code}')
