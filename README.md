# `ultraprint` - A Python Library for Enhanced Terminal Output

Welcome to `ultraprint`! This Python library is designed to enhance terminal output with colorful and styled text, making your console logs more readable and aesthetically pleasing developed by [*Ranit Bhowmick*](https://www.linkedin.com/in/ranitbhowmick/) & [*Sayanti Chatterjee*](https://www.linkedin.com/in/sayantichatterjee/). Whether you're building a command-line application, debugging code, or just want to add some flair to your terminal, `ultraprint` provides a simple and effective solution.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Basic Usage](#basic-usage)
   - [Color Functions](#color-functions)
   - [Text Style Functions](#text-style-functions)
   - [Background Color Functions](#background-color-functions)
   - [Newline Function](#newline-function)
4. [Advanced Usage: Logging](#advanced-usage-logging)
   - [Logger Class](#logger-class)
   - [Logger Methods](#logger-methods)
5. [Documentation](#documentation)
   - [Color Functions](#color-functions)
   - [Text Style Functions](#text-style-functions)
   - [Background Color Functions](#background-color-functions)
   - [Logger Class](#logger-class)
6. [Examples](#examples)
7. [Contributing](#contributing)

## Introduction

`ultraprint` is a Python library that extends the capabilities of the standard `print` function. It allows you to easily print text in different colors, styles, and backgrounds in the terminal. Additionally, it includes a logger class that can log messages with different severity levels and styles, both in the terminal and to a file.

This library is ideal for developers who want to make their terminal outputs more organized and visually appealing. With `ultraprint`, you can quickly identify important information, warnings, errors, and other message types based on their color and style.

## Installation

To install `ultraprint`, simply use `pip`:

```bash
pip install ultraprint
```

## Basic Usage

### Color Functions

The `ultraprint` library provides functions to print text in various colors:

```python
import ultraprint.common as p

p.red("This is red text")
p.green("This is green text")
p.yellow("This is yellow text")
p.blue("This is blue text")
p.purple("This is purple text")
p.cyan("This is cyan text")
p.lgray("This is light gray text")
p.dgray("This is dark gray text")
```

### Text Style Functions

In addition to colors, you can apply styles like bold, underline, and negative:

```python
p.bold("This is bold text")
p.underline("This is underlined text")
p.negative("This is negative text")
```

### Background Color Functions

You can also change the background color of the text:

```python
p.red_bg("This is red background text")
p.green_bg("This is green background text")
p.yellow_bg("This is yellow background text")
p.blue_bg("This is blue background text")
p.purple_bg("This is purple background text")
p.cyan_bg("This is cyan background text")
p.lgray_bg("This is light gray background text")
p.dgray_bg("This is dark gray background text")
```

### Newline Function

For convenience, you can easily print new lines:

```python
p.n()  # Prints one new line

p.n(3)  # Prints three new lines
```

## Advanced Usage: Logging

### Logger Class

The `ultraprint` library includes a `logger` class for structured logging with different severity levels. The logger can output messages both to the console and to a log file.

```python
from ultraprint.logging import logger

# Create a logger object
log = logger('example_log')

# Log some messages
log.info('This is an info message')
log.error('This is an error message')
log.warning('This is a warning message')
log.success('This is a success message')
log.debug('This is a debug message')
log.critical('This is a critical message')
```

### Logger Methods

The `logger` class provides the following methods:

- `info(msg)`: Logs an informational message.
- `error(msg)`: Logs an error message.
- `warning(msg)`: Logs a warning message.
- `success(msg)`: Logs a success message.
- `debug(msg)`: Logs a debug message.
- `critical(msg)`: Logs a critical message.

All methods write the log entry to both the console (in color) and to a log file with the same name as the logger.

## Documentation

### Color Functions

These functions print the provided text in different colors:

- **red(*args)**: Prints text in red.
- **green(*args)**: Prints text in green.
- **yellow(*args)**: Prints text in yellow.
- **blue(*args)**: Prints text in blue.
- **purple(*args)**: Prints text in purple.
- **cyan(*args)**: Prints text in cyan.
- **lgray(*args)**: Prints text in light gray.
- **dgray(*args)**: Prints text in dark gray.

### Text Style Functions

These functions apply different styles to the text:

- **bold(*args)**: Prints bold text.
- **underline(*args)**: Prints underlined text.
- **negative(*args)**: Prints text with a negative style.

### Background Color Functions

These functions print the provided text with different background colors:

- **red_bg(*args)**: Prints text with a red background.
- **green_bg(*args)**: Prints text with a green background.
- **yellow_bg(*args)**: Prints text with a yellow background.
- **blue_bg(*args)**: Prints text with a blue background.
- **purple_bg(*args)**: Prints text with a purple background.
- **cyan_bg(*args)**: Prints text with a cyan background.
- **lgray_bg(*args)**: Prints text with a light gray background.
- **dgray_bg(*args)**: Prints text with a dark gray background.

### Logger Class

The `logger` class provides structured logging with colored outputs. Each log method corresponds to a different level of severity and prints in a specific color.

#### Logger Methods:

- **info(msg)**: Logs an informational message in cyan.
- **error(msg)**: Logs an error message in red.
- **warning(msg)**: Logs a warning message in yellow.
- **success(msg)**: Logs a success message in green.
- **debug(msg)**: Logs a debug message in dark gray.
- **critical(msg)**: Logs a critical message with a red background.

## Examples

### Basic Color and Style Printing

```python
import ultraprint.common as p

p.red("This is red text")
p.bold("This is bold text")
p.red_bg("This is red background text")
```

### Using the Logger

```python
from ultraprint.logging import logger

log = logger('example_log')
log.info('Starting the process...')
log.success('Process completed successfully!')
log.warning('This is a warning')
log.error('An error occurred')
log.critical('Critical failure, system shutting down!')
```

## Contributing

We welcome contributions to `ultraprint`! If you have suggestions, find a bug, or want to add a new feature, please open an issue or submit a pull request on GitHub.