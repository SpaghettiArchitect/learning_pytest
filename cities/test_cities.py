from city_functions import get_formatted_city


def test_city_country():
    """Do cities like 'Santiago, Chile' work?"""
    formatted_city = get_formatted_city("santiago", "chile")
    assert formatted_city == "Santiago, Chile"


def test_city_country_population():
    """Do cities like 'Santiago, Chile - population 5000000' work?"""
    formatted_city = get_formatted_city("santiago", "chile", population=5000000)
    assert formatted_city == "Santiago, Chile - population 5000000"
