# ProjectDisclosed

ProjectDisclosed is designed to help new comers/bug hunters to store and manage HackerOne disclosed reports with personalized options and statistics. With features such as tracking read/unread reports, organizing data based on Common Weakness Enumerations (CWE), and Severity levels, ProjectDisclosed offers a comprehensive solution for managing reading disclosed security vulnerabilities effectively.

## Features

- **Personalized Options**: Customize your experience with features such as marking reports as read/unread.
- **CWE-Based Data Organization**: Organize reports based on Common Weakness Enumerations (CWE) for efficient categorization.
- **Severity-Based Data**: Track and analyze reports based on severity levels to prioritize responses effectively.

## Installation

### Prerequisites

Before installing ProjectDisclosed, ensure you have the following prerequisites installed:

- Python (>=3.6)
- Django (>=3.0)
- Docker (optional, for Docker installation)

### Manual Installation

- ```https://github.com/0xh7ml/projectdisclosed.git```
- ```cd projectdisclosed```
- ```python -m venv env (Windows) python3 -m venv env (macOs/Linux)```
- ```source env/Scripts/activate(Windows) source env/bin/activate (macOs/Linux)```
- ```pip install -r requirements.txt```
- ```python manage.py migrate (Windows) python3 manage.py migrate (macOs/Linux)```
- ```python manage.py runserver```


## Usage

1. log in to your ProjectDisclosed account by ```admin:admin```.
2. Start reading disclosed reports.
3. Mark as read when you read any reports for better stats.

## Contributing

Contributions to ProjectDisclosed are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure tests pass.
4. Submit a pull request detailing your changes.