#! python3
# hw02_main.py - practicing git skills

# Function fills a dictionary from the list by separator on the first occurrence
def from_list_to_dict_by_separator_first_occurrence(list: list, dict: dict) -> dict:
    separator = '='
    for i in range(len(list)):
        if list[i]:
            key, value = list[i].split(separator, 1)
            dict.setdefault(key, value)
    return dict


# Function parses string of cookies separated by ';' and return dictionary with cookies
# where the key is an information before first '=' and value after
def parse_cookie(query: str) -> dict:
    dict_of_cookies = {}
    from_list_to_dict_by_separator_first_occurrence(query.split(';'), dict_of_cookies)
    print(dict_of_cookies)
    return dict_of_cookies


if __name__ == '__main__':
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
