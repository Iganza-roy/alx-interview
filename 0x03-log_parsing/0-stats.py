#!/usr/bin/python3

import sys


def print_stats(status_codes, total_size):
    """
    Prints the accumulated metrics.
    
    Args:
        status_codes (dict): A dictionary of status codes and their counts.
        total_size (int): The accumulated total file size.
    """
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


def process_input():
    """
    Processes input lines from stdin, updating the status codes dictionary and total file size.
    """
    total_size = 0
    status_codes = {code: 0 for code in ["200", "301", "400", "401", "403", "404", "405", "500"]}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 2:
                continue
            
            file_size = int(parts[-1])
            status_code = parts[-2]

            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(status_codes, total_size)

    except KeyboardInterrupt:
        print_stats(status_codes, total_size)
        raise

    print_stats(status_codes, total_size)


if __name__ == "__main__":
    process_input()
