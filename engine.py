from requests_html import HTMLSession
import csv

session = HTMLSession()

url = "https://www.idnfinancials.com/id/byan/pt-bayan-resources-tbk#managements"

try:
	response = session.get(url)

	response.html.render(sleep=30, keep_page=True, scrolldown=1)

	nama_manajemen = response.html.find('#managements .item .name')
	title_manajemen = response.html.find('#managements .item .title')
	company_overview = response.html.find('table.table tbody tr')
	data_perusahaan = [row.find('td')[0].text for row in company_overview]
	data_presentase = [row.find('td')[1].text for row in company_overview]
	print(data_perusahaan)
	print(data_presentase)

	data = [element.text for element in nama_manajemen]
	data_title = [element.text for element in title_manajemen]
	print(data_title)

	#filename = "data.csv"

	#with open(filename, 'w', newline='') as csvfile:
	#	writer = csv.writer(csvfile)
	#	writer.writerow(["Nama Manajemen"])
	#	writer.writerows([[name] for name in data])

	#print("data saved to", filename)

except Exception as e:
    print("this is the error: ", e)
    print("error occurred at line:", e.__traceback__.tb_lineno)
finally:
	session.close()
	print("session closed scraping success")