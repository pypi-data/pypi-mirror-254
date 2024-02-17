"""A component for displaying a map with layers in streamlit."""

from typing import List

import folium
from streamlit_folium import st_folium


def get_map_url_and_name_for_layers(layers: List[dict]) -> List[dict]:
    """From a given set of layers from the EBX API, return a list of dicts with the map URL and name.
    
    Args:
        layers (List[dict]): The layers from the EBX API.

    Returns:
        List[dict]: The list of dicts with the map URL and name.
    """
    out_layers = []

    for layer in layers:
        layer_name = layer.get("name")

        for group in layer.get("groups"):
            out_layers.append({
                "name": f"{layer_name} - {group.get('label')}",
                "map_url": group.get("mapURL")
            })

    return out_layers

def get_bounding_box_for_layers(layers: List[dict]) -> List[float]:
    """From a given set of layers from the EBX API, return the bounding box.
    
    Args:
        layers (List[dict]): The layers from the EBX API.

    Returns:
        List[float]: The bounding box.
    """
    bboxes = [layer.get("bbox") for layer in layers]

    max_NE_lon, min_NE_lat = bboxes[0].get("NE")
    min_SW_lon, max_SW_lat = bboxes[0].get("SW")

    for bbox in bboxes[1:]:
        NE_lon, NE_lat = bbox.get("NE")
        SW_lon, SW_lat = bbox.get("SW")

        max_NE_lon = max(max_NE_lon, NE_lon)
        min_NE_lat = min(min_NE_lat, NE_lat)
        min_SW_lon = min(min_SW_lon, SW_lon)
        max_SW_lat = max(max_SW_lat, SW_lat)

    return [min_NE_lat, max_NE_lon, max_SW_lat, min_SW_lon]

def ebx_map(layers):
    """For a given set of layers from a run doc, display a map with the layers."""
    bbox = get_bounding_box_for_layers(layers)
    layers = get_map_url_and_name_for_layers(layers)
    
    center_lat = (bbox[0] + bbox[2]) / 2
    center_lon = (bbox[1] + bbox[3]) / 2

    m = folium.Map(location=[center_lat, center_lon], zoom_start=10)

    attr = (
        '&copy; <a href="https://earthblox.io/">Earth Blox</a>'
    )

    for layer in layers:
        folium.TileLayer(
            tiles=layer.get("map_url"),
            name=layer.get("name"),
            attr=attr,
            overlay=True,
        ).add_to(m)

    folium.LayerControl().add_to(m)

    st_folium(m)