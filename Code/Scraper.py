import requests
from bs4 import BeautifulSoup

URL = "https://www.horacemann.org/athletics/teams-programs"
page = requests.get(URL)

print(page)

soup = BeautifulSoup(page.content, "html.parser")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")