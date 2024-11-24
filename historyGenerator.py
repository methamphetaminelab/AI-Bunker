import random
import json

def loadHistories(filename="histories.json"):
    with open(filename, 'r', encoding='utf-8') as file:
        histories = json.load(file)
    return histories

def generateHistory(histories):
    history = random.choice(histories)
    
    population_left = random.randint(history['population_left_range'][0], history['population_left_range'][1])
    
    return f"Катастрофа: {history['title']}\n\n{history['description']}\n\nОстаток населения: {population_left} человек"

# if __name__ == "__main__":
#     histories = loadHistories()
#     print(generateHistory(histories))
