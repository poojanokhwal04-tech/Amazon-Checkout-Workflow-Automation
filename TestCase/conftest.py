from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver import Firefox,FirefoxOptions
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities import ReadConfigini
from Utilities.ReadScreenshotPath import screenshotpath
import pytest

@pytest.fixture
def setup(request):

    url=ReadConfigini.read_configuration_file("common info", "url")
    browser=ReadConfigini.read_configuration_file("common info", "browser")

    if browser=="firefox":
        o = FirefoxOptions()
        driver = Firefox(options=o)
    elif browser=="edge":
        o = EdgeOptions()
        o.add_experimental_option('detach', True)
        driver = Edge(options=o)
    else:
        o = ChromeOptions()
        o.add_experimental_option('detach', True)
        driver = Chrome(options=o)

    wait=WebDriverWait(driver,20)
    testname = request.node.name
    path = screenshotpath(testname)

    request.cls.driver=driver
    request.cls.wait=wait
    request.cls.path=path

    driver.get(url)
    yield path
    driver.quit()