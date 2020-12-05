from random import choice
from string import ascii_lowercase as letters

list_of_domains = ['gmail.com', 'naver.com', 'nate.com']

quotes = [ 'Luck is what happens when preparation meets opportunity',
            'All cruelty springs from weakness',
            'Begin at once to live, and count each seperate day as a separate life',
            'Throw me to the wolves and I will return leading the pack']

def generate_name(length_of_name):
    return ''.join(choice(letters) for i in range(length_of_name))

def get_domain(list_of_domains):
    return choice(list_of_domains)

def get_quotes(list_of_quotes):
    return choice(list_of_quotes)

def generate_record(total_records, length_of_name, list_of_domains, list_of_quotes):
    with open('data.txt','w') as to_write:
        for num in range(total_records):
            key = generate_name(length_of_name)+'@'+ get_domain(list_of_domains)
            value = get_quotes(list_of_quotes)
            to_write.write(key + ': ' + value + '\n')

generate_record(10000, 10, list_of_domains, quotes)