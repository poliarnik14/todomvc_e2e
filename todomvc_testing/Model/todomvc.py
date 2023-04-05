from selene import have, command
from selene.support.shared import browser
completed = have.css_class('completed')

class TodoMVC:
    def __init__(self):
        self.todo_list = browser.all('#todo-list>li')

    def open(self):
        browser.open('https://todomvc4tasj.herokuapp.com/')
        app_loaded = "return $._data($('#clear-completed')[0], 'events')" \
                     ".hasOwnProperty('click')"
        browser.should(have.js_returned(True, app_loaded))
        return self

    def add(self, *todos: str):
        for todo in todos:
            browser.element('#new-todo').type(todo).press_enter()
        return self

    def given_opened(self, *todos: str):
        self.open()
        self.add(*todos)

    def should_be(self, *todos: str):
        self.todo_list.should(have.exact_texts(todos))
        return self

    def should_size(self, expect_size):
        self.todo_list.should(have.size(expect_size))

    def edit_double_click(self, todo, new_text):
        self.todo_list.element_by(have.exact_text(todo)).double_click()
        return self.todo_list.element_by(have.css_class('editing')).element('.edit').perform(command.js.set_value(new_text)).press_enter()

    def toggle_click(self, todos: str):
        self.todo_list.element_by(have.exact_text(todos)).element('.toggle').click()

    def clear_completed(self):
        browser.element('#clear-completed').click()
        return self

    def completed_click(self):
        browser.element('[href="#/completed"]').click()
        return self

    def all_click(self):
        browser.element('[href="#/"]').click()
        return self

    def hover_destroy(self, todo: str):
        self.todo_list.element_by(have.exact_text(todo)).hover().element('.destroy').click()