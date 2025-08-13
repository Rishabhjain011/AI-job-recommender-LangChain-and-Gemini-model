# AI-Job-Recommender-System-using-Langchain-Gemini-
---<img width="1908" height="947" alt="Screenshot 2025-08-13 153705" src="https://github.com/user-attachments/assets/93834b8b-5f92-49ca-b6af-aa634fac6293" />

---
### **🌟 Features**

- 📄➡️🔤 PDF → Text with PyMuPDF (fitz)

- 🧩🤝 LangChain + Gemini chains: Summary, Gaps, Roadmap, Keywords (single LLM, reusable chains)

- 🖥️⚡ Streamlit UI: upload resume → view insights → fetch jobs

- 💼🔎 LinkedIn jobs via Apify with sensible inputs (title, location, rows)

---
### **A Streamlit app that:**
<img width="1765" height="376" alt="Screenshot 2025-08-13 153729" src="https://github.com/user-attachments/assets/b2f0174b-2d80-4de3-92c4-fbb16b44e0f6" />
<img width="1814" height="808" alt="Screenshot 2025-08-13 153957" src="https://github.com/user-attachments/assets/93390d1b-916e-40e4-b2cd-ceacc7e84cd2" />
<img width="1853" height="913" alt="Screenshot 2025-08-13 154006" src="https://github.com/user-attachments/assets/a8ccc2bd-835e-4cda-bcef-88aa97056a7e" />
<img width="1894" height="779" alt="Screenshot 2025-08-13 154015" src="https://github.com/user-attachments/assets/3ed43757-273d-4007-86e4-8302d5e44d91" />


- 📄➡️📝 Extracts text from a PDF resume

- 🧠✨ Uses Gemini (via LangChain) to summarize, find skill gaps, suggest a roadmap, and generate job-search keywords

- 🔍🌐 (Optional) Fetches LinkedIn jobs via Apify using those keywords

---

### 🗂️**Project Structure**
<img width="1101" height="501" alt="Screenshot 2025-08-13 160348" src="https://github.com/user-attachments/assets/da55feaa-6a43-4a41-a41b-debc723d8b91" />


- app.py – Streamlit UI: loads PDF, runs chains, displays results, and fetches jobs. 

- src/helper.py – extract_text_from_pdf(uploaded_file). 

- src/llm_gemini.py – cached Gemini LLM + chains (chain_summary, chain_gaps, chain_keywords, chain_roadmap). 

- src/job_api.py – fetch_linkedin_jobs(search_query, location, rows) calling an Apify actor. \

---
### **🧰 Requirements**

- 🐍 Python 3.10+ (recommended)

- Packages: streamlit, PyMuPDF, python-dotenv, apify-client, langchain, langchain-core, langchain-google-genai, google generativeai.
---

### **🔐 Configuration**

Create .env in the project root (do not commit this file):

- ➡️GOOGLE_API_KEY=your_gemini_key_here

- ➡️APIFY_API_TOKEN=your_apify_token_here

- ➡️.gitignore already excludes .env and related secret files. 

---
### 📄**Notes**

- 🔑 Gemini key is required for the LLM chains. The app loads the key and builds a cached Gemini client. 

- 🌐Apify token is required only if you want to fetch LinkedIn jobs. The call will raise a clear error if it’s missing.
---

### ▶️**Run the App**

From your project folder (venv active):

python -m streamlit run app.py

---
### 🛠️**How It Works**

- **📤Upload PDF → Extract text**

extract_text_from_pdf(uploaded_file) uses PyMuPDF to read the PDF stream. 


- **🧠Gemini (LangChain) analysis**

The app builds a single get_llm() instance and composes prompt chains to produce summary, gaps, and roadmap. 

 
 - **🏷️ Generate keywords → Fetch jobs**
 
The keywords chain returns a comma-separated list; the app cleans it and runs the first few queries to avoid a single   overly long search term. 

Each query is sent to fetch_linkedin_jobs(title, location, rows) and results are merged & de-duplicated. 

Jobs are then rendered with title, company, location, and link. 


- **⚙️ Apify actor input**

The job fetcher builds a run_input with title, location, rows, sortby, freshness, and experience, then runs the actor and returns items from the dataset. 

---
### **🔒Security**

- 🚫Never commit .env (ignored by .gitignore). 

- ✅Consider committing a safe template like .env.example with variable names only.
---

### **🧪Scripts & Commands**

- **Create venv:**

py -3 -m venv .venv

.\.venv\Scripts\Activate.ps1


- **Install deps**
  
pip install -U streamlit PyMuPDF python-dotenv apify-client \

langchain langchain-core langchain-google-genai google-generativeai


- **Run app**

python -m streamlit run app.py



