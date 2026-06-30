import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from query import get_answer

st.set_page_config(
    page_title="CMS Policy Assistant",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 CMS Medicare & Medicaid Policy Assistant")
st.markdown("Ask questions about Medicare and Medicaid policy documents from CMS.")

st.divider()

question = st.text_input(
    "Your question:",
    placeholder="e.g. What is the definition of a Medicare Advantage beneficiary?"
)

if st.button("Get Answer", type="primary"):
    if question.strip():
        with st.spinner("Searching documents and generating answer..."):
            answer = get_answer(question)
        st.markdown("### Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question first.")

st.divider()
st.caption("Powered by LangChain + ChromaDB + Claude | Data source: CMS.gov")
