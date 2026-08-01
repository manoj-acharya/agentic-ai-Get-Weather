import random 

def get_weather_condition(city:str="Bangalore")->dict:
    """
    Returns the current weather condition for a given city.

    Args:
        city (str): The name of the city for which to get the weather condition.

    Returns:
        dict: A dictionary containing the current weather condition and temperature.
    """
    #makeing wether condition random for now, in future we can use some api to get the weather condition.
    possible_conditions = ["sunny", "rainy", "cloudy", "snowy", "windy"]
    condition = random.choice(possible_conditions)
    temperature = random.randint(-10, 35)  # Simulate a range of temperatures
    message = f"The current weather in {city} is {condition} with a temperature of {temperature}°C."
    # print(message)
    weather_data = {
        "condition": condition,
        "temperature": temperature,
        "weather_message": message
    }

    # For demonstration purposes, let's return a sample weather condition
    return weather_data  # Possible values: "sunny", "rainy", "cloudy", "snowy", etc.

def get_clothing_suggestion(city:str="Bangalore")->str:
    """
    Suggest clothing based on the current weather condition of the city.
    
    Args:
        city (str): The name of the city for which to get the weather condition.
        
    Returns:
        str: A clothing suggestion based on the weather condition.
    """
    weather_data = get_weather_condition(city)
    weather_condition = weather_data["condition"]
    temperature = weather_data["temperature"]
    weather_message = weather_data["weather_message"]


    suggestions = {
        "sunny": "Wear light clothing, sunglasses, and a hat.",
        "rainy": "Carry an umbrella and wear a waterproof jacket.",
        "cloudy": "A light jacket or sweater would be suitable.",
        "snowy": "Wear a warm coat, gloves, and a hat.",
        "windy": "A windbreaker or jacket is recommended."
    }

    message = f"Weather condition: {weather_condition}, Temperature: {temperature}°C. {weather_message}. {suggestions.get(weather_condition, "No specific suggestion available for this weather condition.")}"   
    return message