# Universal data-parser
# DataParser Utility

## Overview

**DataParser** is a Python-based utility designed to parse, preview, and extract metadata from various structured data file formats, including:

- CSV
- Excel (`.xls`, `.xlsx`)
- JSON (`.json`)
- Newline-delimited text
- JSON (`.ndjson`)

It supports scanning all files in a given directory, displaying a preview of each dataset and summarizing metadata such as field names, inferred SQL data types, and maximum field lengths.

## Features

- Parse supported files and extract data using `pandas`.
- Normalize and handle nested JSON structures.
- Detect and convert Python datatypes to SQL-like types.
- Analyze column lengths, including list-type values.
- Generate HTML previews and metadata for each file.

## How It Works
-Instantiate the DataParser class.
-Call parse_file(filepath) to parse a single file or parse_directory(directory_path) to process all supported files in a directory.
-For each file, the tool:
-Detects the file type.
-Reads and normalizes the data.
-Infers field metadata (name, data type, field length).
-Returns a preview and metadata summary in HTML format

