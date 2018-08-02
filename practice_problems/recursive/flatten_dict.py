def flatten_dict(d, primary_key=None, results=None):
    if not results:
        results = {}
    for key, value in d.items():
        if isinstance(value, dict):
            primary_key = key
            flatten_dict(value, primary_key, results)
            primary_key = None
        else:
            if primary_key:
                results[primary_key + "." + key] = value
            else:
                results[key] = value
    return results

d = {
    'a': 2,
    'b': 3,
    'c': {
        'd': 4,
        'e': 5
    },
    'f': 6
}

print(flatten_dict(d))
