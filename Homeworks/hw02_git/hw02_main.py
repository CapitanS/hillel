#! python3
# hw02_main.py - practicing git skills


# Function fills a dictionary from the list by separator
def from_list_to_dict_by_separator(list: list, dict: dict) -> dict:
    separator = '='
    for i in range(len(list)):
        if list[i]:
            key, value = list[i].split(separator)
            dict.setdefault(key, value)
    return dict


# Function parses url and return dictionary with parameters for web-server.
# Parameters are the list of couples key/value, which separated by symbol &.
def parse(query: str) -> dict:
    dict_of_parameters = {}
    string_of_parameters = query.partition('?')
    if string_of_parameters[1] and string_of_parameters[2]:
        # check for an anchor in url
        if string_of_parameters[2].find('#') == -1:
            list_of_parameters = string_of_parameters[2].split('&')
            from_list_to_dict_by_separator(list_of_parameters, dict_of_parameters)
        else:
            # detach the anchor and split the parameters
            list_of_parameters = string_of_parameters[2].split('#')[0].split('&')
            from_list_to_dict_by_separator(list_of_parameters, dict_of_parameters)
    else:
        return dict_of_parameters
    return dict_of_parameters


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    # New 10 asserts for testing
    assert parse('http://example.com/?name=Dima#') == {'name': 'Dima'}
    assert parse('http://?') == {}
    assert parse('http://example.com/?name=Dima#anchor') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&age=28') ==\
           {'name': 'ferret', 'color': 'purple', 'age': '28'}
    assert parse('http://') == {}
    assert parse('http') == {}
    assert parse('http://example.com/?name=') == {'name': ''}
    assert parse('http://example') == {}
    assert parse('http://example?') == {}
    assert parse('https://example.com/path/to/page/') == {}
