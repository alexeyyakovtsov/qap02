my_dict = {
    'person1': {
            'name': 'Tom',
            'age': 22,
            'salary': 20000,
            'items': [
                'car',
                'jacket',
                'TV'
        ]
    },
    'person2': {
        'name': 'Mike',
        'age': 24,
        'salary': 24000,
        'items': [
            'laptop',
            'bike',
            'boat'
        ]
    }
}

print(my_dict)

print(my_dict['person1'].get('items'))
print(my_dict.keys())
help(dict)