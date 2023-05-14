import requests

##### токен #####
token = '246637b30f0709b2aaca33dcb7103a26'
#####

### регистрация
#response = requests.post('https://pokemonbattle.me:9104/trainers/reg', headers = {'Content-Type':'application/json'},
#    json = {"trainer_token": f'{token}', "email": "ind-ruslan-poljatykin@qa.studio", "password": "i2n~81qV"}
#)
#print(response.text)

### подтверждение почты
#response_confirme = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', headers = {'Content-Type':'application/json'},
#     json = {"trainer_token": token,}                             
#)
#print(response_confirme.text)

### создание покемона
add_pokemon_response = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type':'application/json', 'trainer_token':token},
                                json = {"name": "Бульбазавр", "photo": "https://dolnikov.ru/pokemons/albums/001.png"}  
)
print(add_pokemon_response.text)

pokemon_id = add_pokemon_response.json()['id'] ### сохраняем в переменную id покемона
print(pokemon_id)

### изменение имени покемона
change_pokemons_name_response = requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type':'application/json', 'trainer_token':token},
                                     json = {"pokemon_id": pokemon_id, "name": "Бульба",}  
)
print(change_pokemons_name_response.text)

### кладем в покебол
add_pokeball_response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers = {'Content-Type':'application/json', 'trainer_token':token},
                                     json = {"pokemon_id": pokemon_id}  
)
print(add_pokeball_response.text)


### убить покемона
kill_pokemons_response = requests.post('https://pokemonbattle.me:9104/pokemons/kill', headers = {'Content-Type':'application/json', 'trainer_token':token},
                                     json = {"pokemon_id": pokemon_id}  
)
print(kill_pokemons_response.text)

