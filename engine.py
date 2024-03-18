from requests_html import HTMLSession
import csv

session = HTMLSession()

url = "https://www.idnfinancials.com/id/byan/pt-bayan-resources-tbk"

try:
	response = session.get(url)
	if response.status_code == 200:
		print("Request successful")
	else:
		print("Request failed")

	response.html.render(sleep=15, keep_page=True, scrolldown=2)

	nama_manajemen = response.html.find('#managements .item .name')
	title_manajemen = response.html.find('#managements .item .title')
	company_overview = response.html.find('table.table tbody tr')
	# detail_shareholders = response.html.find('table.table tbody tr')
	data_perusahaan = [row.find('td')[0].text for row in company_overview]
	# data_presentase = [row.find('td')[1].text for row in company_overview]
	shareholders = response.html.find('#table-shareholder tbody tr')
	data_shareholders = []
	for shareholder in shareholders:
		nama_pemegang_saham = shareholder.find('td')[0].text
		jumlah_saham = shareholder.find('td')[1].text
		modal_disetor = shareholder.find('td')[2].text
		persentase = shareholder.find('td')[3].text
		data_shareholders.append((nama_pemegang_saham, jumlah_saham, modal_disetor, persentase))

	for data in data_shareholders:
		print(f"Nama Pemegang Saham: {data[0]}")
		print(f"Jumlah Saham: {data[1]}")
		print(f"Modal Disetor: {data[2]}")
		print(f"Persentase: {data[3]}")
		print()

	print(f'\n Ini merupakan data perusahaan {data_perusahaan}')
	# print(data_presentase)
	data_nama = [element.text for element in nama_manajemen]
	data_title = [element.text for element in title_manajemen]
	print(f'\n Ini merupakan nama eksekutif{data_nama}')
	print(f'\n Ini merupakan jabatan{data_title}') 

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