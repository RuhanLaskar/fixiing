## 2025-10-26 - Critical Accessibility Fixes in Static Sites
**Learning:** Static sites often neglect basic semantic HTML form associations (label `for` + input `id`), which breaks screen reader navigation completely.
**Action:** Always verify form accessibility with a screen reader or inspector first. Simple semantic fixes (adding `id` and `for`) provide high value with zero risk.

**Learning:** "Fake Site" warning modals are often implemented hastily with `span` elements and `onclick` handlers, excluding keyboard users.
**Action:** Always refactor interactive `span`s to `<button>` elements with `aria-label` and style resets to maintain visual fidelity while fixing accessibility.
