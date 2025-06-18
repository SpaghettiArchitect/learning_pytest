def get_formatted_city(city: str, country: str) -> str:
    """Create a neatly formatted city name."""
    city_name = f"{city}, {country}"
    return city_name.title()
