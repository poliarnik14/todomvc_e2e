from selene import browser
from selene.support.jquery_style_selectors import s

browser.open("https://www.example.com")
checkbox = s("#checkbox_id")
checkbox.toggle()
