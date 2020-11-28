#! python3
# hw02_main.py - practicing git skills


# Function fills a dictionary from the list by separator
def from_list_to_dict_by_separator(my_list: list) -> dict:
    separator = '='
    my_dict = {}
    for i in range(len(my_list)):
        if my_list[i]:
            key, value = my_list[i].split(separator)
            my_dict.setdefault(key, value)
    return my_dict


# Function parses url and return dictionary with parameters for web-server.
# Parameters are the list of couples key/value, which separated by symbol &.
def parse(query: str) -> dict:
    list_of_parameters = []
    string_of_parameters = query.partition('?')
    if string_of_parameters[1] and string_of_parameters[2] == -1:
        list_of_parameters = string_of_parameters[2].split('&')
    elif string_of_parameters[2] != -1:
        # detach the anchor and split the parameters
        list_of_parameters = string_of_parameters[2].split('#')[0].split('&')
    else:
        pass
    dict_of_parameters = from_list_to_dict_by_separator(list_of_parameters)
    return dict_of_parameters


# Function fills a dictionary from the list by separator on the first occurrence
def from_list_to_dict_by_separator_first_occurrence(my_list: list) -> dict:
    separator = '='
    my_dict = {}
    for i in range(len(my_list)):
        if my_list[i]:
            key, value = my_list[i].split(separator, 1)
            my_dict.setdefault(key, value)
    return my_dict


# Function parses string of cookies separated by ';' and return dictionary with cookies
# where the key is an information before first '=' and value after
def parse_cookie(query: str) -> dict:
    dict_of_cookies = from_list_to_dict_by_separator_first_occurrence(query.split(';'))
    return dict_of_cookies


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
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
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima;;age=28') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima;age=28') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima;;') == {'name': 'Dima'}
    assert parse_cookie('name=Dima;age=28;group=3') == {'name': 'Dima', 'age': '28', 'group': '3'}
    assert parse_cookie('name=') == {'name': ''}
    assert parse_cookie('=Dima;;') == {'': 'Dima'}
    assert parse_cookie('=Dima;') == {'': 'Dima'}
    assert parse_cookie('=') == {'': ''}
    assert parse_cookie('name=Dima;=;age=28') == {'name': 'Dima', '': '', 'age': '28'}
    assert parse_cookie('= ') == {'': ' '}
