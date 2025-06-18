def get_formatted_city(city: str, country: str, population: int = 0) -> str:
    """Create a neatly formatted city name."""
    city_name = f"{city}, {country}".title()
    if population:
        city_name += f" - population {population}"
    return city_name
