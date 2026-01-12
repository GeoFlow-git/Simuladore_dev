from Prop_calculator import visocity_calculator


def test_visocity_calculator():
    
    # Test case 1: Standard values
    mass = 10.0  # kg
    volume = 2.0  # m^3
    expected_viscosity = (mass / volume) * 0.001
    assert abs(visocity_calculator(mass, volume) - expected_viscosity) < 1e-6

    # Test case 2: Zero volume (should handle division by zero)
    mass = 5.0  # kg
    volume = 0.0  # m^3
    try:
        visocity_calculator(mass, volume)
        assert False, "Expected an exception for zero volume"
    except ZeroDivisionError:
        pass

    # Test case 3: Negative mass (should handle invalid input)
    mass = -5.0  # kg
    volume = 2.0  # m^3
    try:
        visocity_calculator(mass, volume)
        assert False, "Expected an exception for negative mass"
    except ValueError:
        pass

    # Test case 4: Large values
    mass = 1e6  # kg


