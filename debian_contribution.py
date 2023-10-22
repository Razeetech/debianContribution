"""
Converts HTML content from a Debian wiki page to Markdown while preserving URLs.
"""

import re
import requests
from bs4 import BeautifulSoup

# for more specific error handling
class DebianWikiConversionError(Exception):
    """
    to handle more exceptions
    """
    pass

# Function to fetch the content of a Debian wiki page
def fetch_debian_wiki_page(url):
    """
    Fetches the content of a Debian wiki page from the given URL.

    Args:
        url (str): The URL of the Debian wiki page to fetch.

    Returns:
        str: The HTML content of the page.
    """
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as exception:
        raise Exception(f"Error fetching Debian wiki page: {str(exception)}") from exception

# Function to convert HTML content to Markdown while preserving URLs
def html_to_markdown_with_urls(html):
    """
    Converts HTML content to Markdown format while preserving URLs.

    Args:
        html (str): The HTML content to convert.

    Returns:
        str: The Markdown-formatted content.
    """
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
    """
    Saves the Markdown content to a file.

    Args:
        markdown_text (str): The Markdown content to save.
        filename (str): The name of the file to save to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(markdown_text)

# Main function for the script
def convert_debian_wiki_to_markdown(wiki_url, output_filename):
    """
    Converts a Debian wiki page to Markdown format and saves it to a file.

    Args:
        wiki_url (str): The URL of the Debian wiki page.
        output_filename (str): The name of the output Markdown file.
    """
    try:
        wiki_html = fetch_debian_wiki_page(wiki_url)
        markdown_content = html_to_markdown_with_urls(wiki_html)
        save_markdown_to_file(markdown_content, output_filename)
        print(f"Debian wiki page converted to {output_filename}")
    except DebianWikiConversionError as exception:
        print(f"An error occurred: {str(exception)}")

if __name__ == "__main__":
    # Example usage:
    DEBIAN_WIKI_URL = "https://wiki.debian.org/News"
    OUTPUT_FILENAME = "debian_wiki_news.md"
    convert_debian_wiki_to_markdown(DEBIAN_WIKI_URL, OUTPUT_FILENAME)
