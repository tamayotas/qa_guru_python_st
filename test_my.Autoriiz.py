from selene.support.shared import browser
from selene import be, have

browser.open('https://www.eldorado.ru/promo/prm-black-friday/?utm_medium=cpc&page_code=prm-black-friday')
browser.element('[class="h-personal__login"]').click()
browser.element('[class="Bm Hm"]').type('+79043845533')


