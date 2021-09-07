import lxml
from bs4 import BeautifulSoup as soup
import requests
import urlopen
import pandas

payload = {
    'FreeForm_bd': '01.09.2021',
    'FreeForm_ed': '30.09.2021',
    'FreeForm[id_department]': 0,
    'FreeForm[id_manager]': None,
    'FreeForm[id_project]': None,
    'FreeForm[id_office]': 1
}
url1 = 'https://crm3.e-portal.ru/index.php?r=report/paysperiod'
url2 = 'https://crm3.e-portal.ru/index.php?r=report/paysperiod'

# https://crm3.e-portal.ru/index.php?r=site/login
# https://crm3.e-portal.ru/index.php?r=report/paysperiod

session = requests.Session()
resp = session.post(url1, {
    'LoginForm[username]': 'baa',
    'LoginForm[password]': 'Qwe12345',  # log-in
    'LoginForm[rememberMe]': 1
})
print(resp.status_code)
new_resp = session.post(url2)  # navigation
print(new_resp.text)

'''
table = soup.find('table', class_="gridtab")
output = []
for row in table.find_all("tr"):
    new_row = []
    for cell in row.find_all(["td", "th"]):
        for sup in cell.find_all('sup'):
            sup.extract()
        for collapsible in cell.find_all(
                class_="mw-collapsible-content"):
            collapsible.extract()
        new_row.append(cell.get_text().strip())
    output.append(new_row)
print(output)
'''
# save to Excel
# res.to_excel(r'c:\result.xlsx', index=False)
