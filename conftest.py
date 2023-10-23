import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session')
def config_browser():
    browser.config.window_height = 1200
    browser.config.window_width = 1920

    yield

    browser.close()
