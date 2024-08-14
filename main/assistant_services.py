import random
import pyttsx3
import threading
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    def speak_thread():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=speak_thread).start()

def wish_me():
    hour = datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning, Mr. HR!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon, Mr. HR!")
    else:
        speak("Good Evening, Mr. HR!")

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you get when you cross a snowman with a vampire? Frostbite.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    return jokes[random.randint(0, len(jokes) - 1)]

def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def calculate_tip(amount, percentage):
    try:
        amount = float(amount)
        percentage = float(percentage)
        tip = (amount * percentage) / 100
        return f"Tip amount is: ${tip:.2f}"
    except ValueError:
        return "Invalid amount or percentage."

def play_game():
    number = random.randint(1, 10)
    return f"Guess a number between 1 and 10. I've picked a number: {number}"

def get_motivation():
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. – Confucius"
    ]
    return quotes[random.randint(0, len(quotes) - 1)]

def search_wikipedia(topic):
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    return f"Here is what I found on Wikipedia: {url}"

def find_restaurants():
    url = "https://www.google.com/maps/search/restaurants+near+me"
    return f"Here are some restaurants near you: {url}"

def find_local_events():
    url = "https://www.eventbrite.com/d/online/events/"
    return f"Here are some local events: {url}"

def search_recipes(dish):
    url = f"https://www.allrecipes.com/search/results/?wt={dish.replace(' ', '%20')}"
    return f"Here is a recipe for {dish}: {url}"

def recommend_book():
    url = "https://www.goodreads.com/quotes/tag/inspirational"
    return f"Here are some book recommendations: {url}"

def find_local_deals():
    url = "https://www.groupon.com/local"
    return f"Here are some deals near you: {url}"

def get_travel_info(destination):
    url = f"https://en.wikipedia.org/wiki/{destination.replace(' ', '_')}"
    return f"Here is some travel information about {destination}: {url}"

def find_nearby_gyms():
    url = "https://www.google.com/maps/search/gyms+near+me"
    return f"Here are some gyms near you: {url}"

def get_stock_price(company):
    url = f"https://www.google.com/finance/quote/{company}"
    return f"Here is the stock price for {company}: {url}"

def check_flight_status(flight_number):
    url = f"https://www.flightaware.com/live/flight/{flight_number}"
    return f"Here is the status of flight {flight_number}: {url}"

def fun_fact():
    url = "https://www.factretriever.com/fun-facts"
    return f"Here is a fun fact: {url}"

def historical_events():
    today = datetime.now().strftime("%B_%d")
    url = f"https://www.onthisday.com/events/date/{today}"
    return f"Here are historical events for today: {url}"

def inspirational_quote():
    url = "https://www.brainyquote.com/topics/inspirational-quotes"
    return f"Here is an inspirational quote: {url}"

def local_attractions():
    url = "https://www.google.com/maps/search/local+attractions"
    return f"Here are some local attractions: {url}"

def new_music():
    url = "https://www.billboard.com/charts/hot-100/"
    return f"Check out the latest hits: {url}"

def word_of_the_day():
    url = "https://www.merriam-webster.com/word-of-the-day"
    return f"Here is the word of the day: {url}"

def famous_birthdays():
    today = datetime.now().strftime("%B_%d")
    url = f"https://www.famousbirthdays.com/{today}.html"
    return f"Here are famous birthdays for today: {url}"

def recipe_ideas():
    url = "https://www.allrecipes.com/recipes/"
    return f"Here are some recipe ideas: {url}"

def daily_horoscope(sign):
    url = f"https://www.astrology.com/horoscope/daily/{sign}.html"
    return f"Here is your daily horoscope: {url}"

def diy_projects():
    url = "https://www.instructables.com/"
    return f"Here are some DIY project ideas: {url}"
