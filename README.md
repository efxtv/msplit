# msplit

## About Script

The `msplit.py` script is a command-line utility designed to split large files into smaller parts based on different criteria such as size, number of parts, or number of lines. This script is useful for managing and processing large datasets efficiently.

## Dependencies

To run `msplit.py`, ensure you have:

- Python 3.x

No additional Python libraries are required beyond the standard library.

## How to Use

You can use `msplit.py` from the command line with various options to split your files.

### How to use msplit

### list of options 

s - Size

n - Number of parts

l - Number of lines

```
./msplit.py option GB,MB/Number/Parts <input_file> <output_prefix>
```

```
./msplit.py s 1GB largefile.txt output_part
```
```
./msplit.py n 5 data.csv output_part
```
```
./msplit.py l 1000 textfile.txt output_part
```

