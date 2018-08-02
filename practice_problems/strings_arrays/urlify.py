def urlify(string, len):
    string_list = string.split()
    string_url = "%20".join(string_list)
    return string_url

print(urlify("Mr John Smith   ", 13))
