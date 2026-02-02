## 2025-10-26 - Accessibility in Static Forms
**Learning:** Many static site templates explicitly disable default focus outlines (`outline: none`) for aesthetic reasons without providing an alternative, rendering forms inaccessible to keyboard users.
**Action:** When auditing static sites, grep for `outline: none` and verify that interactive elements like inputs and textareas have a replacement `:focus` state defined.
