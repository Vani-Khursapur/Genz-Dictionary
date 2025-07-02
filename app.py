from flask import Flask, request, jsonify, render_template, send_from_directory
import os

app = Flask(__name__)


gen_z_dict = {
    "yeet": {
        "meaning": "To throw something with force or excitement.",
        "example": "She yeeted the ball across the field!",
        "emoji": "🤾‍♀️💨"
    },
    "slay": {
        "meaning": "To do something exceptionally well or look amazing.",
        "example": "You slayed that outfit today!",
        "emoji": "🔥👗✨"
    },
    "sus": {
        "meaning": "Short for 'suspicious' or 'suspect,' often used to call something or someone shady.",
        "example": "That deal sounds kinda sus, not gonna lie.",
        "emoji": "🤔🚨"
    },
     "no cap": {
        "meaning": "For real, no lie. Used to express sincerity.",
        "example": "This pizza is the best, no cap!",
        "emoji": "🧢❌"
    },
    "vibe": {
        "meaning": "A mood or atmosphere that someone or something gives off.",
        "example": "The café has such a chill vibe!",
        "emoji": "🎶✨"
    },
    "bet": {
        "meaning": "Used to confirm something or agree to a plan.",
        "example": "You coming to the party? Bet!",
        "emoji": "👌🎉"
    },
    "bussin": {
        "meaning": "Used to describe something that's really good, especially food.",
        "example": "This burger is bussin'!",
        "emoji": "🍔🤤"
    },
    "lit": {
        "meaning": "Amazing, exciting, or fun.",
        "example": "The concert last night was so lit!",
        "emoji": "🔥🎤"
    },
    "periodt": {
        "meaning": "Used at the end of a sentence to emphasize that there's no further discussion needed.",
        "example": "I’m not going back there, periodt.",
        "emoji": "✅🔚"
    },
    "stan": {
        "meaning": "To be an obsessive fan of someone or something.",
        "example": "I stan this new artist so much!",
        "emoji": "🎤❤️"
    },
    "flex": {
        "meaning": "To show off or boast about something.",
        "example": "That’s a nice car! Big flex.",
        "emoji": "💪🚗"
    },
    "ghost": {
        "meaning": "To suddenly cut off communication with someone without explanation.",
        "example": "He ghosted me after our last chat.",
        "emoji": "👻🚫"
    },
    "lowkey": {
        "meaning": "Used to express something subtly or secretly.",
        "example": "I’m lowkey excited for the trip.",
        "emoji": "🤫✨"
    },
    "highkey": {
        "meaning": "The opposite of lowkey, used to express something openly or strongly.",
        "example": "I’m highkey nervous about the exam tomorrow.",
        "emoji": "😬📚"
    },
    "tea": {
        "meaning": "Gossip or juicy news.",
        "example": "Spill the tea on what happened at the party!",
        "emoji": "☕👀"
    },
    "main character": {
        "meaning": "Someone who acts as if the world revolves around them (in a positive or humorous way).",
        "example": "She’s definitely the main character in her life story.",
        "emoji": "🌟🎬"
    },
    "big yikes": {
        "meaning": "Used to describe something super embarrassing or awkward.",
        "example": "He spilled coffee on his boss’s shirt, big yikes!",
        "emoji": "😬☕"
    },
    "on fleek": {
        "meaning": "Perfectly done or looking great.",
        "example": "Your eyebrows are on fleek!",
        "emoji": "✨💁‍♀️"
    },
    "snatched": {
        "meaning": "Used to describe something as flawless or amazing, often related to appearance.",
        "example": "Her outfit is absolutely snatched!",
        "emoji": "🔥👗"
    },
    "salty": {
        "meaning": "Bitter or upset about something.",
        "example": "He’s salty because he lost the game.",
        "emoji": "🧂😡"
    },
    "pinky": {
        "meaning": "Vani Jayadev Khursapur",
        "example": "Pinky loves sakshi",
        "emoji": "🥰🫂"
    },
    "hot happala" : {
        "meaning": "Smitha",
        "example": "Smitha loves Dance and Sakshi",
        "emoji": ""
    },
    "tan": {
        "meaning": "Tanmay Anand",
        "example": "Sakshi will break tanmay's wall",
        "emoji": ""
    },
    
}

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        
        user_input = request.json.get('term', '').strip().lower()

        
        if user_input in gen_z_dict:
            slang = gen_z_dict[user_input]
            response = f"{slang['meaning']}\n {slang['emoji']}\n\nExample: {slang['example']}"
        else:
            response = None  

        return jsonify({"message": response})
    except Exception as e:
        
        print(f"Error: {e}")
        return jsonify({"message": "An error occurred on the server. Please try again later."}), 500


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  