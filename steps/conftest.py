# conftest.py
from playwright.sync_api import sync_playwright, Page
import pytest

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        page = browser.new_page(no_viewport=True)
        yield page
        browser.close()
