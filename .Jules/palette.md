## 2025-02-20 - Inline JS State Management
**Learning:** This repo relies heavily on inline scripts in HTML for UI logic (e.g., hamburger menu toggling). These scripts often toggle classes but miss ARIA attribute updates.
**Action:** When modifying interactive elements here, always check the corresponding inline script block and ensure ARIA states (`aria-expanded`, etc.) are synchronized with class changes.
