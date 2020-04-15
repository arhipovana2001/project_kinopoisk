def main():
    def functon1(film1, film2, actor1, actor2):
        print(film1 + ' - ', end='')
        print(', '.join(films_set[film1]))
        print(film2 + ' - ', end='')
        print(', '.join(films_set[film2]))

    def function2(film1, film2, actor1, actor2):
        a = films_set[film1] & films_set[film2]
        print(', '.join(a))

    def function3(film1, film2, actor1, actor2):
        a = films_set[film1] - films_set[film2]
        print(', '.join(a))

    def function4(film1, film2, actor1, actor2):
        print(actor1 + ' - ', end='')
        print(', '.join(actors_set[actor1]))
        print(actor2 + ' - ', end='')
        print(', '.join(actors_set[actor2]))

    def function5(film1, film2, actor1, actor2):
        f = actors_set[actor1] & actors_set[actor2]
        print(', '.join(f))

    def function6(film1, film2, actor1, actor2):
        f = actors_set[actor1] - actors_set[actor2]
        print(', '.join(f))

    films_set = {}
    actors_set = {}
    with open('input.txt', encoding='utf-8') as inp:
        k = 0
        for line in inp.readlines():
            if k % 2 == 0:
                film = line[:-1]
                films_set[film] = ''
            else:
                actors_old = line.split(', ')
                actors = []
                for i in actors_old:
                    if i.count('\n') > 0:
                        actors.append(i[:-1])
                    else:
                        actors.append(i)
                films_set[film] = set(actors)
            k += 1

    for key, value in films_set.items():
        for i in value:
            actors_set[i] = set()

    for actor in actors_set:
        for film in films_set:
            if actor in films_set[film]:
                actors_set[actor].add(film)

    film1 = str(input('Введите название первого фильма: '))
    film2 = str(input('Введите название второго фильма: '))
    actor1 = str(input('Введите имя первого актера: '))
    actor2 = str(input('Введите имя второго актера: '))
    print('''1. Определить общий актерский состав, снимавшихся хотя бы в одном из этих двух фильмах.''')
    print('''2. Определить актеров, снимавшихся и в первом, и во втором фильме.''')
    print('''3. Определить актеров, участвующих в съемках первого, но не участвующих в съемках второго.''')
    print('''4. Определить названия фильмов, в которых снимался хотя бы в одном из актеров.''')
    print('''5. Определить названия фильмов, в которых снимались оба актера.''')
    print('''6. Определить названия фильмов, в которых снимался первый актер, но не участвовал в съемках второй.''')
    print('''7. Выйти из программы''')
    choice = int(input('Выберите, что вы хотите сделать: '))

    while choice != 7:
        if choice == 1:
            functon1(film1, film2, actor1, actor2)
        elif choice == 2:
            function2(film1, film2, actor1, actor2)
        elif choice == 3:
            function3(film1, film2, actor1, actor2)
        elif choice == 4:
            function4(film1, film2, actor1, actor2)
        elif choice == 5:
            function5(film1, film2, actor1, actor2)
        elif choice == 6:
            function6(film1, film2, actor1, actor2)
        choice = int(input('Выберите, что вы хотите сделать: '))
    else:
        exit()


main()
