#!/usr/bin/env python3

# file by t.me/efxtv
# Join us for more

import argparse
import os
import re

def parse_size(size_str):
    match = re.match(r"(\d+)([MG]B)?", size_str)
    if not match:
        raise ValueError(f"Invalid size format: {size_str}")
    size = int(match.group(1))
    unit = match.group(2)
    if unit == 'GB':
        size *= 1024 * 1024 * 1024
    else:  # Default to MB if no unit or 'MB'
        size *= 1024 * 1024
    return size

def split_by_size(file_path, output_prefix, size_str):
    size_bytes = parse_size(size_str)
    with open(file_path, 'rb') as f:
        part_num = 0
        while True:
            chunk = f.read(size_bytes)
            if not chunk:
                break
            with open(f"{output_prefix}{part_num:03}", 'wb') as chunk_file:
                chunk_file.write(chunk)
            part_num += 1

def split_by_parts(file_path, output_prefix, num_parts):
    file_size = os.path.getsize(file_path)
    part_size = file_size // num_parts
    with open(file_path, 'rb') as f:
        for part_num in range(num_parts):
            chunk = f.read(part_size)
            if part_num == num_parts - 1:
                chunk += f.read()  # Append the remaining bytes to the last part
            with open(f"{output_prefix}{part_num:03}", 'wb') as chunk_file:
                chunk_file.write(chunk)

def split_by_lines(file_path, output_prefix, num_lines):
    with open(file_path, 'r') as f:
        part_num = 0
        lines = []
        for i, line in enumerate(f, 1):
            lines.append(line)
            if i % num_lines == 0:
                with open(f"{output_prefix}{part_num:03}", 'w') as chunk_file:
                    chunk_file.writelines(lines)
                lines = []
                part_num += 1
        if lines:
            with open(f"{output_prefix}{part_num:03}", 'w') as chunk_file:
                chunk_file.writelines(lines)

def main():
    parser = argparse.ArgumentParser(description="Split a large file into smaller parts.")
    subparsers = parser.add_subparsers(dest='command')

    # Size-based splitting
    parser_size = subparsers.add_parser('s', help='-s (size in MB/GB) input output')
    parser_size.add_argument('size', help='Size of each part (e.g., 5MB or 1GB)')
    parser_size.add_argument('input', help='Input file')
    parser_size.add_argument('output', help='Output prefix')

    # Number of parts-based splitting
    parser_parts = subparsers.add_parser('n', help='-n (number of parts) input output')
    parser_parts.add_argument('num_parts', type=int, help='Number of parts')
    parser_parts.add_argument('input', help='Input file')
    parser_parts.add_argument('output', help='Output prefix')

    # Line-based splitting
    parser_lines = subparsers.add_parser('l', help='-l (line number) input output')
    parser_lines.add_argument('num_lines', type=int, help='Number of lines per part')
    parser_lines.add_argument('input', help='Input file')
    parser_lines.add_argument('output', help='Output prefix')

    args = parser.parse_args()

    if args.command == 's':
        split_by_size(args.input, args.output, args.size)
    elif args.command == 'n':
        split_by_parts(args.input, args.output, args.num_parts)
    elif args.command == 'l':
        split_by_lines(args.input, args.output, args.num_lines)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

