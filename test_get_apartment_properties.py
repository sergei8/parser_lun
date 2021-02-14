import pytest
from bs4 import BeautifulSoup as bs

from get_apartment_properties import \
    get_total_page, \
    find_all_aprts, \
    get_total_price, \
    get_rooms, \
    get_price_per_m, \
    get_level, \
    get_area, \
    get_year, \
    get_type, \
    get_address
    
LUN_URL = 'https://flatfy.lun.ua/продажа-квартир-киев'


@pytest.fixture
def get_lun_page():
    html = \
"""
<html>
<body>
<div></div>
<div class="realty-content-layout"><div class="realty-content-layout__main-row"><a target="_blank" rel="nofollow noopener" href="/redirect/376981514" class="realty-preview__content-link" data-event-category="card" data-event-action="click" data-event-label="content"><div class="realty-content-layout__properties"><div class="realty-content-layout__properties-row"><div class="realty-content-layout__property"><div class="realty-preview__price">165&nbsp;000 $</div></div><div class="realty-content-layout__property rooms"><span class="realty-preview__info rooms">1 комната</span></div></div><div class="realty-content-layout__properties-row"><div class="realty-content-layout__property"><div class="realty-preview__price--sqm">3367 $ за м²</div></div><div class="realty-content-layout__property area"><span class="realty-preview__info area">49 / 20 / 18 м²</span></div></div></div></a><div class="realty-content-layout__head"><div class="realty-content-layout__title-row"><h3 class="realty-preview__title">
<a target="_blank" rel="nofollow noopener" href="/redirect/376981514" class="realty-preview__title-link" data-event-category="card" data-event-action="click" data-event-label="header">ул. Златоустовская</a></h3></div><div class="realty-content-layout__sub-title-row"><a class="realty-preview__sub-title" data-event-category="card" data-event-action="click" data-event-label="subtitle_geo" href="/жк-einstein-concept-house-киев">ЖК Einstein Concept House</a><a class="realty-preview__sub-title" data-event-category="card" data-event-action="click" data-event-label="subtitle_geo" href="/продажа-квартир-киев-микрорайон-солдатская-слободка">Солдатская слободка</a><a class="realty-preview__sub-title" data-event-category="card" data-event-action="click" data-event-label="subtitle_geo" href="/продажа-квартир-киев-шевченковский-район">Шевченковский</a><a class="realty-preview__sub-title" data-event-category="card" data-event-action="click" data-event-label="subtitle_geo" href="/продажа-квартир-киев">Киев</a></div></div><div class="realty-content-layout__description"><div title="Показать подробное описание" data-event-category="card" data-event-action="text" data-event-label="open" aria-hidden="false" class="rah-static rah-static--height-specific" style="height: 36px; overflow: hidden;"><div><div class="realty-preview__details"> <p class="realty-preview__description">КВАРТИРЫ В КЛУБНОМ ДОМЕ БЕЗ КОМИССИИ!!! Квартира 47 кВ метров на втором этаже , с ремонтом , полностью меблированной !!! Клубный дом премиум класса "Einstein Concept House" по адресу ул. Златоустовская, 22. В доме всего 26 квартир это поверьте очень комфортно жить в приличном месте и с приличными соседями ! Стильный и уютный холл , обслуживание , охрана консьерж сервис 24/7 В квартире стоит система “Умный дом” - легкий доступ ко всем функциям вашей квартиры через мобильное приложение у вас в телефоне ! - Дистанционный контроль использования энергоресурсов; - Автоматизированное управление освещением; - Контроль потребления электроэнергии и воды с мобильного приложения. - Доступ к камерам с мобильного приложения. - Автоматизированный контроль посещения дома. - Датчики для отслеживания рабочего состояния систем. - Немедленное информирование об аварийных случаях. - Система анти-затопления, которая отключает воду в аварийном случае. Современная охранная система дома - система видеонаблюдения с возможностью записи. Вход в подъезд по вашему отпечатку пальца !!! или по карте. Дистанционное управление входной дверью IP-домофония. Круглосуточный сервис заказа услуг в 1 клик. Собственная клининговая, консьерж-сервис 24/7. Станция подзарядки электромобилей. Во внутреннем дворе шлагбаум,и своя парковка. Качественный дом с небольшим Собственный индивидуальный тепловой пункт в доме, бесшумный скоростной лифт Wittur (Германия), станция подзарядки для электромобилей, подогрев крыльца от обледенения. Дом расположен в исторической части города, рядом множество парков и скверов.</p></div></div></div></div><a target="_blank" rel="nofollow noopener" href="/redirect/376981514" class="realty-preview__content-link" data-event-category="card" data-event-action="click" data-event-label="content"><div class="realty-content-layout__properties"><div class="realty-content-layout__properties-row"><div class="realty-content-layout__property">
<span class="realty-preview__info"><span class="realty-preview__info-label">этаж</span>2 из 9</span></div><div class="realty-content-layout__property"></div></div><div class="realty-content-layout__properties-row"><div class="realty-content-layout__property"></div><div class="realty-content-layout__property"><span class="realty-preview__info"><span class="realty-preview__info-label">стены</span>кирпичные</span></div></div></div><div class="realty-content-layout__properties-row realty-content-layout__time-row"><div class="realty-content-layout__property"><span class="realty-preview__info realty-preview__info--time">Обновлено: <span>5 февраля</span></span></div><div class="realty-content-layout__property"><span class="realty-preview__info realty-preview__info--time">Найдено: <span>28 октября 2020&nbsp;г.</span></span></div></div></a></div>

<span class="paging-dots">...</span>
<a class="paging-button" data-event-category="pagination" data-event-action="number_click" data-event-label="99" 
href="/продажа-квартир-киев?page=99">99</a>
</body>
</html>
"""

    html1 = \
"""
<html>
<body>
<div></div>
<div class="realty-content-layout"><div class="realty-content-layout__main-row"><a target="_blank" rel="nofollow noopener" href="/redirect/379991021" class="realty-preview__content-link" data-event-category="card" data-event-action="click" data-event-label="content"><div class="realty-content-layout__properties"><div class="realty-content-layout__properties-row"><div class="realty-content-layout__property realty-content-layout__property--full-width"><div class="realty-preview__price">89&nbsp;000 $</div></div></div><div class="realty-content-layout__properties-row"><div class="realty-content-layout__property realty-content-layout__property--full-width"><div class="realty-preview__price--sqm">1413 $ за м²</div></div></div></div></a><div class="realty-content-layout__head"><div class="realty-content-layout__title-row"><h3 class="realty-preview__title"><a target="_blank" rel="nofollow noopener" href="/redirect/379991021" class="realty-preview__title-link" data-event-category="card" data-event-action="click" data-event-label="header">ул. Максимовича (Онуфрия Трутенко), 7</a></h3></div><div class="realty-content-layout__sub-title-row"><a class="realty-preview__sub-title" data-event-category="card" data-event-action="click" data-event-label="subtitle_geo" href="/жк-ул-михаила-максимовича-трутенко-9-киев">ЖК ул. Михаила Максимовича (Трутенко), 9</a><a class="realty-preview__sub-title" data-event-category="card" data-event-action="click" data-event-label="subtitle_geo" href="/продажа-квартир-киев-микрорайон-голосеево">Голосеево</a><a class="realty-preview__sub-title" data-event-category="card" data-event-action="click" data-event-label="subtitle_geo" href="/продажа-квартир-киев-голосеевский-район">Голосеевский</a><a class="realty-preview__sub-title" data-event-category="card" data-event-action="click" data-event-label="subtitle_geo" href="/продажа-квартир-киев">Киев</a></div></div><div class="realty-content-layout__description"><div title="Показать подробное описание" data-event-category="card" data-event-action="text" data-event-label="open" aria-hidden="false" class="rah-static rah-static--height-specific" style="height: 42px; overflow: hidden;"><div><div class="realty-preview__details"> <p class="realty-preview__description">Вашему вниманию предлагается 2к квартира по адресу: Михаила Максимовича 7 Общая площадь – 63, кухня 11 кв. м. Дом 2012 года постройки, этаж 12/14, квартира с евроремонтом, кондиционеры в каждой комнате, везде пластиковые окна, лоджия застеклена и обшита пластиком, на полу плитка. Установлен бойлер, счетчики на холодную и горячую воду, счётчик на отопление, на полу паркетное покрытие и плитка, на стенах обои, встроенная кухня и шкафы купе, домофон, интернет. ванная и санузел раздельные, пол и стены плитка, квартира частично с мебелью. В подъезде есть консьерж и установлено видеонаблюдение. Закрытая территория с круглосуточной охраной жилого комплекса, большая наземная парковка, детские площадки, футбольное поле. В двух минутах от дома остановка общественного транспорта, Развитая инфраструктура, Метро Васильковская 7-10 мин, пешком. В двух минутах от дома остановка общественного транспорта, В пешей доступности большое количество магазинов, EVA, ProStor, Новая почта, УкрПочта, супермаркеты: Варус, Ашан, Лоток.</p></div></div></div></div><a target="_blank" rel="nofollow noopener" href="/redirect/379991021" class="realty-preview__content-link" data-event-category="card" data-event-action="click" data-event-label="content"><div class="realty-content-layout__properties"><div class="realty-content-layout__properties-row"><div class="realty-content-layout__property"><span class="realty-preview__info rooms">2 комнаты</span></div><div class="realty-content-layout__property"><span class="realty-preview__info">серия КТ</span></div></div><div class="realty-content-layout__properties-row"><div class="realty-content-layout__property"><span class="realty-preview__info area">63 / 31.5 / 11 м²</span></div><div class="realty-content-layout__property"><span class="realty-preview__info">2013</span></div></div><div class="realty-content-layout__properties-row"><div class="realty-content-layout__property"><span class="realty-preview__info">12 этаж из 14</span></div><div class="realty-content-layout__property"><span class="realty-preview__info">утепленная панель</span></div></div></div><div class="realty-content-layout__properties-row realty-content-layout__time-row"><div class="realty-content-layout__property"><span class="realty-preview__info realty-preview__info--time">Обновлено: <span>сегодня в 19:00</span></span></div><div class="realty-content-layout__property"><span class="realty-preview__info realty-preview__info--time">Найдено: <span>19 декабря 2020&nbsp;г.</span></span></div></div></a></div><div class="realty-content-layout__action-row"><div class="realty-content-layout__action-property"><a target="_blank" rel="nofollow noopener" href="/redirect/379991021" class="realty-preview__details-button" data-event-category="card" data-event-action="click" data-event-label="more">Подробнее</a></div><div class="realty-content-layout__special-actions"><div class="realty-preview__group-button"><button class="button-base icon-button realty-preview__icon-wrapper" tabindex="0" type="button" aria-label="Кто еще продает" title="Кто еще продает" data-event-category="card" data-event-action="who_sell_click" data-event-label="open"><span class="icon-button__label">Ещё 9+</span><canvas class="button-base__ripple"></canvas></button></div></div></div></div>
</body>
</html>
"""
    
    return html.replace('\n', '')
    
    
def test_get_total_page(get_lun_page):
    expected = ['99', None]
    actual   = get_total_page(get_lun_page)
    assert  actual in expected
    
def test_find_all_aprts(get_lun_page):
    expected = [1 ,'*** error', None]
    actual   = len(find_all_aprts(get_lun_page))
    assert actual in expected
    
def test_get_total_price(get_lun_page):
    soup = bs(get_lun_page, features='html.parser')
    
    expected = ['165\xa0000 $' ,'*** error', None]
    actual   = get_total_price(soup)
    assert  actual in expected

def test_get_rooms(get_lun_page):
    soup = bs(get_lun_page, features='html.parser')
    
    expected = ['1 комната' ,'*** error', None]
    actual   = get_rooms(soup)
    assert  actual in expected

def test_get_price_per_m(get_lun_page):
    soup = bs(get_lun_page, features='html.parser')
    
    expected = ['3367 $ за м²' , None]
    actual   = get_price_per_m(soup)
    assert  actual in expected

def test_get_level(get_lun_page):
    soup = bs(get_lun_page, features='html.parser')
    
    expected = ['2 из 9' ,'*** error', None]
    actual   = get_level(soup)
    assert  actual in expected

def test_get_area(get_lun_page):
    soup = bs(get_lun_page, features='html.parser')
    
    expected = ['49 / 20 / 18 м²' ,'*** error', None]
    actual   = get_area(soup)
    assert  actual in expected

def test_get_year(get_lun_page):
    soup = bs(get_lun_page, features='html.parser')
    
    expected = ['2013' , None]
    actual   = 'год постройки' + get_year(soup)
    assert  actual in expected

def test_get_type(get_lun_page):
    soup = bs(get_lun_page, features='html.parser')
    
    expected = ['утепленная панель', None]
    actual   = get_type(soup)
    assert  actual in expected

def test_get_address(get_lun_page):
    soup = bs(get_lun_page, features='html.parser')
    
    expected = ['ул. Златоустовская' ,'*** error', None]
    actual   = get_address(soup)
    assert  actual in expected
