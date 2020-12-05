from os import read

class AlgoHashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]
    
    def set_val(self, key, value):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key,value)
        else:
            bucket.append((key, value))

    def get_val(self, key): 
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No record found with that email address"

    def del_val(self,key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False 
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.remove(bucket[index])
        else:
            return "No record found with that email address"


    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = AlgoHashTable(300) 
hash_table.set_val('hamsterhamin@gamil.com', {'first_name':'hamin','last_name':'jo'})
hash_table.set_val('superhamster@naver.com', {'first_name':'jisoo','last_name':'kim'})
hash_table.set_val('superpotato@nate.com', {'first_name':'minho','last_name':'lee'})
print(hash_table)
print(hash_table.get_val('superpotato@nate.com'))
hash_table.del_val('superpotato@nate.com')
print(hash_table)


quotes_table = AlgoHashTable(100)
with open('data.txt') as f:
    for line in f:
        key, value = line.split(":")
        quotes_table.set_val(key, value)
    
print(quotes_table)
print(quotes_table.get_val('vvfcwaqovl@naver.com'))