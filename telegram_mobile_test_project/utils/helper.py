from selene import browser, be


def is_pop_up_message(css_locator):
    message = browser.element(css_locator)

    if message.wait_until(be.visible):
        message.click()
