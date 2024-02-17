from . import Framework
from Framework import driver


def test_re_login(driver):
    Framework.WebDriverBase.open(driver, "http://127.0.0.1:8080")
