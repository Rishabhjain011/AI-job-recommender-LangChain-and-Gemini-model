import streamlit as st
from dotenv import load_dotenv
from pathlib import Path
import os

# Load .env from project root
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

from src.helper import extract_text_from_pdf
from src.llm_gemini import get_llm
from src.job_api import fetch_jobs_from_linkedin

st.set_page_config(page_title="AI Job Recommender", page_icon="📄", layout="wide")

st.title("📄 AI Job Recommender (LangChain + Gemini)")
st.markdown("Upload your resume and get job recommendations based on your skills and experience from LinkedIn.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file is not None:
    try:
        resume_text = extract_text_from_pdf(uploaded_file)
        st.success("Resume uploaded and processed successfully!")
        
        llm = get_llm()

        with st.spinner("Extracting skills from your resume..."):
            prompt = f"Extract a list of top 5 technical skills from this resume text:\n\n{resume_text}"
            skills_response = llm.invoke(prompt)
            skills = skills_response.content if hasattr(skills_response, "content") else skills_response
            st.write("### Extracted Skills", skills)

        with st.spinner("Fetching job recommendations..."):
            jobs = fetch_jobs_from_linkedin(skills, location="India", limit=5)
            if jobs:
                st.write("## Recommended Jobs")
                for job in jobs:
                    st.write(f"**{job['title']}** at {job['company']} — {job['location']}")
                    st.write(f"[Apply Here]({job['link']})")
                    st.write("---")
            else:
                st.warning("No jobs found. Try again with different skills or location.")

    except Exception as e:
        st.error(f"Error: {e}")
