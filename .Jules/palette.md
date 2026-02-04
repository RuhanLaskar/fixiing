## 2024-05-22 - Accessible Modals on Load
**Learning:** Modals that appear on page load must be immediately accessible to keyboard users. If the close button is not a focusable element (like a span) and there is no Escape key support, keyboard-only users are trapped and cannot access the site content.
**Action:** Always use `<button>` for close actions, implement `role="dialog"`, `aria-modal="true"`, and ensure `Escape` key dismisses the modal.
