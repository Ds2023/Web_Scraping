import requests
from bs4 import BeautifulSoup
import csv


def job_categories():
    #Available job categories and links
    url = "https://www.careerpointkenya.co.ke/"
    response = requests.get(url).text
    #print(response.status_code)
    s = BeautifulSoup(response,"html.parser")
    group = s.find_all("li",class_="menu-item-type-taxonomy")
    for category in group:
        items = category.find("a")
        links = category.find("a")["href"]
        print(f'''
        Category : {items.text}
        Link : {links}
        ''')


def main_headers():
    #headers and their links
    url = "https://www.careerpointkenya.co.ke/"
    response = requests.get(url).text
    s = BeautifulSoup(response,"html.parser")
    main_links = s.find_all("li",class_="menu-item-type-post_type")
    for i in main_links:
        links = i.find("a")["href"]
        print(links)
        headers = i.find("span",class_="menu-text")
        while headers != None:
            print(headers.text.strip())
            break


def newest_jobs():
    #new jobs posted
    url2 = "https://www.careerpointkenya.co.ke/jobs/"
    response2 = requests.get(url2).text
    #print(response2.status_code)
    soup = BeautifulSoup(response2,"html.parser")
    new = soup.find_all("div",class_="fusion-post-content post-content")
    for job in new:
        jobs = job.find("a").text
        print(jobs)


def recruitment_firms():
    #recruitment firms and links
    url3 = "https://www.careerpointkenya.co.ke/recruitment-agencies-kenya/"
    response3 = requests.get(url3).text
    #print(response3.status_code)
    v = BeautifulSoup(response3,"html.parser")
    agency = v.find("div",class_="post-content")
    agents = agency.find_all("p",style="text-align: justify;")
    for agent in agents:
        link = agent.find("a",style="color: #0000ff;")
        while link != None:
            #link_ref = link.a['href']  
            print(link["href"]) #instead of
            break
        # name = agent.find("strong")
        # while name != None:
        #     title = name.text
        #     print(title)
        #     break
    y = agency.find_all("p")
    for i in y:
        a = i.find("strong")
        while a != None:
            all = a.text
            print(all)
            break
    # print(f'''
    # Recruitent firm:{link["href"]}
    # Link: {all}
    # ''')
