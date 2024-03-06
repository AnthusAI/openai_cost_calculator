from decimal import Decimal
import unittest
from openai_cost_calculator.openai_cost_calculator import calculate_cost
from openai_cost_calculator.pricing_information import model_pricing

class TestOpenAICostCalculator(unittest.TestCase):

    def test_calculate_cost(self):
        # Test the cost calculation for a specific model
        result = calculate_cost(model_name='gpt-4-0125-preview', input_tokens=1000000, output_tokens=500000)
        self.assertEqual(result['input_cost'], Decimal('10.00'))
        self.assertEqual(result['output_cost'], Decimal('15.00'))
        self.assertEqual(result['total_cost'], Decimal('25.00'))

    def test_model_name_none(self):
        # Test that the function raises an error if the model name is not specified
        with self.assertRaises(ValueError):
            calculate_cost()

    def test_invalid_model_name(self):
        # Test that the function raises an error for an invalid model name
        with self.assertRaises(ValueError):
            calculate_cost(model_name='invalid-model', input_tokens=1000, output_tokens=1000)

    def test_model_prices(self):
        self.assertEqual(model_pricing['gpt-4-0125-preview']['input_price'], 10.00)
        self.assertEqual(model_pricing['gpt-4-0125-preview']['output_price'], 30.00)
        self.assertEqual(model_pricing['gpt-4-1106-preview']['input_price'], 10.00)
        self.assertEqual(model_pricing['gpt-4-1106-preview']['output_price'], 30.00)
        self.assertEqual(model_pricing['gpt-4-1106-vision-preview']['input_price'], 10.00)
        self.assertEqual(model_pricing['gpt-4-1106-vision-preview']['output_price'], 30.00)

if __name__ == '__main__':
    unittest.main()
