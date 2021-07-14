

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_contains_add_to_basket_button(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    button_name = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert button_name, 'button isn\'t found'
