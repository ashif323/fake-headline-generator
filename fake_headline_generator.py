# 1- import necessary libraries
import random

# 2- Categorized data
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

# 3- function to generate a fake headline

def generate_headline(category):
        data = categories[category]
        subj = random.choice(data['subjects'])
        act = random.choice(data['actions'])
        place = random.choice(data['places'])
        return f" BREAKING NEWS:   {subj} {act} {place}"
        
    
# 4- interactive user input
print("Categories available: sports, entertainment, politics")

while True:
        try:
            cat = input("\nChoose a category from the above list (or type 'exit' to quit): ").strip().lower()
            if cat == 'exit':
                break
            if cat in categories:
                print(generate_headline(cat))
            else:
                print("Invalid category. Please choose from the list.")
        except KeyboardInterrupt:
            print("\nExiting the headline generator. Goodbye!")
            break
            


