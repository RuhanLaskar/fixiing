## 2025-05-23 - Accessible Warning Modals
**Learning:** Blocking modals like "Fake Site Warnings" must be accessible (ARIA roles, focus management, keyboard interaction) because they prevent access to the entire site until dismissed. A `<span>` close button is a major barrier for keyboard users.
**Action:** Always use `<button>` for close actions, add `role="dialog"`, `aria-modal="true"`, and ensure the close button is reachable via keyboard.
