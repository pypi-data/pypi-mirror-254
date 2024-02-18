This package automates the creation of a basic directory structure and files for a data science or machine learning project. It is designed to set up an empty project with standard directories and placeholder files, making it easier to start your project.

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


## Usage

Run the script from the directory where you intend to create the project template.

```python
# Replace 'MyProject' according to your project's name

from dsf import creator
creator("MyProject")

 ```

## Notes:

The script will log each directory and file creation.
Below is a guide for folder usage:

  - **src/(projectName):** Main source code directory.
  - **models:** Reserved for storing model files.
  - **data/raw:** For storing raw/intermediate/processed data files.
  - **reports:** For storing graphs and reports.
  - **research:** Jupyter notebook for experiments.
  - **tests:** Reserved for test scripts.
  - **main.py:** Main entry point for the project.
  - **app.py:** Web-app specific code.
