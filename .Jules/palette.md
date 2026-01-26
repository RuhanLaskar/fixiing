## 2026-01-26 - Form Accessibility & Focus States
**Learning:** The contact form had labels but they weren't associated with inputs, and focus styles were removed globally for inputs without replacement. This makes the form unusable for screen readers and confusing for keyboard users.
**Action:** Always check `for`/`id` pairs on forms and verify visible focus states when `outline: none` is present.
