## 2025-02-18 - Input Focus Indicators
**Learning:** The design system removes default focus outlines (`outline: none`) on inputs for aesthetic reasons but didn't provide a replacement. This hurts keyboard accessibility.
**Action:** When removing outlines, always add a visible alternative like a `border-color` change or `box-shadow` on `:focus`.
