from chatterbot import ChatBot

# Create a new chat bot
chatbot = ChatBot(
    'Weather Bot',
    logic_adapters=[
        'chatterbot_weather.weather_adapter.WeatherLogicAdapter'
    ]
)

# Ask a question about the weather
response = chatbot.get_response('What is the weather like today?')

print(response)
