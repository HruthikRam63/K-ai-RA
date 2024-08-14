import datetime
from flask import Flask, render_template, request, jsonify, url_for
from assistant_services import (
    speak, wish_me, tell_joke, calculate_expression, calculate_tip, play_game, get_motivation,
    search_wikipedia, find_restaurants, find_local_events, search_recipes, recommend_book,
    find_local_deals, get_travel_info, find_nearby_gyms, get_stock_price, check_flight_status,
    fun_fact, historical_events, inspirational_quote, local_attractions, new_music, word_of_the_day,
    famous_birthdays, recipe_ideas, daily_horoscope, diy_projects
)

app = Flask(__name__, template_folder='../web_app/templates', static_folder='../web_app/static')

@app.route('/')
def index():
    wish_me()
    return render_template('kAIra_frontend.html')

@app.route('/start-recognition', methods=['POST'])
def start_recognition():
    recognition_result = request.json.get('transcript', '')
    return jsonify({'transcript': recognition_result})

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    command = data.get('command', '').lower()

    response = process_command(command)
    return jsonify(response)

def process_command(command):
    if 'hello' in command or 'hey' in command:
        speak("Hello Sir, how may I assist you today?")
        return {}
    elif 'how are you' in command:
        speak("I'm doing good, how about you?")
        return {}
    elif 'open google' in command:
        speak("Opening Google...")
        return {'url': 'https://google.com'}
    elif 'open youtube' in command:
        speak("Opening YouTube...")
        return {'url': 'https://youtube.com'}
    elif 'open some youtube video' in command:
        speak("Opening a YouTube video...")
        return {'url': 'https://youtu.be/46TqWYJIUDc?si=LUpbBMLCQ9IDyWek'}
    elif 'open chatgpt' in command:
        speak("Opening ChatGPT...")
        return {'url': 'https://chat.openai.com'}
    elif 'open facebook' in command:
        speak("Opening Facebook...")
        return {'url': 'https://facebook.com'}
    elif 'open twitter' in command:
        speak("Opening Twitter...")
        return {'url': 'https://twitter.com'}
    elif 'open instagram' in command:
        speak("Opening Instagram...")
        return {'url': 'https://instagram.com'}
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
        return {}
    elif 'tell me a joke' in command:
        joke = tell_joke()
        speak(joke)
        return {'response': joke}
    elif 'calculate' in command:
        expression = command.replace('calculate', '').strip()
        result = calculate_expression(expression)
        speak(f"The result is {result}.")
        return {'response': f"The result is {result}."}
    elif 'tip' in command:
        parts = command.split()
        amount = parts[parts.index('tip') - 1]
        percentage = parts[parts.index('tip') + 1]
        result = calculate_tip(amount, percentage)
        speak(result)
        return {'response': result}
    elif 'play game' in command:
        game_response = play_game()
        speak(game_response)
        return {'response': game_response}
    elif 'motivation' in command:
        motivation = get_motivation()
        speak(motivation)
        return {'response': motivation}
    elif 'wikipedia' in command:
        topic = command.replace('wikipedia', '').strip()
        result = search_wikipedia(topic)
        speak(f"Here is what I found on Wikipedia.")
        return {'response': result}
    elif 'restaurants' in command:
        result = find_restaurants()
        return {'redirect': url_for('results', requirement='Find restaurants nearby', action=result)}
    elif 'events' in command:
        result = find_local_events()
        return {'redirect': url_for('results', requirement='Find local events', action=result)}
    elif 'recipe' in command:
        dish = command.replace('recipe for', '').strip()
        result = search_recipes(dish)
        return {'redirect': url_for('results', requirement=f'Recipe for {dish}', action=result)}
    elif 'book recommendation' in command:
        result = recommend_book()
        return {'redirect': url_for('results', requirement='Book recommendation', action=result)}
    elif 'deals' in command:
        result = find_local_deals()
        return {'redirect': url_for('results', requirement='Find local deals', action=result)}
    elif 'travel' in command:
        destination = command.replace('travel info for', '').strip()
        result = get_travel_info(destination)
        return {'redirect': url_for('results', requirement=f'Travel info for {destination}', action=result)}
    elif 'gyms' in command:
        result = find_nearby_gyms()
        return {'redirect': url_for('results', requirement='Find nearby gyms', action=result)}
    elif 'stock price' in command:
        company = command.replace('stock price of', '').strip()
        result = get_stock_price(company)
        return {'redirect': url_for('results', requirement=f'Stock price of {company}', action=result)}
    elif 'flight status' in command:
        flight_number = command.replace('flight status for', '').strip()
        result = check_flight_status(flight_number)
        return {'redirect': url_for('results', requirement=f'Flight status for {flight_number}', action=result)}
    elif 'fun fact' in command:
        result = fun_fact()
        return {'redirect': url_for('results', requirement='Fun fact', action=result)}
    elif 'historical events' in command:
        result = historical_events()
        return {'redirect': url_for('results', requirement='Historical events for today', action=result)}
    elif 'inspirational quote' in command:
        result = inspirational_quote()
        return {'redirect': url_for('results', requirement='Inspirational quote', action=result)}
    elif 'attractions' in command:
        result = local_attractions()
        return {'redirect': url_for('results', requirement='Local attractions', action=result)}
    elif 'new music' in command:
        result = new_music()
        return {'redirect': url_for('results', requirement='New music', action=result)}
    elif 'word of the day' in command:
        result = word_of_the_day()
        return {'redirect': url_for('results', requirement='Word of the day', action=result)}
    elif 'famous birthdays' in command:
        result = famous_birthdays()
        return {'redirect': url_for('results', requirement='Famous birthdays', action=result)}
    elif 'recipe ideas' in command:
        result = recipe_ideas()
        return {'redirect': url_for('results', requirement='Recipe ideas', action=result)}
    elif 'daily horoscope' in command:
        sign = command.replace('daily horoscope for', '').strip()
        result = daily_horoscope(sign)
        return {'redirect': url_for('results', requirement=f'Daily horoscope for {sign}', action=result)}
    elif 'diy projects' in command:
        result = diy_projects()
        return {'redirect': url_for('results', requirement='DIY projects', action=result)}
    else:
        search_url = f'https://www.google.com/search?q={command.replace(" ", "+")}'
        return {'url': search_url}

@app.route('/results')
def results():
    requirement = request.args.get('requirement', '')
    action = request.args.get('action', '')
    return render_template('results.html', requirement=requirement, action=action)

if __name__ == "__main__":
    app.run(debug=True)
