def visocity_calculator(mass, volume):
    """
    Calculate the viscosity of a fluid given its mass and volume.

    Parameters:
    mass (float): Mass of the fluid in kilograms.
    volume (float): Volume of the fluid in cubic meters.

    Returns:
    float: Viscosity of the fluid in Pascal-seconds (Pa·s).
    """
    density = mass / volume  # Density in kg/m^3
    viscosity = density * 0.001  # Simplified formula for demonstration
    return viscosity