from difflib import SequenceMatcher


def diff_percentage(actual_value: str, scanned_value: str) -> float:
    """
    Calculate percentage error in a scanned string from that of the original string.
    It is the percentage of number of characters differing from original string including removals and inserts.
    :param actual_value:
    :param scanned_value:
    :return:
    """
    actual_length = len(actual_value)
    if actual_length:
        diff_result = SequenceMatcher(a=actual_value, b=scanned_value)
        # refer docs for more info: https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.get_opcodes
        differing_char_count = sum(
            (0 if tag == 'equal' else i2 - i1 if tag == 'delete' else j2 - j1 for tag, i1, i2, j1, j2 in
             diff_result.get_opcodes()),
            0,
        )
        percentage_error = 100 * differing_char_count / actual_length
        return 100 - percentage_error
    else:
        return 0
