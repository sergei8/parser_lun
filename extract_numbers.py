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

def get_total_price(line: str) -> Union[float, None]:
    """возвращает цену квартиры как число или None

    Args:
        line (str): строка файла

    Returns:
        Union[float, None]: цена
    """
    
    # разрезать строку на элементы списка
    line_as_list: List[str] = line.split(',')
    
    # взять эл-т с ценой
    price_str: str = line_as_list[0]
    
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
    
def main():
    
    with open('aprts_data.csv') as file:
        # читать файл данных построчно
        for line in file:
            # выбрать цену квартиры
            total_price: Union[float, None] = get_total_price(line)
            # print(total_price)
    
    
if __name__ == '__main__':
    main()