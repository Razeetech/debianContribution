import unittest
from unittest.mock import patch
from DebianContribution import fetch_debian_wiki_page, html_to_markdown_with_urls, convert_debian_wiki_to_markdown

class TestDebianWikiToMarkdown(unittest.TestCase):
    @patch('DebianContribution.requests.get')
    def test_fetch_debian_wiki_page_success(self, mock_requests_get):
        mock_response = mock_requests_get.return_value
        mock_response.status_code = 200
        mock_response.text = "<html><body>Mock Wiki Page</body></html>"

        url = "https://wiki.debian.org/News"
        page_content = fetch_debian_wiki_page(url)

        mock_requests_get.assert_called_once_with(url)
        self.assertEqual(page_content, "<html><body>Mock Wiki Page</body></html>")

    @patch('DebianContribution.requests.get')
    def test_fetch_debian_wiki_page_failure(self, mock_requests_get):
        mock_requests_get.side_effect = Exception("Failed to fetch page")

        url = "https://wiki.debian.org/News"
        with self.assertRaises(Exception):
            fetch_debian_wiki_page(url)

    def test_html_to_markdown_with_urls(self):
        html = """
        <p>This is a <a href="https://example.com">link</a> to a website.</p>
        <p>Another <a href="https://example.org">link</a>.</p>
        <p>No link here.</p>
        """
        expected_markdown = "This is a [link](https://example.com) to a website.\nAnother [link](https://example.org).\n\nNo link here."

        markdown = html_to_markdown_with_urls(html)

        self.assertNotEqual(markdown, expected_markdown)

    @patch('DebianContribution.fetch_debian_wiki_page')
    @patch('DebianContribution.html_to_markdown_with_urls')
    @patch('DebianContribution.save_markdown_to_file')
    def test_convert_debian_wiki_to_markdown(self, mock_save_markdown, mock_html_to_markdown, mock_fetch_page):
        # Mock data
        wiki_url = "https://wiki.debian.org/News"
        output_file = "mock_output.md"
        wiki_html = "<html><body>Mock Wiki Page</body></html>"
        expected_markdown = "This is a [link](https://example.com) to a website."

        mock_fetch_page.return_value = wiki_html
        mock_html_to_markdown.return_value = expected_markdown

        # Run the conversion
        convert_debian_wiki_to_markdown(wiki_url, output_file)

        # Check if functions were called with correct arguments
        mock_fetch_page.assert_called_once_with(wiki_url)
        mock_html_to_markdown.assert_called_once_with(wiki_html)
        mock_save_markdown.assert_called_once_with(expected_markdown, output_file)

if __name__ == '__main__':
    unittest.main()

