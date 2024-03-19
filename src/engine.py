from requests_html import HTMLSession
import csv

def scrape_manajemen():
	session = HTMLSession()

	# url = "https://www.idnfinancials.com/id/byan/pt-bayan-resources-tbk"
	url = "https://www.idnfinancials.com/id/antm/pt-aneka-tambang-tbk"

	try:
		response = session.get(url)
		if response.status_code == 200:
			print("Request successful")
		else:
			print("Request failed")

		response.html.render(sleep=5, keep_page=True, scrolldown=2)

		nama_manajemen = response.html.find('#managements .item .name')
		title_manajemen = response.html.find('#managements .item .title')
		company_overview = response.html.find('table.table tbody tr')
		data_perusahaan = [row.find('td')[0].text for row in company_overview]

		print(f'\n Ini merupakan data perusahaan {data_perusahaan}')
		data_nama = [element.text for element in nama_manajemen]
		data_title = [element.text for element in title_manajemen]
		print(f'\n Ini merupakan nama eksekutif{data_nama}')
		print(f'\n Ini merupakan jabatan{data_title}') 

	except Exception as e:
		print("this is the error: ", e)
		print("error occurred at line:", e.__traceback__.tb_lineno)
	finally:
		session.close()
		print("session closed scraping success")

def scrape_shareholders():
	session = HTMLSession()

	# url = "https://www.idnfinancials.com/id/byan/pt-bayan-resources-tbk"
	url = "https://www.idnfinancials.com/id/antm/pt-aneka-tambang-tbk"

	try:
		response = session.get(url)
		if response.status_code == 200:
			print("Request successful")
		else:
			print("Request failed")

		response.html.render(sleep=5, keep_page=True, scrolldown=2)

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

	except Exception as e:
		print("this is the error: ", e)
		print("error occurred at line:", e.__traceback__.tb_lineno)
	finally:
		session.close()
		print("session closed scraping success")
  
def scrape_short_announcements():
	session = HTMLSession()

	# url = "https://www.idnfinancials.com/id/byan/pt-bayan-resources-tbk"
	url = "https://www.idnfinancials.com/id/antm/pt-aneka-tambang-tbk"

	try:
		response = session.get(url)
		if response.status_code == 200:
			print("Request successful")
		else:
			print("Request failed")

		response.html.render(sleep=5, keep_page=True, scrolldown=2)

		announcements = response.html.find('#table-announcement tbody tr')
		for announcement in announcements:
			date = announcement.find('.date')[0].text
			title_announcement = announcement.find('.title')[0].text
			resource = announcement.find('.source a')[0].attrs['href']
			print(f"Date: {date}")
			print(f"Title: {title_announcement}")
			print(f"Resource: {resource}")
			print()

	except Exception as e:
		print("this is the error: ", e)
		print("error occurred at line:", e.__traceback__.tb_lineno)
	finally:
		session.close()
		print("session closed scraping success")
  
def scrape_ipo():
	session = HTMLSession()

	# url = "https://www.idnfinancials.com/id/byan/pt-bayan-resources-tbk"
	url = "https://www.idnfinancials.com/id/antm/pt-aneka-tambang-tbk"

	try:
		response = session.get(url)
		if response.status_code == 200:
			print("Request successful")
		else:
			print("Request failed")

		response.html.render(sleep=5, keep_page=True, scrolldown=2)

		ipo_dates_table = response.html.find('#table-ipo-dates tbody tr')
		data_ipo_dates = []
		for row in ipo_dates_table:
			label = row.find('td')[0].text
			value = row.find('td')[1].text
			data_ipo_dates.append((label, value))
		for data in data_ipo_dates:
			print(f"{data[0]}: {data[1]}")

	except Exception as e:
		print("this is the error: ", e)
		print("error occurred at line:", e.__traceback__.tb_lineno)

	finally:
		session.close()
		print("session closed scraping success")
  
def scrape_news():
	session = HTMLSession()

	# url = "https://www.idnfinancials.com/id/byan/pt-bayan-resources-tbk"
	base_url = "https://www.idnfinancials.com/id/news/related/byan/pt-bayan-resources-tbk"
	page = 1

	try:
		while True:
			url = f"{base_url}/{page}"
			response = session.get(url)
			if response.status_code == 200:
				print(f"Request successful for page {page}")
			else:
				print(f"Request failed for page {page}")
				break

			response.html.render(sleep=5, keep_page=True, scrolldown=2)

			articles = response.html.find('.widget-body article.item')
			if not articles:
				break

			for article in articles:
				title = article.find('h2.title a')[0].text
				description = article.find('p.summary')[0].text
				date = article.find('p.date-published')[0].text
				print(f"Title: {title}")
				print(f"Description: {description}")
				print(f"Date: {date}")
				print()

			page += 1

	except Exception as e:
		print("this is the error: ", e)
		print("error occurred at line:", e.__traceback__.tb_lineno)

	finally:
		session.close()
		print("session closed scraping success")

def scrape_announcements():
	session = HTMLSession()

	base_url = "https://www.idnfinancials.com/id/announcement/byan/pt-bayan-resources-tbk"
	page = 1

	try:
		while True:
			url = f"{base_url}/{page}"
			response = session.get(url)
			if response.status_code == 200:
				print(f"Request successful for page {page}")
			else:
				print(f"Request failed for page {page}")
				break

			response.html.render(sleep=5, keep_page=True, scrolldown=2)

			announcements = response.html.find('.list-announcement-main li.item')
			if not announcements:
				break

			for announcement in announcements:
				title = announcement.find('h3 a')[0].text
				date = announcement.find('.d-f')[0].text
				resource = announcement.find('.c')[0].text
				print(f"Title: {title}")
				print(f"Date: {date}")
				print(f"Resource: {resource}")
				print()

			page += 1

	except Exception as e:
		print("this is the error: ", e)
		print("error occurred at line:", e.__traceback__.tb_lineno)

	finally:
		session.close()
		print("session closed scraping success")

def scrape_news():
	session = HTMLSession()

	# url = "https://www.idnfinancials.com/id/byan/pt-bayan-resources-tbk"
	base_url = "https://www.idnfinancials.com/id/news/related/byan/pt-bayan-resources-tbk"
	page = 1

	try:
		while True:
			url = f"{base_url}/{page}"
			response = session.get(url)
			if response.status_code == 200:
				print(f"Request successful for page {page}")
			else:
				print(f"Request failed for page {page}")
				break

			response.html.render(sleep=5, keep_page=True, scrolldown=2)

			articles = response.html.find('.widget-body article.item')
			if not articles:
				break

			for article in articles:
				title = article.find('h2.title a')[0].text
				description = article.find('p.summary')[0].text
				date = article.find('p.date-published')[0].text
				print(f"Title: {title}")
				print(f"Description: {description}")
				print(f"Date: {date}")
				print()

			page += 1

	except Exception as e:
		print("this is the error: ", e)
		print("error occurred at line:", e.__traceback__.tb_lineno)

	finally:
		session.close()
		print("session closed scraping success")

def scrape_emiten():
	session = HTMLSession()

	base_url = "https://www.idnfinancials.com/id/company/sector/energy-a"
	page = 1

	try:
		while True:
			url = f"{base_url}/{page}"
			response = session.get(url)
			if response.status_code == 200:
				print(f"Request successful for page {page}")
				
			else:
				print(f"Request failed for page {page}")
				break

			response.html.render(sleep=5, keep_page=True, scrolldown=2)
			emiten_codes = response.html.find('.code')
			for code in emiten_codes:
				print(f"Code: {code.text}")
			page += 1

	except Exception as e:
		print("this is the error: ", e)
		print("error occurred at line:", e.__traceback__.tb_lineno)

	finally:
		session.close()
		print("session closed scraping success")
  
def scrape_overview():
	session = HTMLSession()

	base_url = "https://www.idnfinancials.com/id/bren/pt-barito-renewables-energy-tbk#net-foreign"

	try:
		response = session.get(base_url)
		if response.status_code == 200:
			print("Request successful")
		else:
			print("Request failed")
		response.html.render(sleep=5, keep_page=True, scrolldown=2)
		overview_description = response.html.find('p')[0].text
		address = response.html.find('.bd-highlight')[0].text
		telephone_fax = response.html.find('.bd-highlight')[1].text
		email = response.html.find('.bd-highlight')[2].text.split('\n')[1]
		tanggal_pencatatan = response.html.find('.bd-highlight')[3].text.split('\n')[1]
		print(f"Overview Description: {overview_description}")
		print(f"\nAddress: {address}")
		print(f"\nTelephone/Fax: {telephone_fax}")
		print(f"\nEmail: {email}")
		print(f"\nTanggal Pencatatan: {tanggal_pencatatan}")
	except Exception as e:
		print("this is the error: ", e)
		print("error occurred at line:", e.__traceback__.tb_lineno)
	finally:
		session.close()
		print("session closed scraping success")
  
def scrape_affiliation():
	session = HTMLSession()

	base_url = "https://www.idnfinancials.com/id/bren/pt-barito-renewables-energy-tbk#net-foreign"

	try:
		response = session.get(base_url)
		if response.status_code == 200:
			print("Request successful")
		else:
			print("Request failed")
		response.html.render(sleep=5, keep_page=True, scrolldown=2)
		affiliation_table = response.html.find('table.table')[0]
		headers = affiliation_table.find('thead tr th')
		data_rows = affiliation_table.find('tbody tr')
		for row in data_rows:
			nama_perusahaan = row.find('td')[0].text
			persentase = row.find('td')[1].text
			print(f"Nama Perusahaan: {nama_perusahaan}")
			print(f"Persentase: {persentase}")
			print()
	except Exception as e:
		print("this is the error: ", e)
		print("error occurred at line:", e.__traceback__.tb_lineno)
	finally:
		session.close()
		print("session closed scraping success")
