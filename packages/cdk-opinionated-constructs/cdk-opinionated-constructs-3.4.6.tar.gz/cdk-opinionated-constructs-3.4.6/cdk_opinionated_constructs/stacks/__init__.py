"""TBD."""

import aws_cdk.aws_ssm as ssm


@staticmethod
def set_ssm_parameter_tier_type(*, values: dict[list, dict]) -> ssm.ParameterTier:
    """
    Sets the tier type of the parameter based on the total characters of
    the key and value.

    Parameters:          
        - values: The environment configuration properties.

    Returns:
      - The tier type.
    """

    total_value_characters = sum(len(str(v)) for v in values.values())
    total_key_characters = sum(len(str(v)) for v in values)
    total_characters = total_key_characters + total_value_characters
    tier_type = ssm.ParameterTier.STANDARD
    if total_characters > 4096:
        tier_type = ssm.ParameterTier.ADVANCED
    return tier_type
