from datetime import datetime


def merge_ranges(list_of_ranges, datetime=False):
    merged_ranges = []

    if datetime:
        list_of_ranges = replace_none(list_of_ranges)

    if len(list_of_ranges) > 0:
        sorted_list = sorted(list_of_ranges)
        range_start, range_end = sorted_list[0]
        for start, end in sorted_list:
            if start is None or start <= range_end:
                if end is None:
                    range_end = None
                    break
                elif range_end is not None:
                    range_end = max(range_end, end)
            else:
                merged_ranges.append((range_start, range_end))
                range_start, range_end = start, end
        merged_ranges.append((range_start, range_end))

    return merged_ranges


def replace_none(ranges):
    ret = []
    for (start, end) in ranges:
        if start is None:
            start = datetime.min
        if end is None:
            end = datetime.max
        ret.append((start, end))
    return ret