import re
from playwright.sync_api import sync_playwright


def test_user_can_search_wikipedia_and_open_article():
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()

        # Arrange
        page.goto("https://www.wikipedia.org/")

        # Act
        page.get_by_role("searchbox").fill("University of Chicago")
        page.keyboard.press("Enter")

        # Assert
        page.wait_for_url(re.compile(".*University_of_Chicago.*"))
        assert "University_of_Chicago" in page.url
        assert page.get_by_role("heading", name="University of Chicago").is_visible()

        page.screenshot(path="screenshots/wikipedia_search.png")

        browser.close()
