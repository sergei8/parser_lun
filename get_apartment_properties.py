LUN_URL = 'https://flatfy.lun.ua/продажа-квартир-киев'

import requests
import re
from typing import Union, Dict, List
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_lun_html(url: str) -> Union[str, None]:
    """получает html страніци по url
    т.к. страница динамическая, то использует selenium webdriver

    Args:
        url (str): url страницы

    Returns:
        Union[str, None]: html страницы или None, при ошибке доступа
    """
    
    # опции webdriver  
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument('--silent')
    options.add_argument('--log-level=3')
    
    try:
        # открываем webdriver для Chrome с использованием его менеджера
        driver = webdriver.Chrome(ChromeDriverManager().install(),  options=options)
        # получаем страницу и выделяем ее текст 
        driver.get(url)
        page_source = driver.page_source
    except:
        page_source = None
    
    driver.quit()
    
    return page_source

def get_total_page(html: str) -> Union[str, None]:
    """возвращает количество страниц для парсинга
    """
    soup = bs(html, features='html.parser')
    
    try:
        # найти span с class = paging-dots
        span_3_dots = soup.find('span', class_="paging-dots")    
        
        # выбрать следующий и извлечь из него контент
        total_pages = span_3_dots.next_sibling.text
    except:
        return None

    return total_pages if  isinstance(total_pages, str)  else None

def find_all_aprts(html: str) -> Union[List[bs], None]:
    """Выбирает с страницы список bs-элементов с классом 'realty-content-layout'
    в которых находиятся описания квартир

    Args:
        html (str): [страница]

    Returns:
        Union[List[bs], None]: [список элементов квартир]
    """
    
    try:
        soup = bs(html, features='html.parser')
    
        # получить список всех описаний квартир на странице
        aprts_soup_list = soup.find_all('div', class_='realty-content-layout')
    except:
        return None
    
    return aprts_soup_list 

def get_total_price(soup: bs) -> Union[str, None]:
    """возвращает цену квартиры как она представлена в bs-элементе

    Args:
        soup (bs): [елемент квартиры]

    Returns:
        Union[str, None]: [цена]
    """
    
    try:
        total_price = soup.find('div', class_='realty-preview__price').text
    except:
        return '*** not found '
    
    return total_price 

def get_rooms(soup: bs) -> Union[str, None]:
    """возвращает кол-во комнат
    """
    
    try:
        rooms = soup.find('span', class_='realty-preview__info rooms').text
    except:
        return '*** not found '
    
    return rooms 

def get_price_per_m(soup:bs) -> Union[str, None]:
    """возвращает кол-во комнат
    """
    
    try:
        price_per_m: str = soup.find('div', class_='realty-preview__price--sqm').text
    except:
        return '*** not found '
    
    return price_per_m 

def get_level(soup:bs) -> Union[str, None]:
    
    try: 
        level = soup.find('span', text='этаж').next_sibling
    except: 
        return '*** not found '
    
    return level

def get_year(soup:bs) -> Union[str, None]:
    """возвращает год квартиры
    """
    try: 
        year = soup.find_all(class_='realty-content-layout__properties-row')[2].find_all(class_='realty-preview__info')[1].text
    except: 
        return '*** not found '
    
    return year

def get_type(soup: bs) -> Union[str, None]:
    """возвращает тип квартиры
    """
    try: 
        type = list(soup.find_all(class_='realty-content-layout__properties-row')[3].find_all(class_='realty-preview__info')[1].children)[1]
    except: 
        return '*** not found '
    
    return type

def get_area(soup:bs) -> Union[str, None]:
    """возвращает площадь комнат в виде строки
    """
    try: 
        area = soup.find('span', class_='realty-preview__info area').text
    except: 
        return '*** not found '
    
    return area

def get_address(soup:bs) -> Union[str, None]:
    """возвращает адрес
    """
    try: 
        area = soup.find('a', class_='realty-preview__title-link').text
    except: 
        return '*** not found '
    
    return area

    

def main():
    
    # получить 1-ю страницу с продажей квартир lun 
    url = LUN_URL
    lun_html = get_lun_html(LUN_URL)
    if lun_html is None:
        print (f'ошибка доступа к страніце: {url}')
        exit (1)
    
    # получить общее количество страниц с продажей
    total_pages = get_total_page(lun_html)
    if total_pages is None:
        print('ошибка в определении кол-ва страниц')
        exit (1)
    if not total_pages.isnumeric():
        print(f'кол-во страниц не число: {total_pages}')
        exit (1)    
    
    # total_pages = 0
    # проход по всем страницам
    for page in range(70,71):
    # for page in range(int(total_pages) + 1):
        
        # формируем url страницы
        url = f'{LUN_URL}?page={str(page)}'
        html = get_lun_html(url)
        
        # получить с текущей страницы soup всех описаний квартир
        # при ошибке перейти на следующую страницу
        # TODO сделать генератор "aprt_soup_list"
        aprt_soup_list = find_all_aprts(html)
        if aprt_soup_list is None:
            print(f'ошибка парсинга страницы: {url}')
            continue
        
        # проход по списку квартир и формирование строки выходного файла
        with open('output.csv', 'a+') as file:
            for aprt in aprt_soup_list:
                line =  f'{get_total_price(aprt)},{get_rooms(aprt)},{get_price_per_m(aprt)},'
                line += f'{get_level(aprt)},{get_year(aprt)},{get_type(aprt)},{get_area(aprt)},{get_address(aprt)}'
                print(line)
                file.write(line+'\n')
        

if __name__ == '__main__':
    
    main()