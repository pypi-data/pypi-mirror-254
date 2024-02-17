P_FILE_ID = r'(?P<FILE_ID>[A-Za-z0-9+\-_/=]{65,80})'
P_USERNAME = r'(?P<USERNAME>(?=.{5,64}(?:\s|$))(?![_])(?!.*[_]{2})[a-zA-Z0-9_]+(?<![_.]))'
P_MSG_ID = r'MSG(?P<MSG_ID>\d+)'
P_STICKER_ID = fr'({P_FILE_ID}|{P_MSG_ID})'