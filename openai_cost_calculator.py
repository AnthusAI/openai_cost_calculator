from decimal import Decimal
from pricing_information import model_pricing

def calculate_cost(model_name=None, input_tokens=0, output_tokens=0):
    """
    Calculate the cost of using an OpenAI model based on the number of input and output tokens.

    Parameters:
    - model_name (str): Name of the model. Defaults to None.
    - input_tokens (int): Number of input tokens. Defaults to 0.
    - output_tokens (int): Number of output tokens. Defaults to 0.

    Returns:
    - float: The cost of the request.
    """
    if model_name is None:
        raise ValueError("Model name must be specified.")

    pricing_info = model_pricing.get(model_name)
    if pricing_info is None:
        raise ValueError(f"Model {model_name} not found in pricing list.")

    input_price = Decimal(pricing_info['input_price'])
    output_price = Decimal(pricing_info['output_price'])
    total_cost = (Decimal(input_tokens) * input_price + Decimal(output_tokens) * output_price) / Decimal('1000000')
    return total_cost
