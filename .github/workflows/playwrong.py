import os
from playwright.sync_api import Page, expect

def deploy(page: Page):
    print(f'🐞 os.environ.get("SUPER_SECRET"): {os.environ.get("SUPER_SECRET")}')
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()