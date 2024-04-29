import pytest

from DDframework.utilities.credential_reader import read_credentials_from_csv
from DDframework.utilities.selenium_utilities import verify_if_login_success
@pytest.mark.parametrize("username,password", read_credentials_from_csv("C://python312//automation task 27_DDF//DDframework//credential_data//credentials.csv"))
def test_login(browser, username, password):
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login(browser, username, password)
    verify_if_login_success(browser)