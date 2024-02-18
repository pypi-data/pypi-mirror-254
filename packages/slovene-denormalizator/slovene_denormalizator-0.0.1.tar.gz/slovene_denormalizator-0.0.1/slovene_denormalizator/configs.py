import re

def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

configs={"default":
            {"punct_is_included": True,
            "include_slash": True,
            "include_numbers": True,
            "include_numbers_part_token": True,
            "include_units": True,
            "include_email": True,
            "include_title": True,
            "include_abbr": True,
            "include_symbols": True,
            "include_fractions": True,
            "include_stylistic": True,
            "include_alnum": False,
            "merge_sep_numbers": True,
            "col_years": True,
            "proper_tokenization": True},

        "everyday":
            {"include_units": False},
        "technical":
            {"include_stylistic": False,
            "include_slash": True}}
