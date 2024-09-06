from collections import defaultdict
grouped_data = defaultdict(int)
with open('IPS_Manager_Version_1725341949012.csv', 'r',encoding='utf-8-sig') as fp: #The utf-8-sig encoding is used to handle files that start with a Byte Order Mark (BOM). It's common in CSV files exported from Microsoft Excel and helps ensure the encoding is interpreted correctly.
    rows = csv.DictReader(fp)
    for entry in rows:
        version = entry['IPS Manager Version']
        count = int(entry['Manager Count'])
        grouped_data[version] += count


max(grouped_data.items(), key=lambda k: k[1])


{'x': 10, 'y': 5, 'z': 3}

In [49]: sorted(x.iems(),key=lambda i:i[1])


from collections import defaultdict
grouped_data = defaultdict(int)
d = [{"1.2.3": None}, {"2.3.4": 4}, {"1.2.3": 6}]
for row in d:
    for k,v in row.items():
        grouped_data[k] += v

grouped_data
