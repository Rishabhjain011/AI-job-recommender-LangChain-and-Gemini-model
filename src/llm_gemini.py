import os
from functools import lru_cache
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

@lru_cache(maxsize=1)
def get_llm(model: str = "gemini-1.5-flash", temperature: float = 0.5, max_tokens: int = 1024):
    """
    Initialize and cache the Google Gemini LLM.
    Requires GOOGLE_API_KEY or GEMINI_API_KEY in environment variables.
    """
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Set GOOGLE_API_KEY (or GEMINI_API_KEY) in your .env file.")
    
    return ChatGoogleGenerativeAI(
        google_api_key=api_key,
        model=model,
        temperature=temperature,
        max_output_tokens=max_tokens,
    )

def chain_summary(llm=None):
    """
    Returns a chain for summarizing resumes into skills, education, and experience.
    """
    llm = llm or get_llm()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a concise and professional resume summarizer."),
        ("human", "Summarize this resume focusing on skills, education, and experience:\n\n{resume_text}")
    ])
    return prompt | llm | StrOutputParser()

def chain_gaps(llm=None):
    """
    Returns a chain for identifying missing skills, certifications, and experiences.
    """
    llm = llm or get_llm()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You analyze resumes and clearly identify gaps."),
        ("human", "List missing skills, certifications, and experiences as bullet points:\n\n{resume_text}")
    ])
    return prompt | llm | StrOutputParser()

def chain_keywords(llm=None):
    """
    Returns a chain for extracting ONLY job titles and search keywords (comma-separated).
    """
    llm = llm or get_llm()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Return ONLY a comma-separated list of job titles and search keywords. No extra text."),
        ("human", "Based on this resume summary, output the list:\n\n{summary}")
    ])
    return prompt | llm | StrOutputParser()

def chain_roadmap(llm=None):
    """
    Returns a chain for creating a practical 90-day improvement roadmap.
    """
    llm = llm or get_llm()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You create practical 90-day improvement roadmaps."),
        ("human", "Based on this resume, suggest a roadmap (skills, certifications, industry exposure):\n\n{resume_text}")
    ])
    return prompt | llm | StrOutputParser()
