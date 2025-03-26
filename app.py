from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/fetch', methods=['GET'])
def fetch_api():
    uid = request.args.get('uid')
    region = request.args.get('region')

    if not uid or not region:
        return jsonify({"error": "Missing uid or region parameters"}), 400

    api_url = f"http://wlx-spam-visits.vercel.app/demon_visits?uid={uid}&region={region}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        return jsonify({"status": "success", "data": data})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
