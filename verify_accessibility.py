import os
from playwright.sync_api import sync_playwright

def verify_accessibility():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/index.html")

        # 1. Verify Warning Modal
        print("Verifying Warning Modal...")
        modal = page.locator("#fakeSiteWarningModal")
        # Wait for modal to be visible (it has a style.display set in JS)
        try:
            modal.wait_for(state="visible", timeout=2000)
            print("Modal is visible.")
        except:
             print("Modal did not appear.")

        if modal.is_visible():
            role = modal.get_attribute("role")
            aria_modal = modal.get_attribute("aria-modal")
            aria_labelledby = modal.get_attribute("aria-labelledby")

            if role == "dialog" and aria_modal == "true" and aria_labelledby == "warning-title":
                print("Modal ARIA attributes are correct.")
            else:
                print(f"Modal ARIA attributes incorrect: role={role}, aria-modal={aria_modal}, aria-labelledby={aria_labelledby}")

            # Verify Close Button
            close_btn = page.locator(".warning-close-btn")
            tag_name = close_btn.evaluate("el => el.tagName.toLowerCase()")
            aria_label = close_btn.get_attribute("aria-label")

            if tag_name == "button" and aria_label == "Close warning":
                 print("Close button is a <button> with correct aria-label.")
            else:
                 print(f"Close button incorrect: tag={tag_name}, aria-label={aria_label}")

            # Close the modal
            close_btn.click()
            print("Clicked close button.")
            # Wait a bit for transition/JS
            page.wait_for_timeout(500)
            if not modal.is_visible():
                print("Modal closed successfully.")
            else:
                print("Modal did not close.")

        # 2. Verify Hamburger Menu
        print("\nVerifying Hamburger Menu...")
        hamburger = page.locator("#hamburger-btn")

        # Ensure mobile view
        page.set_viewport_size({"width": 375, "height": 667})

        expanded_initial = hamburger.get_attribute("aria-expanded")
        label = hamburger.get_attribute("aria-label")

        if label == "Toggle navigation menu" and expanded_initial == "false":
            print("Hamburger initial state correct.")
        else:
             print(f"Hamburger initial state incorrect: label={label}, expanded={expanded_initial}")

        if hamburger.is_visible():
            hamburger.click()
            expanded_after = hamburger.get_attribute("aria-expanded")
            if expanded_after == "true":
                print("Hamburger expanded state toggled to true.")
            else:
                print(f"Hamburger expanded state failed to toggle: {expanded_after}")
        else:
            print("Hamburger button is not visible even in mobile view.")

        # Screenshot
        os.makedirs("/home/jules/verification", exist_ok=True)
        page.screenshot(path="/home/jules/verification/verification.png")
        print("Screenshot saved.")

        browser.close()

if __name__ == "__main__":
    verify_accessibility()
