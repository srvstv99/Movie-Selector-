import uuid
from collections import defaultdict
from typing import List
import random


class Friend:
    def __init__(self, firstname, lastname):
        self._id = uuid.uuid4()
        self.firstname = firstname
        self.lastname = lastname

    @property
    def id(self):
        return self._id


movie_list = defaultdict(list)


def add_movie(friend_id, movie):
    movie_list[friend_id].append(movie)


def recommend_movie(friends: List[Friend]) -> str:
    all_movies = []
    for friend in friends:
        all_movies.extend(movie_list[friend.id])
    return random.choice(all_movies)


def main():
    # Screen 1
    alice = Friend('Alice', 'A')
    bob = Friend('Bob', 'B')
    charlie = Friend('Charlie', 'C')
    densie = Friend('Densie', 'D')

    # Screen 2
    add_movie(alice.id, 'Harry Potter 1')
    add_movie(alice.id, 'Harry Potter 2')
    add_movie(alice.id, 'Harry Potter 3')
    add_movie(alice.id, 'Harry Potter 4')
    add_movie(alice.id, 'Harry Potter 5')

    add_movie(bob.id, 'Titanic')
    add_movie(bob.id, 'Lord of the Rings 1')
    add_movie(bob.id, 'Lord of the Rings 2')
    add_movie(bob.id, 'Lord of the Rings 3')
    add_movie(bob.id, 'Lord of the Rings 4')
    add_movie(bob.id, 'Alien')
    add_movie(bob.id, 'Terminator')
    add_movie(bob.id, 'Rambo')

    add_movie(charlie.id, 'Bond 1')
    add_movie(charlie.id, 'Bond 2')
    add_movie(charlie.id, 'Bond 3')
    add_movie(charlie.id, 'Bond 4')
    add_movie(charlie.id, 'Bond 5')

    add_movie(densie.id, 'Beauty & Beast')
    add_movie(densie.id, 'Snow White')
    add_movie(densie.id, 'Jumbo')
    add_movie(densie.id, 'Jungle Book')
    add_movie(densie.id, 'Frozen')
    add_movie(densie.id, 'Peter Pan')

    # Screen 3
    print(recommend_movie([alice, charlie, densie]))


main()