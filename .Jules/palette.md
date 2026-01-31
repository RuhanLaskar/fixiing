## 2024-05-22 - Critical Modal Accessibility
**Learning:** High-priority "Warning" modals that appear on load must be immediately dismissible via keyboard (Escape key) and screen readers (semantic button), or they become a major barrier.
**Action:** Always check `window.onload` or `DOMContentLoaded` scripts for blocking modals and ensure they have accessible close mechanisms.
