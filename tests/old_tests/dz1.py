from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
import time

browser.config.hold_browser_open = True
browser.open('https://todomvc.com/examples/emberjs/')

s('#new-todo').type('a').press_enter()
s('#new-todo').type('b').press_enter()
s('#new-todo').type('c').press_enter()

time.sleep(1)

ss('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

s('//label[text()="b"]').element('./preceding-sibling::input').click()

s('[href="#/active"]').click()
ss('#todo-list>li').should(have.exact_texts('a', 'c'))
time.sleep(3)

s('[href="#/completed"]').click()
ss('#todo-list>li').should(have.exact_texts('b'))
time.sleep(3)
