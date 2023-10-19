import requests
from bs4 import BeautifulSoup
import re


# Function to fetch the content of a Debian wiki page
def fetch_debian_wiki_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching Debian wiki page: {str(e)}")

# Function to convert HTML content to Markdown while preserving URLs
def html_to_markdown_with_urls(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Handle links and preserve their URLs
    for a_tag in soup.find_all('a'):
        url = a_tag.get('href')
        if url:
            a_tag.insert_before(f"[{a_tag.text}]({url})")
            a_tag.decompose()

    # Convert the HTML to plain text
    markdown_text = re.sub(r'\n+', '\n\n', soup.get_text().strip())

    # Handle headings and convert them to Markdown
    for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        heading_level = int(heading.name[1])  # Extract the heading level (e.g., 1 from 'h1')
        heading_text = heading.get_text().strip()
        markdown_heading = '#' * heading_level + ' ' + heading_text  # Convert to Markdown
        heading.insert_before(markdown_heading)
        heading.decompose()

    return markdown_text

# Function to save the Markdown content to a file
def save_markdown_to_file(markdown_text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(markdown_text)

# Main function for the script
def convert_debian_wiki_to_markdown(wiki_url, output_file):
    try:
        wiki_html = fetch_debian_wiki_page(wiki_url)
        markdown_content = html_to_markdown_with_urls(wiki_html)
        save_markdown_to_file(markdown_content, output_file)
        print(f"Debian wiki page converted to {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage:
    debian_wiki_url = "https://wiki.debian.org/News"
    output_filename = "debian_wiki_news.md"
    convert_debian_wiki_to_markdown(debian_wiki_url, output_filename)
