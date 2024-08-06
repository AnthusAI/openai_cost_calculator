import logging
from decimal import Decimal
from openai_cost_calculator.pricing_information import model_pricing

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate_cost(model_name=None, input_tokens=0, output_tokens=0):
    """
    Calculate the cost of using an OpenAI model based on the number of input and output tokens.

    Parameters:
    - model_name (str): Name of the model. Defaults to None.
    - input_tokens (int): Number of input tokens. Defaults to 0.
    - output_tokens (int): Number of output tokens. Defaults to 0.

    Returns:
    - dict: A dictionary containing input_cost, output_cost, and total_cost.
    """
    if model_name is None:
        raise ValueError("Model name must be specified.")

    logger.info(f"Calculating cost for model: {model_name}")

    # Handle fine-tuned models
    if model_name.startswith('ft:'):
        base_model = model_name.split(':')[1]
    else:
        base_model = model_name

    # Try to match the model name
    pricing_info = model_pricing.get(base_model)

    if pricing_info is None:
        logger.error(f"No pricing information found for model: {model_name}")
        raise ValueError(f"Model {model_name} not found in pricing list.")

    input_price = Decimal(pricing_info['input_price'])
    output_price = Decimal(pricing_info['output_price'])
    input_cost = (Decimal(input_tokens) * input_price) / Decimal('1000000')
    output_cost = (Decimal(output_tokens) * output_price) / Decimal('1000000')
    total_cost = input_cost + output_cost

    logger.info(f"Calculated costs: input={input_cost}, output={output_cost}, total={total_cost}")

    return {
        'input_cost': input_cost,
        'output_cost': output_cost,
        'total_cost': total_cost
    }