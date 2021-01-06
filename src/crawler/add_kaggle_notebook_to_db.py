import sqlite3


from src.crawler.crawler import KaggleKernel
from src.crawler.crawler import KaggleCrawler

def main():

    db_conn = sqlite3.connect('crawled_kaggle.db')
    table= 'scripts'

    KAGGLE_NOTEBOOK_LINKS = [
        'https://www.kaggle.com/yuansun/lb-0-84-for-starters'
        # 'https://www.kaggle.com/utkukubilay/boston-crimes-eda',
        # 'https://www.kaggle.com/vitorgamalemos/boston-crimes-dataset',
        # 'https://www.kaggle.com/biphili/boston-crime-prediction'
    ]

    for notebook_link in KAGGLE_NOTEBOOK_LINKS:
        kernel = KaggleKernel(notebook_link)

        browser = kernel.get_browser()

        kernel.get(browser)

        browser.close()

        crawler = KaggleCrawler('Python', 'Hotness')
        crawler._insert_into_db(db_conn, table, kernel)

        print('Done:', notebook_link)

    db_conn.close()
if __name__ == '__main__':
    main()