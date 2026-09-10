---
name: Executive Precision
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1b1b1b'
  on-surface-variant: '#3d4a38'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#6d7b66'
  outline-variant: '#bccbb3'
  surface-tint: '#016e00'
  primary: '#016e00'
  on-primary: '#ffffff'
  primary-container: '#00b700'
  on-primary-container: '#013f00'
  inverse-primary: '#4ce33b'
  secondary: '#006879'
  on-secondary: '#ffffff'
  secondary-container: '#7de6ff'
  on-secondary-container: '#006778'
  tertiary: '#ad2665'
  on-tertiary: '#ffffff'
  tertiary-container: '#ff68a5'
  on-tertiary-container: '#6d003a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#77ff61'
  primary-fixed-dim: '#4ce33b'
  on-primary-fixed: '#002200'
  on-primary-fixed-variant: '#015300'
  secondary-fixed: '#a9edff'
  secondary-fixed-dim: '#6bd5ed'
  on-secondary-fixed: '#001f26'
  on-secondary-fixed-variant: '#004e5b'
  tertiary-fixed: '#ffd9e3'
  tertiary-fixed-dim: '#ffb0c9'
  on-tertiary-fixed: '#3e001f'
  on-tertiary-fixed-variant: '#8d024d'
  background: '#fcf9f8'
  on-background: '#1b1b1b'
  surface-variant: '#e5e2e1'
  text-muted: '#848484'
  surface-subtle: '#F8F9FA'
  border-light: '#E5E7EB'
typography:
  display-lg:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '300'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Public Sans
    fontSize: 36px
    fontWeight: '300'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  headline-sm:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.08em
  quote:
    fontFamily: Public Sans
    fontSize: 22px
    fontWeight: '300'
    lineHeight: 34px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  section-gap: 120px
---

## Brand & Style

The design system is crafted for a "senior partner-led boutique" environment, where rigor meets human-centric leadership. The brand personality is authoritative yet approachable, reflecting a firm that navigates complex organizational challenges with surgical precision and strengths-based empathy.

The visual direction follows a **Modern Corporate Minimalism** style. It leverages high-end editorial layouts characterized by expansive whitespace, a strictly controlled palette, and a sophisticated typographic hierarchy. By avoiding unnecessary decoration, the design allows the firm's insights and expertise to take center stage, signaling confidence to enterprise and government evaluators. 

Key visual principles include:
- **Restraint:** Color is used only as a functional tool for orientation and action.
- **Clarity:** Structured informational paths that guide users from sector expertise to tangible case studies.
- **Craft:** Subtle use of micro-interactions and refined elevation to suggest a premium service level.

## Colors

The palette is anchored in a neutral architectural foundation of stark whites, soft grays, and deep "Off-Black" (#1B1B1B) to ensure maximum readability and a professional tone. 

- **Primary Green (#00B700):** Reserved exclusively for high-priority calls to action, active states, and success indicators. It represents growth and the firm's "strengths-based" philosophy.
- **Secondary Sky Blue (#7AE3FC):** Used as a secondary accent for data visualization, category labels, or subtle background washes to differentiate service sectors.
- **Supporting Gray (#848484):** Applied to secondary metadata, captions, and de-emphasized UI elements to maintain a clear visual hierarchy.
- **Neutral Surface:** Grayscale backgrounds are used to separate content blocks, ensuring the interface feels organized and legible for government evaluators performing deep-dive audits.

## Typography

The typographic system balances the modern humanist warmth of **Public Sans** with the systematic efficiency of **Inter**.

- **Headlines:** Use Public Sans with lighter weights (300/400) for large displays to evoke a "Proxima Nova Light" aesthetic. This feels contemporary and boutique.
- **Body Text:** Inter is utilized for its exceptional legibility in long-form reports, case studies, and service descriptions.
- **Captions & Labels:** A strict "label-caps" style is used for overlines (e.g., "CASE STUDY" or "SECTOR") to provide structural cues without adding visual weight.
- **Line Height:** Generous leading is applied to body text to prevent "wall-of-text" fatigue, essential for rigorous consultancy content.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop and a **Fluid Fluid** model for mobile.

- **Grid:** A 12-column grid system is used for desktop (1280px max-width) to align complex information like "Expert Bio" cards and "Service Offering" lists.
- **Sectional Rhythms:** Large vertical gaps (120px+) between major sections emphasize the "Minimalist" aesthetic and allow the user's eyes to rest.
- **Content Reflow:** On mobile, columns collapse to a single stack, but internal card padding remains generous to preserve the premium feel.
- **Evaluator Path:** Layouts are structured linearly: Problem Statement → Methodology (Service) → Evidence (Case Study) → Personnel (Expert).

## Elevation & Depth

To maintain a "Cutting-edge but Corporate" feel, the system avoids heavy drop shadows in favor of **Tonal Layers** and **Low-Contrast Outlines**.

- **Surface Tiering:** Use light gray backgrounds (#F8F9FA) to define card containers or distinct content sections against the white canvas.
- **Borders:** Define interactive elements (inputs, cards) with 1px solid borders in a soft gray (#E5E7EB).
- **Interactive Depth:** On hover, cards should not "lift" with heavy shadows. Instead, use a subtle 1px Primary Green border or a very soft, diffused ambient shadow (0px 4px 20px rgba(0,0,0,0.04)) to indicate interactivity.
- **Transparency:** Glassmorphism is used sparingly, limited to the main navigation header to maintain context while scrolling through long-form content.

## Shapes

The shape language is **Soft (0.25rem)**. This choice strikes a balance between the "Sharp" corporate aesthetic of traditional law/finance and the "Rounded" friendliness of modern SaaS. It suggests precision and rigor while remaining modern and approachable.

- **Primary Buttons:** Use the standard 0.25rem radius.
- **Cards:** 0.5rem (rounded-lg) for container edges to provide a slight visual distinction from interactive buttons.
- **Form Inputs:** Strict 0.25rem radius to maintain a professional, structured appearance.

## Components

- **Buttons:** 
  - *Primary:* Solid Green (#00B700) with White text. Bold, sans-serif, uppercase label.
  - *Secondary:* Transparent with a Green or Sky Blue border.
- **Cards:** White background with a 1px soft gray border. Use a "label-caps" overline for the sector name. Headers in Public Sans.
- **Expert Profiles:** Small circular or soft-square headshots paired with a name (bold) and title (Supporting Gray).
- **Service Lists:** Use custom iconography (monoline, Green) to represent different consultancy sectors.
- **Input Fields:** Minimalist design with 1px gray borders. Active state uses a Primary Green border glow.
- **Breadcrumbs:** Crucial for the evaluator path; small-scale Inter text to help users navigate from "Federal Services" back to "Overview."
- **Call-out Quotes:** Stylized with a Sky Blue left-border and Public Sans Italic to highlight key leadership insights or client testimonials.