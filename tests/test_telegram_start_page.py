import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from telegram_mobile_test_project.utils.helper import is_pop_up_message


@allure.title('Click the button "Start Messaging"')
@allure.tag('mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'zmamedov')
@allure.feature('Elements on start page')
@allure.story('Start Page')
def test_start_messaging():
    with allure.step('Click the button "Start Messaging".'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Start Messaging")')).click()
    with allure.step('Click the button "Continue".'):
        is_pop_up_message(css_locator=(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")'))
    with allure.step('Deny Telegram to make and manage phone calls.'):
        is_pop_up_message(css_locator=
                          (AppiumBy.ANDROID_UIAUTOMATOR,
                           'new UiSelector().resourceId("com.android.packageinstaller:id/permission_deny_button")')
                          )

    with allure.step('Page for filling phone number is displaying.'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Your phone number")')).should(
            have.exact_text('Your phone number'))


@allure.title('Change the theme in the Telegram')
@allure.tag('mobile')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'zmamedov')
@allure.feature('Elements on start page')
@allure.story('Start Page')
def test_switch_theme():
    with allure.step('Open start page of Telegram.'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Telegram")')).should(
            have.text('Telegram'))

    with allure.step('Change the theme on dark.'):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.ImageView')).click()


@allure.title('Type the phone number')
@allure.tag('mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'zmamedov')
@allure.feature('Elements on start page')
@allure.story('Start Page')
def test_type_phone_number():
    with allure.step('Click the button "Start Messaging".'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Start Messaging")')).click()
    with allure.step('Click the button "Continue".'):
        is_pop_up_message(css_locator=(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")'))
    with allure.step('Deny Telegram to make and manage phone calls.'):
        is_pop_up_message(css_locator=
                          (AppiumBy.ANDROID_UIAUTOMATOR,
                           'new UiSelector().resourceId("com.android.packageinstaller:id/permission_deny_button")')
                          )
    with allure.step('Click on list of values "Country".'):
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
