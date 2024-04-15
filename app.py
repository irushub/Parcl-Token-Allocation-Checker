from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_allocation', methods=['POST'])
def get_allocation():
    input_id = request.form['parcel_id']
    api_url = f"https://app.parcl.co/api/allocation/{input_id}"
    
    try:
        # Making request to the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        allocation = data.get('allocation', 'Not found')  # Get allocation or 'Not found' if missing
        return jsonify({'allocation': allocation})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
