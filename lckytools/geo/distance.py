from math import atan2, cos, radians, sin, sqrt


def haversine(
    latitude1: float,
    longitude1: float,
    latitude2: float,
    longitude2: float,
) -> float:
    """
    Calculate the great-circle distance between two points on the Earth's surface.

    Uses the Haversine formula to compute the distance based on latitude and longitude coordinates.
    This formula accounts for the spherical shape of the Earth, making it more accurate than
    flat-surface distance calculations.

    Parameters
    ----------
    latitude1 : float
        Latitude of the first point in decimal degrees.
    longitude1 : float
        Longitude of the first point in decimal degrees.
    latitude2 : float
        Latitude of the second point in decimal degrees.
    longitude2 : float
        Longitude of the second point in decimal degrees.

    Returns
    -------
    float
        Distance between the two points in meters.

    Examples
    --------
    >>> haversine(52.2296756, 21.0122287, 41.8919300, 12.5113300)
    1312792.7623126339

    Note
    ----
    The Haversine formula is an equation important in navigation, giving great-circle distances
    between two points on a sphere from their longitudes and latitudes. This implementation assumes
    a spherical Earth, which can result in small errors in distance calculations.
    """
    # Radius of the Earth in meters
    earth_radius = 6371000

    # Convert degrees to radians
    phi1 = radians(latitude1)
    phi2 = radians(latitude2)
    delta_phi = radians(latitude2 - latitude1)
    delta_lambda = radians(longitude2 - longitude1)

    # Haversine formula
    chord_length_squared = (
        sin(delta_phi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(delta_lambda / 2) ** 2
    )
    angular_distance = 2 * atan2(
        sqrt(chord_length_squared), sqrt(1 - chord_length_squared)
    )

    return earth_radius * angular_distance  # Distance in meters
