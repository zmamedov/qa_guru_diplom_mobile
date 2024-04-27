from appium.options.android import UiAutomator2Options

remote_url = 'http://127.0.0.1:4723'


def to_driver_options():
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'android',
        'deviceName': 'emulator-5554',
        'appWaitActivity': 'org.wikipedia.*',
        'app': 'XXXXXXXXXX',
    })

    return options
