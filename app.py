from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

categories = {
    'sports': {
        'subjects': ['Virat Kohli on buffalo', 'MS Dhoni\'s pet tiger', 'Sachin\'s cricket bat', 'Rohit Sharma\'s autorickshaw'],
        'actions': ['scores century with', 'throws', 'trains with', 'challenges PM using'],
        'places': ['inside Parliament', 'on Moon surface', 'at chai tapri', 'using biryani bowl']
    },
    'entertainment': {
        'subjects': ['Sharukh Khan\'s dimple', 'Salman\'s shirtless selfie', 'Aamir\'s perfectionism', 'Deepika\'s ponytail'],
        'actions': ['dances on', 'sings national anthem with', 'buys entire', 'marries'],
        'places': ['Red Fort boundary wall', 'auto rickshaw meter', 'Delhi Traffic jam', 'jalebi cart']
    },
    'politics': {
        'subjects': ['Modi ji\'s selfie', 'Kejriwal\'s muffler', 'Yogi ji\'s bulldozer', 'Free electricity scheme'],
        'actions': ['declares war against', 'paints purple', 'distributes free', 'launches rocket to'],
        'places': ['Wankhede Stadium', 'Bollywood sets', 'IPL auction table', 'SRK\'s Mannat']
    }
}

def generate_headline(category):
    data = categories[category]
    subj = random.choice(data['subjects'])
    act = random.choice(data['actions'])
    place = random.choice(data['places'])
    return f"BREAKING NEWS: {subj} {act} {place}!".title()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    category = request.json['category']
    headline = generate_headline(category)
    return jsonify({'headline': headline})

if __name__ == '__main__':
    app.run(debug=True)
