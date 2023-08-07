import os.path
import re
import requests
import csv

""" 
Парсим логи на получение данных:
'remote_addr', 'request_datetime', 'request_type', 
'requested_resource', 'response_code', 'response_size'
и пишем в файл CSV
"""

url = "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"

if not os.path.exists("./log.txt"):
    response = requests.get(url).text
    with open('./log.txt', 'w', encoding='utf-8') as file:
        file.write(response)

pattern = re.compile(r"^([\w.:]+[^\s_])[\s-]+\[([\w+/:\s]+)\]\s\"([A-Z]+)\s([/\w]+)\s[\w+/.\"]+\s([0-9]+)\s([0-9]+).+$")
with open('./log.txt') as file:
    log_data = file.readlines()

with open('log_data.csv', 'w') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(('remote_addr', 'request_datetime', 'request_type', 'requested_resource', 'response_code', 'response_size'))

    for line in log_data:
        writer.writerow(re.match(pattern, line).groups())
