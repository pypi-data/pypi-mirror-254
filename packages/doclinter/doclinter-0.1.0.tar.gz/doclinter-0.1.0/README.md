# DocLinter 📝: Python Docstring Complexity Analyzer

DocLinter is a command-line tool written in Python that helps you maintain consistent and readable documentation across your projects.

## Features

- Lint the complexity of docstrings in Python files.
- Customize analysis by specifying a maximum complexity level.
- Easily integrate into your workflow with a simple command-line interface.

## Installation

You can install DocLinter using pip:

```
pip install doclinter
```

## Usage

To analyze the complexity of docstrings in Python files, use the following command:

```
doclinter <file_or_directory_glob>
```

Optional arguments:

- `--max-ari-level <int>`: Specify the maximum automated readability index to report as an error.
- `-v, --verbose`: Display verbose output.

Example:

```
doclinter my_module.py --max-ari-level 10 -v
```

## How It Works 🛠️

DocLinter utilizes the abstract syntax tree (AST) module in Python to parse Python files and extract docstrings. It rates the complexity of each docstring using the Automated Readability Index (ARI), a formula that takes into account factors such as word count, letter count, and sentence count. Docstrings with complexity levels above the specified threshold are reported as errors.

## Why Use DocLinter? 🚀

- **Enhance Documentation Quality**: Ensure that your docstrings meet readability standards, making your codebase more accessible and maintainable.
- **Catch Complex Docstrings**: Identify and address overly complex docstrings that may hinder understanding and collaboration among team members.
- **Improve Code Review Process**: Streamline code reviews by flagging complex docstrings early in the development cycle, saving time and effort.
- **Foster Best Practices**: Encourage the adoption of clear and concise documentation practices across your projects, promoting consistency and professionalism.

## Roadmap 🗺️

- [x] Better reporting so you can find the function easily
- [x] Arguments for ARI complexity thresholds
- [x] Support linting multiple files at once
- [x] Package on PyPI
- [ ] Make GitHub Actions task
- [ ] Improve documentation
- [ ] Support different measures of complexity (adverbs/passive voice...)
- [ ] Parse different kinds of Python docstrings to lint relevant parts
- [ ] Not just Python files, lint markdown too
- [ ] Support different formulas of complexity
- [ ] Support pyproject.toml configuration

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please [submit an issue](https://github.com/eugene-prout/doclinter/issues) or [create a pull request](https://github.com/eugene-prout/doclinter/pulls) on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.

## Acknowledgements

DocLinter is developed and maintained by [Eugene Prout](https://www.prout.tech).