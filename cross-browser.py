from selenium import webdriver
import pyautogui
import time


web_browser = {}


def test_browsers(wd):
    try:
        """
        Include all of the browsers that have a official webdriver according to the selenium website
        Look at the https://selenium.dev/downloads/ docs on how to set all of them up
        """
        web_browser = {
            'Firefox': webdriver.Firefox,
            'Edge': webdriver.Edge,
            'Ie': webdriver.Ie,
            'Safari': webdriver.Safari,
            'Opera': webdriver.Opera,
        }

        if wd == 'Chrome':
            browser = webdriver.Chrome(r'file/to/driver/if/needed/otherwise/remove/r')
        else:
            browser = web_browser.get(wd)()

        browser.maximize_window()
        return browser

    except Exception as msg:
        print(msg)


def test_python_search(wd):
    browser = test_browsers(wd)
    browser.get('https://www.python.org/')
    time.sleep(1)
    browser.find_element_by_id('id-search-field').send_keys('style guide')
    time.sleep(1)
    pyautogui.typewrite(['enter'])
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/div/div[3]/div/section/form/ul/li[1]/h3/a').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div/div[3]/div/section/article/p[2]/i/a[1]').click()
    time.sleep(1)
    print(browser.current_url)


if __name__ == "__main__":
    browsers = ['Chrome', 'Firefox', 'Edge', 'Ie', 'Safari', 'Opera']
    for list in browsers:
        test_python_search(list)
