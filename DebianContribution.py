import requests
from bs4 import BeautifulSoup

# set the tURL of the Debian Wiki News page
debianNewsUrl = "https://wiki.debian.org/News"

# Send an HTTP GET request to the URL
response = requests.get(debianNewsUrl)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the news page using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the content section of the page depending on the page structure)
    newsContent = soup.find("div", {"id": "content"})
    
    if newsContent:
        # Extract the text content and store it in a Markdown file
        with open("debianNews.md", "w", encoding="utf-8") as markdownFile:
            # Iterate through paragraphs and write them to the Markdown file
            for paragraph in newsContent.find_all("p"):
                markdownFile.write(paragraph.get_text() + "\n\n")
        #the news content would be saved in file named debianNews.md
        print("Debian News content has been successfully saved to debian_news.md.")
    else:
        print("Content section not found on the page. Please check the page structure.")
else:
    print("Failed to retrieve the Debian Wiki News page. Status code:", response.status_code)
#please ensure that the libraries requests a d BeautifulSoup are instlled before running the script
