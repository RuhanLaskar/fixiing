## 2025-10-26 - Custom Focus States for Inputs
**Learning:** The design system removes default focus outlines on inputs (`outline: none`) but often fails to provide a replacement, hurting keyboard accessibility.
**Action:** When working on forms, always ensure `input:focus` and `textarea:focus` define a visual indicator. For this design system, thickening and coloring the bottom border (e.g., `border-bottom: 2px solid var(--secondary-color)`) is the established pattern to maintain the aesthetic while fixing accessibility.
