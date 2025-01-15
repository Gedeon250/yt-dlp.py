from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Change to headless=False to view the browser
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())  # Should print "Example Domain"
    browser.close()

