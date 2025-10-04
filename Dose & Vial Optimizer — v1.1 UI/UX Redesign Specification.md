Dose & Vial Optimizer — v1.1 UI/UX Redesign Specification

Version: Draft 1.0
Date: 2025-10-04
Owner: Mithun Aggarwal
Purpose: Align the Dose & Vial Optimizer tool’s UI/UX with the look and feel of the broader Patient Treatment Portal (see reference screenshot).

1. Background

The current calculator (v1.0) is functional but styled in an “app-like” format with orange/white cards, accent banners, and badges. While aligned with GSK branding, the design feels different from the surrounding portal, which uses a clean, clinical form-based aesthetic with dark red highlights, muted grey labels, and white-space heavy layouts.

The goal of v1.1 is to harmonize the calculator with the Patient Treatment Confirmation UI, improving trust, readability, and user experience for HCPs.

2. Design Objectives

Visual alignment: Make the calculator look and feel like part of the patient portal, not a standalone widget.

Clinical readability: Reduce decorative elements, emphasize key clinical numbers.

Trust & compliance: Use tone and typography that match medical forms.

Consistency: Match input fields, disclaimers, and call-to-action buttons to the patient form.

3. Current vs Desired Design
3.1 Layout

Current (v1.0):

Card-based sections with shadows and orange backgrounds.

Calculator summary and recommendation inside colored boxes.

Desired (v1.1):

White background throughout.

Sections separated by whitespace and thin grey dividers.

Results shown in bold text callouts, not banners.

3.2 Color Palette

Current: Orange-heavy (cards, banners, buttons, accents).

Desired:

Primary text: #2b2b2b (dark grey/black).

Headings & critical text: #7d0000 (dark clinical red).

Labels: #6b6b6b (muted grey).

Background: White.

Accents (buttons, highlights): Orange #ff6a00 (used sparingly).

3.3 Typography

Current: System UI, mix of muted + colored text.

Desired:

Headings bold and dark red.

Labels smaller, muted grey.

Key results (total dose, recommendation) in bold dark grey or red, inline with text, not in banners.

3.4 Input Fields

Current: Pills and orange badges for vial strengths, rounded boxes for inputs.

Desired:

Inputs styled like form fields: white background, thin grey borders.

Vial strengths shown as static text or disabled fields, not pills.

Radio buttons styled like simple form choices (Yes/No style, not inline pills).

3.5 Results Presentation

Current:

Summary in orange info box.

Recommendation in green box.

Best option highlighted with badges (“Least waste”, “Fewest vials”).

Desired:

Show dose requirement as a bold clinical note, e.g.:

“Required dose: 203 mg (rounded up)”

Show recommendation inline:

“Recommended combination: 3 × 70 mg vials (Total 210 mg; Waste 7 mg; 3.3%).”

Table simplified: white rows, grey dividers, bold best option row (no badges).

3.6 Disclaimer & Guidance

Current: Banner at top in orange with text.

Desired:

Disclaimer text matches tone of clinical form:

“Please review the calculated dose and vial combination before prescribing. No underdosing and single-patient use are assumed.”

Styled in red text, positioned above inputs, similar to “Please review these details” in the reference form.

3.7 Buttons & Actions

Current: Orange buttons with rounded corners (“Calculate options”, “Reset”, “Print/Save PDF”).

Desired:

Primary CTA (“Calculate options”) → Orange button, flat style.

Secondary CTAs (“Reset”, “Print/Save PDF”) → Grey text buttons (outlined).

Button alignment: right side, consistent spacing.

4. UX Improvements

Inline calculations: Consider auto-updating dose requirement once weight + regimen entered (instead of requiring “Calculate options” click).

PDF export styling: Print layout should mimic a clinical form (white background, structured table, disclaimers at bottom).

Accessibility: Ensure color contrast meets WCAG 2.1 AA (red/grey must be legible).

Tone alignment: Use phrasing from patient form:

Replace “Recommendation will appear here” with “Please review the calculated dose and vial combination.”

5. Technical Implementation Notes

Keep core JS/logic unchanged.

Replace CSS variables to adopt new palette.

Remove card shadows & colored banners.

Redesign HTML structure for sections:

Inputs → form-like divs.

Results → inline notes & plain table.

Use a CSS class system to mirror patient portal (form-section, field-label, review-note).

6. Deliverables for v1.1

Updated app_static.html with new HTML structure + CSS (aligned to portal style).

Revised Streamlit wrapper (no functional changes, only styling if needed).

Updated README.md documenting the v1.1 redesign.

Branch feature/ui-redesign-v1.1 for code changes.

7. Success Criteria

Visual consistency with the Patient Treatment Confirmation form.

Simplified, clinical look and feel.

Key results are clear, bold, and readable without colored banners.

HCP feedback confirms improved usability and trust.