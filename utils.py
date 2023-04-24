import csv
import json

CATEGORIES_MODEL = "ads.Categories"
CSV_FILE_CATEGORIES = 'datasets/categories.csv'
JSON_FILE_CATEGORIES = 'datasets/categories.json'

ADC_MODEL = "ads.Ads"
CSV_FILE_ADC = 'datasets/ads.csv'
JSON_FILE_ADC = 'datasets/ads.json'

def csv_to_json(file_csv, file_json, model):
    json_list = []
    with open(file_csv, encoding='utf-8') as file_csv:
        reader = csv.DictReader(file_csv)
        for row in reader:
            record_dict = {"model": model}
            if model == ADC_MODEL:
                del row['Id']
                row['price'] = float(row['price'])
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False
            else:
                del row['id']
            record_dict['fields'] = row

            json_list.append(record_dict)

    json_object = json.dumps(json_list, indent=4, ensure_ascii=False)
    with open(file_json, 'w', encoding='utf-8') as file:
        file.write(json_object)


csv_to_json(CSV_FILE_CATEGORIES, JSON_FILE_CATEGORIES, CATEGORIES_MODEL)
csv_to_json(CSV_FILE_ADC, JSON_FILE_ADC, ADC_MODEL)
