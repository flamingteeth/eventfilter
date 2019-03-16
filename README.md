# How to Run the Program

## Set up virtual environment

You need to run this program using Python version at least 3.5.

```bash
python3 -m venv venv
venv/bin/python -m pip install --upgrade pip        # Linux
venv\Scripts\python -m pip install --upgrade pip    # Windows
venv/bin/pip install -r requirements.txt            # Linux 
venv\Scripts\pip install -r requirements.txt        # Windows 
```

## Run the program

```bash
venv/bin/python eventfilter.py output.csv           # Linux
venv\Scripts\python eventfilter.py output.csv       # Windows
```

The output CSV is written to `output.csv`, or any other path you specify
in the command.

## Unit tests have been added for the code in test.py
Run the unit test

```bash
venv/bin/python -m unittest                         # Linux
venv\Scripts\python -m unittest                     # Windows
```

## Design Considerations

The main library used in this program is `pandas`, which makes it very
easy to concatenate, filter, sort, and aggregate the data.

For parsing XML, I choosed `xmltodict` because the result can be passed
directly to `pandas` to make a `DataFrame`.

`pendulum` is used to handle the timezone-aware timestamp.

`click` is used to handle the command line argument.



