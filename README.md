# DebianContribution
Project for the contribution stage of Outreachy opensource internship

This script wil reads the news page in the Debian wiki, parse the data and write its content to a file in Markdown

<h2>How to run</h2>

Install the python dependencies with the code
<ul>
<li>Python (3.x recommended) installed on your system</li>
<li>install the dependecies with <code>pip install requests beautifulsoup4</code> or <code>pip install -r requirements.txt</code>
</li>
<li>Clone this repository to your local machine <code>git clone https://github.com/Razeetech/DebianContribution.git</code></li>
<li>Change to the project directory <code>cd DebianContribution</code></li>
  
<li><h2>To Run the DebianContribution scripts</h2></li>
if successful, the news would be save as debian_wiki_news.md
  
<li> use the code <code>python DebianContribution.py</code></li>

<li><h2>To run the tests </h2></li>

<li> use the code <code>python test_DebianContribution.py</code></li>
</ul>

<h2>Test Cases</h2>
<ol>
<li>test_fetch_debian_wiki_page_success: Tests the successful fetching of a Debian Wiki page.</li>
<li>test_fetch_debian_wiki_page_failure: Tests handling the failure when fetching a Debian Wiki page.</li>
<li>test_html_to_markdown_with_urls: Tests the conversion of HTML to Markdown with URLs.</li>
<li>test_convert_debian_wiki_to_markdown: Tests the conversion of Debian Wiki content to Markdown.</li>
</ol>
