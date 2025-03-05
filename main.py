from init import LINK, DATA, HEADERS
from connect import get_info
from parse_data import get_parsing_data


if __name__ == "__main__":
	result = get_info(LINK, DATA, HEADERS)
	get_parsing_data(result)


