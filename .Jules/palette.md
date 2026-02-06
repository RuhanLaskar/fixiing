## 2026-02-06 - Form Accessibility & Focus States
**Learning:** Forms inputs were missing `id` attributes and their labels lacked `for` attributes, breaking screen reader association. Additionally, `outline: none` was used without providing a replacement focus indicator, making keyboard navigation difficult.
**Action:** Always ensure inputs have unique `id`s paired with `label for="..."`. When removing default outlines, provide a clear visual alternative (e.g., border color change, box-shadow) for the `:focus` state.
