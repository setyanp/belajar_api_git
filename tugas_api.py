from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def _remove_punct(s):
    return re.sub(r"[^\w\d\s]+", "",s)

@app.route("/get_name/v1", methods=['GET'])
def get_name():
    nama = request.args.get('name')

    if nama == 'jokowi':
        dict_result = {"nama" : "ya ndak tau kok tanya saya"}
    else:
        dict_result = {"nama" : f"nama beliau adalah {nama}"}

    return jsonify(dict_result)

@app.route("/get_telor/v1", methods=['POST'])
def get_text():
    s = request.get_json()
    s = s['text']

    len_char = len(s)

    s = s.lower()
    s = _remove_punct(s)

    list_s = s.split()
    telor_count = list_s.count("telor")

    dict_result = {
        "total_char": len_char,
        "total_telor": telor_count
    }
    return jsonify(dict_result)


if __name__ == "__main__":
    app.run(port=1234, debug=True)