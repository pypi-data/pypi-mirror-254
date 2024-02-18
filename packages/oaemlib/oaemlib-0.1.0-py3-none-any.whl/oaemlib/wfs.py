import logging
from dataclasses import dataclass

import numpy as np
import requests
from pointset import PointSet

from oaemlib.edge import Edge
from oaemlib.gml import extract_lod1_coords

logger = logging.getLogger("root")


@dataclass
class WFSSettings:
    url: str
    base_request: str
    epsg: int
    n_range: float = 100.0


def edge_list_from_wfs(position: PointSet, wfs_settings: WFSSettings) -> list[Edge]:
    """
    Sends a request to the WFS server to retrieve the Level of Detail 1 (LOD1) CityGML data
    for the specified position.

    Args:
        position (PointSet): The position to retrieve the data for.
        wfs_settings (WFSSettings): The settings for the WFS server.

    Returns:
        list[Edge]: A list of Edge objects representing the retrieved CityGML data.

    Raises:
        requests.RequestException: If the WFS request fails.
    """
    position.to_epsg(wfs_settings.epsg)
    request_url = create_request(pos=position, wfs_settings=wfs_settings)
    logger.debug("Sending request %s", request_url)
    response = requests.get(request_url, timeout=10)
    logger.debug("received answer. Status code: %s", response.status_code)

    if response.status_code != 200:
        raise requests.RequestException("WFS request failed!")

    return parse_response(response)


def create_request(pos: PointSet, wfs_settings: WFSSettings) -> str:
    """
    Creates a WFS request URL for the specified position and range.

    Args:
        pos (PointSet): The position to retrieve the data for.
        wfs_settings (WFSSettings): The settings for the WFS server.

    Returns:
        str: The WFS request URL.

    """
    n_range = wfs_settings.n_range
    bbox_bl = [pos.x - n_range, pos.y - n_range]
    bbox_tr = [pos.x + n_range, pos.y + n_range]
    bbox = f"BBOX={bbox_bl[0]},{bbox_bl[1]},{bbox_tr[0]},{bbox_tr[1]},urn:ogc:def:crs:EPSG::{wfs_settings.epsg}"
    return f"{wfs_settings.url}?{wfs_settings.base_request}&{bbox}"


def parse_response(response: requests.Response) -> list[Edge]:
    """
    Parses the response from the WFS server and returns a list of edges representing
    the building roof footprints.

    Args:
        response (Response): The response object from the WFS server.

    Returns:
        list[Edge]: A list of edges representing the building roof footprints.
    """
    logger.debug("parsing response ...")
    building_coordinates: np.ndarray = np.array(
        extract_lod1_coords(str(response.content, encoding="utf-8"))
    )

    return [
        Edge(start=edge_coord[:3], end=edge_coord[3:])
        for edge_coord in building_coordinates
    ]
