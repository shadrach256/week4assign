# week4assign
# File Processor Program

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A Python program that reads a file, modifies its content, and writes the modified version to a new file with comprehensive error handling.

## Features

- **File Reading**: Safely reads input files with multiple error checks
- **Content Modification**: Converts text to uppercase (customizable)
- **File Writing**: Writes to new files with overwrite protection
- **Error Handling**: Comprehensive handling of file-related errors
- **User-Friendly**: Interactive command-line interface with clear prompts

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/file-processor.git
cd file-processor
```

2. Ensure you have Python 3.6+ installed:
```bash
python --version
```

## Usage

Run the program:
```bash
python file_processor.py
```

Follow the on-screen prompts:
1. Enter the name of the file to read
2. Enter the name of the output file
3. The program will process the file and display success/error messages

## Customizing the Modification

Edit the `file_processor.py` file and change the modification line (around line 20):

```python
# Current modification (converts to uppercase)
modified_content = content.upper()

# You could change it to other modifications like:
# modified_content = content.lower()  # Convert to lowercase
# modified_content = '\n'.join(f"{i+1}: {line}" for i, line in enumerate(content.split('\n')))  # Add line numbers
```

## Error Handling

The program handles these error cases:
- File not found
- Permission errors
- Empty filenames
- Attempts to overwrite existing files
- General I/O errors

## Contributing

Contributions are welcome! Please open an issue or pull request for any:
- Bug fixes
- New features
- Documentation improvements

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
