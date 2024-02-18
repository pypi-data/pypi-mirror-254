def pretty_print(
    obj: list, delimiter: str = ",", last_delimiter: str = "and", repr_: bool = False
) -> str:
    """
    Returns a formatted string representation of an array
    """
    if repr_:
        sorted_ = sorted(repr(element) for element in obj)
    else:
        sorted_ = sorted(f"'{element}'" for element in obj)

    if len(sorted_) > 1:
        sorted_[-1] = f"{last_delimiter} {sorted_[-1]}"

    return f"{delimiter} ".join(sorted_)


def raise_error_on_duplicate_keys(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    duplicate_keys = []
    for k, v in ordered_pairs:
        if k in d:
            duplicate_keys.append(k)
        else:
            d[k] = v
    if duplicate_keys:
        raise ValueError(f"Duplicate keys: {pretty_print(duplicate_keys)}")
    return d
