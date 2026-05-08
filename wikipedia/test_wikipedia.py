from playwright.sync_api import Page, expect


def test_user_can_search_wikipedia_and_open_article(page: Page):
    page.goto("https://www.wikipedia.org/")

    page.get_by_role("searchbox").fill("University of Chicago")
    page.keyboard.press("Enter")

    expect(page).to_have_url(lambda url: "University_of_Chicago" in url)
    expect(page.get_by_role("heading", name="University of Chicago")).to_be_visible()