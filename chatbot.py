from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import requests, json
import requests


class cht_bot:
    def __init__(self):
        self.bot = ChatBot('JR. Adesh')
        self.trainer = ChatterBotCorpusTrainer(self.bot)
        self.trainer.train("chatterbot.corpus.english")
        self.que = {
    "What is your name": "My name is Jr Adesh.",
    "How are you": "I'm just a computer program, so I don't have feelings, but thanks for asking!",
    "What can you do": "I can help answer questions, provide information, or just chat with you.",
    "Who created you": "I was created by a birrilent Genious programer Adesh Shrivastav",
    "Where are you from": "I exist in the Adesh Computer, so I don't have a physical location.",
    "How old are you": "I am just a program, so I don't have an age., but i was created in date 18-02-2024",
    "What is the meaning of life": "The meaning of life is a philosophical question that varies from person to person.",
    "Tell me a joke.": "Why don't scientists trust atoms? Because they make up everything!",
    "What is your favorite color": "I don't have the ability to see colors, so I don't have a favorite.",
    "Do you like music": "I don't have preferences like humans do, but I can certainly provide information about music.",
    "What is the capital of France": "The capital of France is Paris.",
    "What is the square root of 16": "The square root of 16 is 4.",
    "Who is the president of the United States": "I'm sorry, I don't have access to real-time information. Please check a reliable news source.",
    "What is the population of China": "As of my last update, the population of China is over 1.4 billion people.",
    "How do I cook pasta?=": "Boil water, add pasta, and cook until al dente. Don't forget to add salt!",
    "What is artificial intelligence?=": "Artificial intelligence is the simulation of human intelligence processes by machines, especially computer systems.",
    "Can you help me with my homework": "I can certainly try! What do you need help with?",
    "What is the meaning of love": "Love is a complex emotion that can mean different things to different people.",
    "How do I change my password": "To change your password, go to your account settings and look for the option to change your password.",
    "What is the largest mammal": "The blue whale is the largest mammal.",
    "How do I reset my phone": "To reset your phone, go to the settings menu and look for the option to factory reset.",
    "What is the best movie of all time": "There's no definitive answer to that question, as it's subjective and depends on personal taste.",
    "What is the meaning of happiness": "Happiness is a state of well-being and contentment.",
    "What is the speed of light": "The speed of light in a vacuum is approximately 299,792 kilometers per second.",
    "How do I make pancakes": "Mix flour, eggs, milk, and a pinch of salt. Cook the batter on a hot pan until golden brown on both sides.",
    "What is the population of the world": "As of my last update, the world population is over 7.8 billion people.",
    "What is the meaning of success": "Success can mean different things to different people, but it often involves achieving goals or fulfilling one's potential.",
    "How do I tie a tie": "There are several ways to tie a tie, but a common method is the Windsor knot.",
    "What is the meaning of dreams": "The meaning of dreams is a topic of debate among psychologists and researchers.",
    "What is the distance to the moon": "The average distance to the moon is approximately 384,400 kilometers.",
    "What is the capital of Japan": "The capital of Japan is Tokyo.",
    "What is the boiling point of water": "The boiling point of water is 100 degrees Celsius or 212 degrees Fahrenheit at sea level.",
    "What is the meaning of friendship": "Friendship is a relationship of mutual affection between people.",
    "What is the currency of Japan": "The currency of Japan is the Japanese yen.",
    "What is the meaning of democracy": "Democracy is a system of government in which power is vested in the people, who rule either directly or through freely elected representatives.",
    "How do I change a flat tire": "To change a flat tire, first, make sure you're in a safe location, then loosen the lug nuts, lift the car with a jack, remove the lug nuts and the flat tire, put on the spare tire, tighten the lug nuts, and lower the car.",
    "What is the meaning of education": "Education is the process of acquiring knowledge, skills, values, beliefs, and habits.",
    "What is the meaning of freedom": "Freedom is the power or right to act, speak, or think as one wants without hindrance or restraint.",
    "What is the meaning of justice": "Justice is the quality of being fair and reasonable.",
    "How do I make chocolate chip cookies": "Mix butter, sugar, eggs, flour, and chocolate chips. Drop spoonfuls of dough onto a baking sheet and bake until golden brown.",
    "What is the meaning of courage": "Courage is the ability to do something that frightens one.",
    "What is the tallest mountain in the world": "Mount Everest is the tallest mountain in the world.",
    "How do I say 'hello' in Spanish": "Hola!",
    "What is the meaning of beauty": "Beauty is a combination of qualities, such as shape, color, or form, that pleases the aesthetic senses.",
    "What is the meaning of success": "Success can mean different things to different people, but it often involves achieving goals or fulfilling one's potential.",
    "What is the largest ocean": "The Pacific Ocean is the largest ocean.",
    "What is the meaning of leadership": "Leadership is the action of leading a group of people or an organization.",
    "What is the meaning of innovation": "Innovation is the process of creating new ideas, products, or methods.",
    "How do I start a business?": "To start a business, you'll need a solid idea, a business plan, funding, and determination.",
    "What is the meaning of knowledge": "Knowledge is information and skills acquired through experience or education.",
    "What is the meaning of technology": "Technology is the application of scientific knowledge for practical purposes, especially in industry.",
    "How do I take care of a pet": "Taking care of a pet involves providing food, water, shelter, exercise, and veterinary care.",
}
    
    def get_weather(self,city):
        api_key = 'b23d64a0a705f05d5df47c26072d7d95'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            weather = {
                'description': data['weather'][0]['description'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return weather
        else:
            return None

    
        
        
    def question(self):
        while True:
            self.x = input("Your query : ")
            self.x =self.x.capitalize()
            if "weather" in self.x and "what" in self.x:
                city = input("Enter city name: ")
                weather = self.get_weather(city)

                if weather:
                    print(f"Weather in {city}:")
                    print(f"Description: {weather['description']}")
                    print(f"Temperature: {weather['temperature']}Â°C")
                    print(f"Humidity: {weather['humidity']}%")
                    print(f"Wind Speed: {weather['wind_speed']} m/s")
                else:
                    print("Weather information not available for the provided city.")
                    
            if "bye" in self.x or "exit" in self.x:
                print("bye bye see you")
                break
            if self.x.capitalize() in self.que:
                print(self.que[self.x])
            elif "your" in self.x and "name" in self.x:
                print("I am Jr.Adesh")
            
            
            else:
                self.ct_bt(self.x)
    def ct_bt(self,x):
        
        query = x
        print(self.bot.get_response(query))
            
            
if __name__ == "__main__" :
    bt = cht_bot()
    bt.question()
