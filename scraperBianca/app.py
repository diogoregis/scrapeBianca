from flask import Flask, jsonify
from scrapeBianca import scrape_bianca_home

app = Flask(__name__)


@app.route('/scrape_bianca_home', methods=['GET'])
def scrape_bianca_home_api():
    data = scrape_bianca_home()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
