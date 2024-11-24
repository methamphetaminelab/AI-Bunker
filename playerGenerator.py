# import random
# import json

# def loadFiles():
#     with open('gender.json', 'r', encoding='utf-8') as file:
#         gender = json.load(file)

#     with open('build.json', 'r', encoding='utf-8') as file:
#         build = json.load(file)

#     with open('trait.json', 'r', encoding='utf-8') as file:
#         trait = json.load(file)

#     with open('profession.json', 'r', encoding='utf-8') as file:
#         profession = json.load(file)

#     with open('health.json', 'r', encoding='utf-8') as file:
#         health = json.load(file)

#     with open('hobby.json', 'r', encoding='utf-8') as file:
#         hobby = json.load(file)

#     with open('phobia.json', 'r', encoding='utf-8') as file:
#         phobia = json.load(file)

#     with open('inventory.json', 'r', encoding='utf-8') as file:
#         inventory = json.load(file)

#     with open('additionalInformation.json', 'r', encoding='utf-8') as file:
#         additionalInformation = json.load(file)

#     with open('skills.json', 'r', encoding='utf-8') as file:
#         skills = json.load(file)

#     return gender, build, trait, profession, health, hobby, phobia, inventory, additionalInformation, skills

# def chooseGender():
#     pass

# def generatePlayer():
#     gender, age, build, trait, profession, health, hobby, phobia, inventory, additionalInformation, skills = loadFiles()

#     player = {
#         'gender': random.choice(gender),
#         'age': random.randint(15, 100),
#         'build': random.choice(build),
#         'trait': random.choice(trait),
#         'profession': random.choice(profession),
#         'health': random.choice(health),
#         'hobby': random.choice(hobby),
#         'phobia': random.choice(phobia),
#         'inventory': random.choice(inventory),
#         'additionalInformation': random.choice(additionalInformation),
#         'skills': random.choice(skills)
#     }

#     return player

import random
import json

def loadFiles():
    with open('characteristics.json', 'r', encoding='utf-8') as file:
        characteristics = json.load(file)

    return characteristics

def generatePlayer():
    characteristics = loadFiles()

    player = {
        'gender': random.choice(characteristics['gender']),
        'age': random.randint(15, 100),
        'build': random.choice(characteristics['build']),
        'trait': random.choice(characteristics['trait']),
        'profession': random.choice(characteristics['profession']),
        'health': random.choice(characteristics['health']),
        'hobby': random.choice(characteristics['hobby']),
        'phobia': random.choice(characteristics['phobia']),
        'inventory': random.choice(characteristics['inventory']),
        'additionalInformation': random.choice(characteristics['additionalInformation']),
        'skills': random.choice(characteristics['skills'])
    }

    return player