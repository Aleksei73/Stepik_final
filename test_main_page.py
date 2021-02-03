import time
'''link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_cart_button(browser):
    browser.get(link)
    time.sleep(5)
    x = 0
    try:
        browser.find_element_by_css_selector('button[class*="btn-add-to-basket"]')
        x = 1
    except Exception:
        pass
    finally:
        assert x == 1, 'Элемент не найден'
        '''

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
