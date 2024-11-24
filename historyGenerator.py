import random
import json

def loadHistories():
    with open("histories.json", 'r', encoding='utf-8') as file:
        histories = json.load(file)
    return histories

def generateHistory():
    history = random.choice(loadHistories())
    
    population_left = random.randint(history['population_left_range'][0], history['population_left_range'][1])
    
    return f"Катастрофа: {history['title']}\n\n{history['description']}\n\nОстаток населения: {population_left} человек"

# if __name__ == "__main__":
#     histories = loadHistories()
#     print(generateHistory(histories))
