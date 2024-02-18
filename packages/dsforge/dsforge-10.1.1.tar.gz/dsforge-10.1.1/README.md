This script automates the creation of a basic directory structure and files for a data science or machine learning project. It is designed to set up an empty project with standard directories and placeholder files, making it easier to start your project.

The package will create the following structure and files:

    .
    ├── .github
    │   └── workflows
    │       └── .gitkeep
    ├── src
    │   └── (projectName)
    │       ├── __init__.py
    │       ├── modules
    │       │   └── __init__.py
    │       ├── utilities
    │       │   └── __init__.py
    │       ├── pipeline
    │       │   └── __init__.py
    │       ├── constants
    │       │   └── __init__.py
    ├── models
    │   └── .gitkeep
    ├── data
    │   ├── raw
    │   │   └── .gitkeep
    │   ├── intermediate
    │   │   └── .gitkeep
    │   └── processed
    │       └── .gitkeep
    ├── reports
    │   └── .gitkeep
    ├── research
    │   └── experiments.ipynb
    ├── tests
    │   └── .gitkeep
    ├── main.py
    ├── app.py
    ├── Dockerfile
    ├── requirements.txt
    ├── setup.py
    └── README.md

    The script will log each directory and file creation, only creating empty files if they do not already exist.

Notes:
    Make sure to customize the projectName variable according to your project's name.
    This script assumes Python is installed on your system.
