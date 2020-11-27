#! python3
# hw02_main.py - practicing git skills


# Function is parsing url and return dictionary with parameters for web-server.
# Parameters are the list of couples key/value, which separated by symbol &.
def parse(query: str) -> dict:
    dict_of_parameters = {}
    string_of_parameters = query.rpartition('?')
    if string_of_parameters[0] and string_of_parameters[2]:
        list_of_parameters = string_of_parameters[2].split('&')
        for i in range(len(list_of_parameters)):
            if list_of_parameters[i]:
                key, value = list_of_parameters[i].split('=')
                dict_of_parameters.setdefault(key, value)
    else:
        pass
        # list_of_parameters = None
    return dict_of_parameters


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    # TODO Write 10 assert for testing
