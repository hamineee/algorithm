records = [('hamsterhamin@gmail.com','hamin'),
            ('superhamster@naver.com','hamster'),
            ('superpotato@naver.com','potato')
            ]


for index, record in enumerate(records):
    key, value = record
    if key == "superhamster@naver.com":
        break
print(records[index])