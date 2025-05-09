from langchain_core.tools import tool

@tool
def fuel_cost_calculator(distance_km: float, fuel_efficiency_km_per_l: float, fuel_price_per_l: float) -> str:
    """Calculates the fuel cost for a trip."""
    if fuel_efficiency_km_per_l <= 0:
        return "Fuel efficiency must be greater than zero."
    liters_needed = distance_km / fuel_efficiency_km_per_l
    total_cost = liters_needed * fuel_price_per_l
    return f"Estimated fuel cost: AED {total_cost:.2f}"
