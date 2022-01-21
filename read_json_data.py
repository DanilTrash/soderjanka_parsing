import json

with open(r'C:\Users\KIEV-COP-4\Desktop\soderjanka_parsing\soderjanki\data.json') as file:
    file_read_ = json.load(file)
    for data in file_read_:
        data_div = data.get('data').get('div')
        p1 = data_div.get('p1')
        if p1:
            h1 = p1.split('\n')
            lower = h1[0].lower()
            if 'москва' in lower:
                print({lower: data_div.get('p2')})
