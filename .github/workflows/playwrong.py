import os
from playwright.sync_api import Page, expect

def test_get_started_link(page: Page):
    print(f"🐞 os.environ: {os.environ}")
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()