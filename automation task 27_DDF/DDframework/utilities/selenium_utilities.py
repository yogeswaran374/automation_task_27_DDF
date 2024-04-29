import os


def verify_if_login_success(browser):
    try:
        assert "Dashboard" in browser.current_url.lower(), "login has failed"
    except AssertionError as e:
        save_screenshot(browser)
        raise AssertionError("login as failed") from e

def save_screenshot(browser):
    screenshot_directory = os.path.join(os.getcwd(), 'screenshot')
    os.makedirs(screenshot_directory,exist_ok=True)
    screenshot_path = os.path.join((screenshot_directory, f"Login_failure.png"))
    driver.save_screenshot(screenshot_path)
    print(f"screenshot saved at : {screenshot_path}")