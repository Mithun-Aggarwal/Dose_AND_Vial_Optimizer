"""Streamlit wrapper for the Dose & Vial Optimizer calculator."""

from __future__ import annotations

import pathlib

import streamlit as st

APP_HTML_PATH = pathlib.Path(__file__).parent / "app_static.html"


@st.cache_data(show_spinner=False)
def load_static_html() -> str:
    """Load the static calculator HTML for embedding."""
    return APP_HTML_PATH.read_text(encoding="utf-8")


def main() -> None:
    """Render the embedded Dose & Vial Optimizer."""
    st.set_page_config(
        page_title="Dose & Vial Optimizer — 70/100 mg (HCP)",
        page_icon="💉",
        layout="wide",
    )

    st.components.v1.html(
        load_static_html(),
        height=1100,
        scrolling=True,
    )


if __name__ == "__main__":
    main()
