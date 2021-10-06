import json

with open('pokemon_entities/pokemons.json', encoding='utf-8') as database:
    pokemons = json.load(database)['pokemons']
print(pokemons)
for pokemon in pokemons:
    print(pokemon['title_ru'])
    print(pokemon['entities'])

    try:
        print(pokemon['previous_evolution'])
    except:
        continue



# pokemons_on_page = []
# pokemons = Pokemon.objects.all()
# for pokemon in pokemons:
#     pokemons_on_page.append({
#         'pokemon_id': pokemon['pokemon_id'],
#         'img_url': pokemon['img_url'],
#         'title_ru': pokemon['title_ru'],
#     })