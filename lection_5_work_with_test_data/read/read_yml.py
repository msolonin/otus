from yaml import dump, load, safe_load, safe_dump, FullLoader, SafeLoader, full_load

# https://www.techiedelight.com/parse-yaml-file-python/
# Trusted, not trusted sources

with open('../data/data.yaml') as file:
    # This is equivalent to calling the yaml.full_load() function if data is coming from trusted sources
    # a = load(file.read(), Loader=FullLoader)
    # a = full_load(file)
    # This is equivalent to calling the yaml.safe_load() function that can be used to load data by an untrusted source.
    a = load(file.read(), Loader=SafeLoader)
    # a = safe_load(file)
    print(a)


# input_dct = {'user': 'test', 'password': 'test', }
# with open('dump.yml', 'w') as file:
#     # dump(input_dct, file)
#     safe_dump(input_dct, file)


