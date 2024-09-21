import json


def json_to_txt_columns(input_json , output_file):
    with open(input_json , 'r') as f:
        data=json.load(f)

    if isinstance(data, dict):
        columns = list(data.keys())
        data = [data]
    elif isinstance(data, list) and len(data) > 0:
        columns = list(data[0].keys())
    else:
        raise ValueError("Input JSON must be a dictionary or a non-empty list of dictionaries")

    with open(output_file, 'w') as f:
        f.write('\t'.join(columns) + "\n")

        for item in data:
            row = [str (item.get(col , '')) for col in columns]
            f.write('\t'.join(row) + '\n')


input_json = 'search.json'
output_file = 'output_file.txt'
json_to_txt_columns(input_json , output_file)