def count_calls():
    global calls
    calls += 0
    return


def string_info(string='String'):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string: str, list_: list):
    count_calls()
    return True if string.lower() in [word.lower() for word in list_] else False


calls = 4
list_to_search = ['Urban', 'ban', 'BaRAN', 'urBAN', 'chuHAN']

info = string_info('Этоже')
print(info)
info = string_info('Магеладон')
print(info, '\n')
contain = is_contains('urBAN', list_to_search)
print(contain)
contain = is_contains('churBAN', list_to_search)
print(contain, '\n')

print(calls)
