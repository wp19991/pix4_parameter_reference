import json

from bs4 import BeautifulSoup

# 在此输入您的HTML数据
with open('./参数html.txt', 'r', encoding='utf-8') as f:
    html_data = ''.join(f.readlines())

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_data, 'html.parser')

# 找到所有的表格
tables = soup.find_all('table')

res_list = []

# 遍历每个表格并提取数据
for table in tables:
    # 找到表头
    headers = [header.text for header in table.find('thead').find('tr').find_all('th')]

    # 找到表格数据
    rows = table.find('tbody').find_all('tr')
    for row in rows:
        # 提取每一行的数据
        data = [cell.text.strip() for cell in row.find_all('td')]

        # 创建一个字典来将表头和数据配对
        table_data = dict(zip(headers, data))

        # 打印或处理表格数据
        print(table_data)
        res_list.append(table_data)

print(len(res_list))
with open('px4参数.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res_list, indent=4, ensure_ascii=False))
