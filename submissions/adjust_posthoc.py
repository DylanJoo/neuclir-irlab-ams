import json

for file in ['submission-dev-all-irlab-ams-postcite.json', 'submission-dev-all-irlab-ams-postcite-v.json', 'submission-test-all-irlab-ams-postcite.json', 'submission-test-all-irlab-ams-postcite-v.json']:
    d = json.load(open(file))

    with open(file.replace('json', 'jsonl'), 'w') as f:
        for item in d:
            collection_ids = item['collection_ids'][0].replace("neuclir/1/", "")
            item['run_id'] = f"{collection_ids}_{str(item['run_id'])}"
            item['request_id'] = str(item['request_id'])
            f.write(json.dumps(item)+'\n')
