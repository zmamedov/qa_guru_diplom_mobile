import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_start_messaging():
    with allure.step('Open start page of Telegram.'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Telegram")')).should(
            have.text('Telegram'))

    with allure.step('Click the button "Start Messaging".'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Start Messaging")')).click()
    with allure.step('Click the button "Continue".'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")')).click()
    with allure.step('Deny Telegram to make and manage phone calls.'):
        browser.element((AppiumBy.ID, 'com.android.packageinstaller:id/permission_deny_button')).click()

    with allure.step('Page for filling phone number is displaying.'):
        browser.element((AppiumBy.ID, 'new UiSelector().text("Your phone number")')).should(
            have.exact_text('Your phone number'))


def test_switch_theme():
    with allure.step('Open start page of Telegram.'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Telegram")')).should(
            have.text('Telegram'))

    with allure.step('Change the theme on dark'):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.ImageView')).click()
    with allure.step('Return to the light theme'):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.ImageView')).click()


def test_type_phone_number():
    with allure.step('Click the button "Start Messaging".'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Start Messaging")')).click()
    with allure.step('Click the button "Continue".'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")')).click()
    with allure.step('Deny Telegram to make and manage phone calls.'):
        browser.element((AppiumBy.ID, 'com.android.packageinstaller:id/permission_deny_button')).click()
    with allure.step('Clickt on list of values "Country".'):
        browser.element(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").instance(2)')).click()
    with allure.step('Choose the country "Australia".'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("🇦🇺 Australia")')).click()
    with allure.step('Type phone number.'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Phone number')).type('999999998989898989898989')
    with allure.step('Click the button right arrow.'):
        browser.element(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(11)')).click()

    with allure.step('Check of the correctness of number.'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Is this the correct number?")')).should(
            have.text('Is this the correct number?'))
