from selene.support.shared import browser

browser.open('http://duckduckgo.com/')

browser.element('[name="q"]').type('it step').press_enter()
browser.element('[href="https://itstep.org/en"]').click()
browser.element('.menu__link').click()
