from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indexx.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title
        title = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'No title found'

        # Extract paragraphs
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p') if p.get_text(strip=True)]

        # Extract headings
        headings = [h.get_text(strip=True) for h in soup.find_all(['h2', 'h3', 'h4'])]

        # Extract lists
        lists = []
        for list_tag in soup.find_all(['ul', 'ol']):
            items = [item.get_text(strip=True) for item in list_tag.find_all('li') if item.get_text(strip=True)]
            lists.append(items)

        # Extract tables
        tables = []
        for table in soup.find_all('table'):
            headers = [header.get_text(strip=True) for header in table.find_all('th')]
            rows = table.find_all('tr')
            table_data = []
            for row in rows:
                columns = [col.get_text(strip=True) for col in row.find_all('td')]
                if columns:
                    table_data.append(columns)
            tables.append({'headers': headers, 'rows': table_data})

        # Extract links
        links = [{'text': link.get_text(strip=True), 'href': link['href']} for link in soup.find_all('a', href=True) if link.get_text(strip=True)]
        
        return render_template('indexx.html', title=title, paragraphs=paragraphs, headings=headings, lists=lists, tables=tables, links=links)
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
