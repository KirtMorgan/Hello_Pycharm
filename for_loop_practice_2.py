movies_places = {
    'movies_list':['Iron Man', 'Avengers', 'Real Steel', 'Ghost Busters', 'Big'],
    'places_list':['Japan', 'Russia', 'New York', 'New Vegas', 'Cornwall']
}
# for list in movies_places.values():
#     print(list)
#     for movie in list:
#         print(movie)

print('Here is my movie list:')
for movie in movies_places['movies_list']:
    print(movie)

print()

print('Here is a list of places i want to visit:')
for place in movies_places['places_list']:
    print(place)