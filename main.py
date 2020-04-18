import local as lc


def main():
    def function1(film1, film2, actor1, actor2):
        print(film1 + ' - ', end='')
        print(', '.join(films_set[film1]))
        print(film2 + ' - ', end='')
        print(', '.join(films_set[film2]))

    def function2(film1, film2, actor1, actor2):
        a = films_set[film1] & films_set[film2]
        if len(a) > 0:
            print(', '.join(a))
        else:
            print(lc.FUNCTION2)

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
        if len(f) > 0:
            print(', '.join(f))
        else:
            print(lc.FUNCTION5)

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

    film1 = str(input(lc.FILM1))
    while film1 not in films_set:
        print(lc.FILM1ERROR, end='')
        film1 = str(input())

    film2 = str(input(lc.FILM2))
    while film2 not in films_set:
        print(lc.FILM2ERROR, end='')
        film2 = str(input())

    actor1 = str(input(lc.ACTOR1))
    while actor1 not in actors_set:
        print(lc.ACTOR1ERROR, end='')
        actor1 = str(input())

    actor2 = str(input(lc.ACTOR2))
    while actor2 not in actors_set:
        print(lc.ACTOR2ERROR, end='')
        actor2 = str(input())

    print(lc.MENU1)
    print(lc.MENU2)
    print(lc.MENU3)
    print(lc.MENU4)
    print(lc.MENU5)
    print(lc.MENU6)
    print(lc.MENU7)
    choice = int(input(lc.CHOICE))

    while choice != 7:
        if choice == 1:
            function1(film1, film2, actor1, actor2)
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
        elif choice < 1 or choice > 7:
            print(lc.ERROR)
        choice = int(input(lc.CHOICE))
    else:
        exit()


main()
