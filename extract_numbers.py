#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-02-15 21:25:15
# @Author  : Shkliarskiy 
# 
# программа выбирает из lun-файла все числовые показатели с
# соответствующими преобразованиями
# 
# total_price - цена квартиры
# total_rooms - количество комнат
# price_sqm - цена за кв.м
# level - этаж
# total_levels - этажность дома
# year - год постройки дома
# rooms_area - список метража комнат

from typing import List, Union, Dict

COURSE = 28.0
NOT_FOUND = '*** not found'
DOLLAR = '$'
HRIVNA = 'грн'

def _get_row_property(line: str, index: int) -> Union[str, None]:
    """выделяет из csv-строки эл-т index порядковый номер эл-та
    """
    
    # разрезать строку на элементы списка
    line_as_list: List[str] = line.split(',')
    
    # выделить эл-т, если индекс не матчит, то возвратить  `None`
    try:
        row_prop: str = line_as_list[index]
    except:
        return None
    
    # не распарсеныый показатель
    if row_prop == NOT_FOUND: 
        return None
    
    # вернуть эл-т с индексом index
    return row_prop

def get_total_price(line: str) -> Union[float, None]:
    """возвращает цену квартиры как число или None

    Args:
        line (str): строка файла

    Returns:
        Union[float, None]: цена
    """
        
    price_str = _get_row_property(line, 0)
    if price_str is None:
        return None
    
    # сделать список
    price_list: List[str] = price_str.split()
    
    # порход по списку c накоплением всех цифр
    price = ''
    for item in price_list:
        if item.isnumeric():
            price += item
            
    # если цена не найдена
    if price == '': return None
    
    # перевести в цифорвой формат
    price_number = float(price)
    
    # перевести гривны в доллары, если цена в гривне (цена - последний эл-т)
    if price_list[-1] == 'грн': 
        price_number = round(price_number / COURSE, 1)
        
    return price_number
    
def get_romms(line: str) -> Union[int, None]: 
    """возвращает общее число комнат в квартире
    """
    
    # получить эл-т с числом комнат 
    rooms_str = _get_row_property(line, 1)
    if rooms_str is None:
        return None
    
    # выделить число комнат
    total_rooms_str: str = rooms_str.split()[0]
    if total_rooms_str.isnumeric():
        return int(total_rooms_str)
    else:
        return None
    
def get_price_sqm(line: str) -> Union[float, None]:
    """возвращает цену за м2 в $
    """
    
    # получить эл-т с ценой за м2
    price_sqm_str = _get_row_property(line, 2)
    if price_sqm_str is None:
        return None
    
    price_sqm_list:List[str] = price_sqm_str.split()
    
    # формируем цену в зависимости от валюты
    if DOLLAR in price_sqm_list:
        try:
            price_sqm = float(price_sqm_list[0])
        except:
            return None
    elif HRIVNA in price_sqm_list:
        ind = price_sqm_list.index(HRIVNA)
        # убрать пробели в записи цени в грн
        price_sqm_hrn = ''.join(price_sqm_list[:ind])
        # преобразовать в $ і вернуть
        if price_sqm_hrn.isnumeric():
            price_sqm = float(price_sqm_hrn) / COURSE
        else:
            return None
    else:
        # что-то пошло не так
        return None
    
    return price_sqm
        

def main():
    
    with open('aprts_data.csv') as file:
        # читать файл данных построчно
        for line in file:
            # выбрать цену квартиры
            total_price = get_total_price(line)
            # вибрать чісло комнат
            total_rooms = get_romms(line)
            # выбрать цену за метр в $
            price_sqm = get_price_sqm(line)
            # print(total_price, total_rooms, price_sqm)
    
    
if __name__ == '__main__':
    main()