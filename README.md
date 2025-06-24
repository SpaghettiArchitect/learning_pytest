# Learning Pytest

This repo contains some examples and exercises for learning pytest. The examples are taken from Chapter 11 of [_Python Crash Course_ by Eric Matthes](https://nostarch.com/python-crash-course-3rd-edition).

## How to run?

1. Download and install [uv by astral](https://docs.astral.sh/uv/getting-started/installation/).
2. Clone this repository to your local machine.
3. `cd` into the project's directory and run the following command:

```shell
uv run [name_of_script].py
```

The only files that can be run as standalone programs are `names/names.py` and `surveys/language_survey.py`.

You can run each test by changing the current directory to some of the directories present (`cities`, `employees`, `names` or `surveys`), and running pytest. For example, the following commands will run the tests present in `names/test_name_function.py`:

```shell
cd ./names
uv run pytest
```
