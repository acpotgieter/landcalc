"""Adds custom Map class that extends the folium Map class."""
import folium

class Map(folium.Map):
    """Custom Map class that extends the folium Map class."""

    def __init__(self, center=(0, 0), zoom=2, **kwargs):
        """Initialize the Map with a center and zoom level."""
        super().__init__(location=center, zoom_start=zoom, **kwargs)
