import json

for file in ['submission-dev-all-irlab-ams-postcite.json', 'submission-dev-all-irlab-ams-postcite-v.json', 'submission-test-all-irlab-ams-postcite.json', 'submission-test-all-irlab-ams-postcite-v.json']:
    d = json.load(open(file))

    with open(file.replace('json', 'jsonl2'), 'w') as f:
        for item in d:
            item['request_id'] = str(item['request_id'])
            f.write(json.dumps(item)+'\n')
