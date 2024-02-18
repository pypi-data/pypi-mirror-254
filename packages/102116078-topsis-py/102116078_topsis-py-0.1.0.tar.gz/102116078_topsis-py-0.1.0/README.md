# Topsis-Py

Implementation of Topsis in Python by rno. 102116078

## Installation

```bash
pip install topsis-py
```
## Usage

```bash
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

Where
```
<InputDataFile>: Path to the input CSV file.

<Weights>: Comma-separated weights for each criterion.

<Impacts>: Comma-separated impacts ('+' for maximization, '-' for minimization).

<ResultFileName>: Name of the file to save the results.
```

# Example
```bash
python topsis input.csv '1,1,2,1' '+,+,-,+' results.csv
```