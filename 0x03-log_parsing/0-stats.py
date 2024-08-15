#!/usr/bin/python3

import sys


def print_stats(status_code_counts, total_file_size):
    """
    Print the accumulated metrics.
    Args:
        status_code_counts (dict): Dictionary containing status code counts.
        total_file_size (int): The total size of all files.
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


def process_line(line, status_code_counts, total_file_size):
    """
    Process each line of input to extract status code and file size.
    Args:
        line (str): The input line.
        status_code_counts (dict): Dictionary to store counts of status codes.
        total_file_size (int): The running total of the file sizes.
    Returns:
        tuple: Updated status code count and total file size.
    """
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = parts[-2]

        total_file_size += file_size

        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

    except (IndexError, ValueError):
        pass

    return status_code_counts, total_file_size


def main():
    total_file_size = 0
    status_code_counts = {
        "200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
        "404": 0, "405": 0, "500": 0
        }
    line_count = 0

    try:
        for line in sys.stdin:
            status_code_counts, total_file_size = process_line(
                line, status_code_counts, total_file_size
                )
            line_count += 1

            if line_count == 10:
                print_stats(status_code_counts, total_file_size)
                line_count = 0

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(status_code_counts, total_file_size)


if __name__ == "__main__":
    main()
