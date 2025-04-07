# Calculator Project

This is a simple calculator project that performs basic arithmetic operations: addition, subtraction, multiplication, and division. The project is structured to separate the functionality of each operation into its own module, making it easy to maintain and extend.

## Project Structure

```
calculator-project
├── src
│   ├── addition.py
│   ├── subtraction.py
│   ├── multiplication.py
│   ├── division.py
│   └── main.py
├── tests
│   ├── test_addition.py
│   ├── test_subtraction.py
│   ├── test_multiplication.py
│   └── test_division.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd calculator-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the calculator, execute the `main.py` file:
```
python src/main.py
```

Follow the prompts to enter two numbers and select the desired operation.

## Testing

To run the tests, ensure you have the necessary testing framework installed (as listed in `requirements.txt`), and then execute:
```
pytest tests/
```

## Contributing

Feel free to submit issues or pull requests for improvements or additional features.