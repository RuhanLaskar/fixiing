## 2024-05-22 - Persistent Modals & Keyboard Access
**Learning:** Initial modal interruptions ("fake site warnings") are hostile if they lack keyboard dismissibility (Escape key, Tab-able close button) and persistence.
**Action:** Always wrap close icons in `<button>` with `aria-label`, support `Escape` key, and use `localStorage` to remember dismissal.
