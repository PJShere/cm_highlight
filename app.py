from flask import Flask
from flask import request, jsonify
from lxml import etree as ET

app = Flask(__name__)


@app.route('/getxml_lineno', methods=['POST'])
def getxml_lineno():
    xml_chunk = request.form['xml_chunk']
    x_path = request.form['x_path']
    root = ET.fromstring(xml_chunk.encode('utf-8'))
    for el in root.xpath(x_path):
        lineno = el.sourceline - 1
        endlineno = el.sourceline + (len(ET.tostring(el).strip().split()) - 1)

    resp = {'start': {'line': lineno, 'ch': 0}, 'end': {'line': endlineno, 'ch': 0}}
    msg = jsonify(resp)

    return msg


if __name__ == "__main__":
    app.run(debug=True)
