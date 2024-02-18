# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import enum

reserved_keys = ["_verbatim", "_product", "_union", "_intersection", "_complement"]
comment_key = "_comment"


class signature_kind(enum.Enum):
    verbatim = 0
    fvalue = 1
    kv = 2
    kmv = 3
    kvs = 4
    kmvs = 5
    akvs = 6
    union = 7
    product = 8
    intersection = 9
    complement = 10


def is_verbatim(value: dict) -> bool:
    """
    Check if the value is a verbatim value.

    A verbatim value is a dictionary with a single key `_verbatim` and any JSON-compatible
    value as the value.
    """
    if not isinstance(value, dict):
        return False

    if not len(value.keys()) == 1:
        return False

    for key, val in value.items():
        if not key == "_verbatim":
            return False

    return True


def is_fvalue(value) -> bool:
    """
    Check if the value is a fundamental value.

    A fundamental value is a string or a verbatim value.
    """
    return isinstance(value, str) or is_verbatim(value)


def is_comment(value: dict) -> bool:
    """
    check if a key-value pair is a comment
    """
    if not isinstance(value, dict):
        return False

    if not len(value.keys()) == 1:
        return False

    for key, val in value.items():
        if not key == "_comment":
            return False

    return True


def is_kv(value: dict) -> bool:
    """
    Check if the input value is a key-value pair.

    The value is a key-value pair if it is a dictionary with a single key and a single value. The
    key cannot be a reserved value and the value  can either be a string or a verbatim value.
    """
    if not isinstance(value, dict):
        return False

    if not len(value.keys()) == 1:
        return False

    for key, val in value.items():
        if key in reserved_keys:
            return False

        if key == comment_key:
            return False

        if not is_fvalue(val):
            return False

    return True


def is_kmv(value: dict) -> bool:
    """
    Check if the input value is a key-multi-value pair.

    The value is a key-multi-value pair if it is a dictionary with a single key and a list of
    values. The key cannot be `_product` and the values have to be strings.
    """

    if not isinstance(value, dict):
        return False

    if not len(value.keys()) == 1:
        return False

    for key, val in value.items():
        if key in reserved_keys:
            return False

        if key == comment_key:
            return False

        if not isinstance(val, list):
            return False

        for v in val:
            if not is_fvalue(v):
                return False

    return True


def is_kvs(value: dict) -> bool:
    """Check if the value is a key value set

    key-value set is a dictionary with keys as the product names and values as the product values.
    The product values can be a single value. But the keys cannot themselves be a `_product` key.
    That is, there is no nested product in the value.
    """
    if not isinstance(value, dict):
        return False

    for key, val in value.items():
        if is_comment({key: val}):
            continue

        if key in reserved_keys:
            return False

        if not is_fvalue(val):
            return False

    return True


def is_kmvs(value: dict) -> bool:
    """Check if the value is a key-multi-value set

    key-multi-value set is a dictionary with keys as the product names and values as the product
    values. The product values can be only be a list of values. But the keys cannot
    themselves be a `_product` key. That is, there is no nested product in the value.
    """
    if not isinstance(value, dict):
        return False

    for key, val in value.items():
        if key in reserved_keys:
            return False

        if not is_kmv({key: val}):
            return False

    return True


def is_akvs(value: list) -> bool:
    """Check if the value is an array of key-value sets"""

    if not isinstance(value, list):
        return False

    for v in value:
        if not is_kvs(v):
            return False
    return True


def is_union(value) -> bool:
    if isinstance(value, list):
        return is_union_list_form(value)
    elif isinstance(value, dict):
        return is_union_dict_form(value)

    return False


def is_union_dict_form(value: dict) -> bool:
    if not len(value.keys()) == 1:
        return False

    for key, val in value.items():
        if not key == "_union":
            return False

    if not isinstance(value["_union"], list):
        return False

    return is_union_list_form(value["_union"])


def is_union_list_form(value: list) -> bool:
    if is_akvs(value):
        return True

    for v in value:
        if not (is_union(v) or is_product(v)):
            return False

    return True


def is_product_dict_value(value) -> bool:
    if is_kmvs(value):
        return True

    # The entrypoint of this function is from is_product_dict_form. So, we can assume that the
    # value is a dictionary with a single key. Hence, we don't need this check in a non-buggy
    # implementation. However, we keep this check because we don't yet have a full formal
    # specification of the grammar.
    if not len(value.keys()) == 1: # pragma: no cover
        return False # pragma: no cover

    for key, val in value.items():
        if key == "_product":
            return is_product_dict_value(value)

        if key == "_union":
            return is_union({key: value})

    return False


def is_product_dict_form(value: dict) -> bool:
    for key, val in value.items():
        if not is_product_dict_value({key: val}):
            return False
    return True


def is_product(value: dict) -> bool:
    if not isinstance(value, dict):
        return False

    if not len(value.keys()) == 1:
        return False

    for key, val in value.items():
        if not key == "_product":
            return False

        if isinstance(val, dict):
            return is_product_dict_form(val)

        if isinstance(val, list):
            for v in val:
                if not is_union(v):
                    return False

    return True


def is_set(value) -> bool:
    return is_union(value) or is_product(value)
