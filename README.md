# OpenAI Cost Calculator

The OpenAI Cost Calculator is a Python tool designed to calculate the cost of using OpenAI models based on the number of input and output tokens. This tool supports various models, including GPT-4 variants, and uses precise decimal arithmetic to ensure accurate financial calculations.

Please help keep this updated!  Please send pull requests!

Or, better yet, continue pressuring OpenAI to provide a pricing API or some way to find the actual price of requests.

## Features

- Support for multiple OpenAI models including GPT-4 variants.
- Accurate cost calculation using decimal arithmetic.
- Simple and easy-to-use interface.

## Installation

To install the OpenAI Cost Calculator, you need to have Python installed on your system. Then, you can install the package and its dependencies by running:

```bash
pip install -r requirements.txt
```

This command installs all the necessary dependencies, including `coverage` for code coverage analysis and `watchexec` for automatically rerunning tests during development.

## Usage

To calculate the cost of using an OpenAI model, you can import and use the `calculate_cost` function from the `openai_cost_calculator` module. Here's an example:

```python
from openai_cost_calculator import calculate_cost

cost = calculate_cost(model_name='gpt-4-0125-preview', input_tokens=1000, output_tokens=500)

print(f"Total cost: {cost}")
```

Replace `'gpt-4-0125-preview'` with the model you're using, and adjust `input_tokens` and `output_tokens` according to your usage.

## Running Tests

To ensure the reliability of the cost calculations, unit tests are provided. You can run these tests using the following command:

```bash
make test
```

For a detailed coverage report, use:

```bash
make coverage
```

This will generate a coverage report in both terminal and HTML format, allowing you to see which parts of the code are covered by tests.

## Contributing

Contributions to the OpenAI Cost Calculator are welcome, especially in keeping the pricing information up-to-date. As OpenAI updates their pricing, please help by submitting pull requests with the updated prices. This ensures that the tool remains accurate and useful for everyone. Feel free to also suggest improvements or add support for additional models.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.