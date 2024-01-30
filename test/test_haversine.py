from lckytools.geo.distance import haversine


def test_haversine():
    # Test known values
    # Coordinates of New York City and London
    lat_nyc, lon_nyc = 40.7128, -74.0060
    lat_london, lon_london = 51.5074, -0.1278

    # Expected distance in meters (approximately)
    # The shortest distance (air line) between London and New-York
    # is 3,461.34 mi (5,570.48 km).
    expected_distance = 5570.48 * 1000

    # Calculate distance using haversine function
    calculated_distance = haversine(lat_nyc, lon_nyc, lat_london, lon_london)

    # Check if the calculated distance is close to the expected value
    # Allowing a small margin of error
    assert abs(calculated_distance - expected_distance) < 1000


def test_haversine_zero_distance():
    # Test with the same coordinates for both points
    lat, lon = 52.2296756, 21.0122287

    # Expected distance is 0
    expected_distance = 0

    # Calculate distance
    calculated_distance = haversine(lat, lon, lat, lon)

    # Check if the distance is 0
    assert calculated_distance == expected_distance
