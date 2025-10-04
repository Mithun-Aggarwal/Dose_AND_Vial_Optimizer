# Dose & Vial Optimizer (Streamlit Wrapper)

A lightweight Streamlit wrapper that embeds the existing **Dose & Vial Optimizer** HTML calculator. The calculator logic remains fully client-side and unchanged while Streamlit provides a simple deployment surface for local use or Streamlit Community Cloud.

## Features
- Embeds the provided `app_static.html` calculator exactly as delivered.
- Preserves vial strengths (70 mg and 100 mg), dosing rules, accessibility affordances, and disclaimer messaging.
- Applies a GSK-aligned Streamlit theme (orange/white palette).
- Zero backend dependencies; purely static calculator embedded in Streamlit.

## Repository Layout
```
.
├── app_static.html           # Provided calculator (logic unchanged)
├── streamlit_app.py          # Streamlit wrapper that embeds the HTML
├── requirements.txt          # Python dependencies (Streamlit only)
├── .streamlit/config.toml    # Theme configuration
├── Makefile                  # Convenience commands (run/freeze)
├── .editorconfig             # Consistent editor settings
└── .gitignore                # Standard Python/Streamlit ignores
```

## Prerequisites
- Python 3.10 or newer
- `pip` for dependency management

## Quick Start (Local)
1. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch Streamlit:
   ```bash
   streamlit run streamlit_app.py
   ```
4. Your browser will open to the running app. The embedded calculator retains its original functionality, including print/save support and dosing validation.

> Tip: `make run` is available if you have `make` installed.

## Deploy to Streamlit Community Cloud
1. Push this repository to GitHub (public or private).
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click **Deploy an app** and select the repo/branch.
4. Set the main file path to `streamlit_app.py`.
5. Choose Python 3.10 (or later) and let Streamlit install dependencies from `requirements.txt`.
6. Deploy—no additional secrets or configuration required.

## Screenshot Placeholder
_Add a screenshot of the running app here after deployment._

## Support & Maintenance
- Calculator logic remains within `app_static.html`. Update that file directly if changes are required.
- The Streamlit wrapper is intentionally minimal—no backend services or analytics are included per the requirement.
- For issues, open a GitHub issue or contact the project maintainer.

## License
MIT License. See `LICENSE` (add if not already present).
