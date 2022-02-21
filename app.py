import streamlit as st

from bbquote783.lib import get_quote

quote = get_quote()  # assuming the function returns an author and a quote

f"This is my quote:  {quote}"

