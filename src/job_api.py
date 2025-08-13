import os
from apify_client import ApifyClient

def fetch_jobs_from_linkedin(skills, location="India", limit=10):
    """
    Fetch jobs from LinkedIn using Apify API.
    """
    api_key = os.getenv("APIFY_API_KEY")
    if not api_key:
        raise RuntimeError("APIFY_API_KEY is missing in environment variables.")

    client = ApifyClient(api_key)

    # LinkedIn job scraper actor ID (change if you use a different one)
    run_input = {
        "queries": [f"{skills} jobs in {location}"],
        "maxItems": limit
    }

    run = client.actor("nbermansky/linkedin-jobs-scraper").call(run_input=run_input)

    jobs = []
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        jobs.append({
            "title": item.get("title"),
            "company": item.get("company"),
            "location": item.get("location"),
            "link": item.get("url")
        })

    return jobs
