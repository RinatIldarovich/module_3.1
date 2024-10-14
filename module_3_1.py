calls=0

def count_calls():
    global calls
    calls += 1


print(calls)

def string_info(string):
    result = (len(string), string.upper(), string.lower())
    count_calls()
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))

def is_contains(string, list_to_search):    # 4
    string = string.lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result


print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)