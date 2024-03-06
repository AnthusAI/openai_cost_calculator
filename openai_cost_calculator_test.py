import unittest
from openai_cost_calculator import calculate_cost
from pricing_information import model_pricing

class TestOpenAICostCalculator(unittest.TestCase):

    def test_model_prices(self):
        self.assertEqual(model_pricing['gpt-4-0125-preview']['input_price'], 10.00)
        self.assertEqual(model_pricing['gpt-4-0125-preview']['output_price'], 30.00)
        self.assertEqual(model_pricing['gpt-4-1106-preview']['input_price'], 10.00)
        self.assertEqual(model_pricing['gpt-4-1106-preview']['output_price'], 30.00)
        self.assertEqual(model_pricing['gpt-4-1106-vision-preview']['input_price'], 10.00)
        self.assertEqual(model_pricing['gpt-4-1106-vision-preview']['output_price'], 30.00)

    def test_model_name_none(self):
        # Test that the function raises an error if the model name is not specified
        with self.assertRaises(ValueError):
            calculate_cost()

    def test_invalid_model_name(self):
        # Test that the function raises an error for an invalid model name
        with self.assertRaises(ValueError):
            calculate_cost(model_name='invalid-model', input_tokens=1000, output_tokens=1000)

if __name__ == '__main__':
    unittest.main()
