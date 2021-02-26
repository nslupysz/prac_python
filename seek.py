import requests
from bs4 import BeautifulSoup

job = "react"
region ="Auckland"
seek_url = f"https://www.seek.co.nz/{job}-jobs/in-{region}"

def max_page():
    r = requests.get(seek_url)
    soup = BeautifulSoup(r.text, "html.parser")

    pagination = soup.find("p",{"class":"mRR2Am8"})
    pages = pagination.find_all('span')
    anchors =[]
    for page in pages:
        anchors.append(page.string)
    last_page = anchors[-1]
    return last_page


def extract_jobs(last_page):
    jobs =[]
    for n in range(int(last_page)):
        goToUrl = f"{seek_url}?page={n+1}"
        r = requests.get(goToUrl)
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find_all("article")

        for result in results:
            title = result.find("a",{"data-automation":"jobTitle"}).string
            if result.find("a",{"data-automation":"jobCompany"}) is not None:
                company = result.find("a",{"data-automation":"jobCompany"}).string
            else:
                company = "N/A"

            location = result.find("a",{"data-automation":"jobLocation"}).string
            
            if result.find("span",{"data-automation":"jobSalary"}) is not None:
                salary = result.find("span",{"data-automation":"jobSalary"}).find("span").string
            else:
                salary = "N/A"

            description = result.find("span",{"data-automation":"jobShortDescription"}).string

            link_id = result.get("data-job-id")
            link = f"https://www.seek.co.nz/job/{link_id}"

            job = {'title': title, 'company': company, 'location': location, 'salary': salary, 'description':description, 'link':link}
            jobs.append(job)

    return jobs
            
        
