#!/usr/bin/python3
"""
Module 0-stats
"""

import sys


if __name__ == '__main__':
    file_size = 0
    status_counts = {200: 0,
                     301: 0,
                     400: 0,
                     401: 0,
                     403: 0,
                     404: 0,
                     405: 0,
                     500: 0}
    line_count = 0

    def print_stats(file_size, status_counts):
        """ Print statistics. """
        print(f"File size: {file_size}")

        for code in sorted(status_counts.keys()):
            if status_counts[code] > 0:
                print(f"{code}: {status_counts[code]}")

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            # Extract and validate the file size
            try:
                size = int(parts[-1])
                file_size += size
            except (IndexError, ValueError):
                continue

            # Extract and validate the status code
            try:
                status_code = int(parts[-2])
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except (IndexError, ValueError):
                continue

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(file_size, status_counts)
        raise
