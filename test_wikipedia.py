from playwright.sync_api import sync_playwright


def test_wikipedia_search():
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()

        page.goto("https://www.wikipedia.org/")
        page.get_by_role("searchbox").fill("University of Chicago")
        page.keyboard.press("Enter")

        page.wait_for_url("**/University_of_Chicago")
        assert "University of Chicago" in page.title()

        browser.close()
