def unflatten_dict(a, primary_key=None, results=None):
    if results is None:
        results = {}
    
    if primary_key:
        if primary_key in results:
            results[primary_key].update(a)
        else:
            results[primary_key] = a
        return results

    for key, value in a.items():
        if "." in key:
            array = key.split(".")
            primary_key = array[0]
            new_key = array[1]
            new_dict = {new_key: value}
            unflatten_dict(new_dict, primary_key, results)
            primary_key = None
        else:
            results[key] = value

    return results

a = {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
print(unflatten_dict(a))
