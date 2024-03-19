import schedule
import time
import subprocess
from src.engine import scrape_manajemen, scrape_shareholders, scrape_short_announcements, scrape_ipo, scrape_news, scrape_announcements, scrape_emiten, scrape_overview, scrape_affiliation
from src.sql import show_tables, insert_tables


# def main():
#     schedule.every(1).minutes.do(scrape_shareholders())

#     while True:
#         schedule.run_pending()
#         time.sleep(1)

def main():
    scrape_affiliation()

if __name__ == "__main__":
    main()
