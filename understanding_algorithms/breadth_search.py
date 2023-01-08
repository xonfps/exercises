from collections import deque


def search(name):
    fork = {}
    fork['You'] = ['Alice', 'Bob', 'Claire']
    fork['Bob'] = ['Anuj', 'Peggy']
    fork['Alice'] = ['Peggy']
    fork['Claire'] = ['Thom', 'Jonny']
    fork['Anuj'] = []
    fork['Peggy'] = []
    fork['Thom'] = []
    fork['Jonny'] = []

    search_queue = deque()
    search_queue += fork['You']
    checked = []

    def person_is_seller(name):
        return name[-1] == 'm'

    while search_queue:
        person = search_queue.popleft()
        if not person in checked:
            if person_is_seller(person):
                print(f'{person} is a mango seller')
                return True
            else:
                search_queue += fork[person]
    return False

search('You')
