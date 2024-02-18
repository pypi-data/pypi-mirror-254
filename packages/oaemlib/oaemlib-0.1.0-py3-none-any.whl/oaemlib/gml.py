import os
from dataclasses import dataclass, field
from functools import lru_cache
from typing import TypeAlias

import numpy as np
import xmltodict
from scipy.spatial import KDTree

from oaemlib.edge import Edge

CoordinateList: TypeAlias = list[list[float]]


@dataclass
class GMLFileList:
    """
    Hashable list of gml files.

    This class is used to cache the gml files for a given position.
    """

    data_path: str
    files: list[str] = field(default_factory=list)

    def add(self, file: str) -> None:
        self.files.append(os.path.join(self.data_path, file))

    def __hash__(self) -> int:
        return "".join(sorted(self.files)).__hash__()


class GMLData:
    """
    Class representing the content of one or more gml files.

    For efficient querying of the building edges, a KDTree is built from the coordinates.
    """

    def __init__(self, coordinates: CoordinateList) -> None:
        self.coordinates = np.array(coordinates)
        self.kdtree = (
            KDTree(np.r_[self.coordinates[:, :2], self.coordinates[:, 3:5]])
            if coordinates
            else None
        )
        self.edges = (
            [
                Edge(start=edge_coord[:3], end=edge_coord[3:])
                for edge_coord in self.coordinates
            ]
            if coordinates
            else []
        )

    def query_edges(self, pos: np.ndarray, n_range: float = 100.0) -> list[Edge]:
        """
        Returns a list of edges for a given position using the KDTree.
        """
        if not self.edges:
            return []

        query_indices = self.kdtree.query_ball_point(pos[:, :2].flatten(), r=n_range)
        unique_indices = {index % len(self.edges) for index in query_indices}
        return [self.edges[index] for index in unique_indices]


def handle_surface_member(surface_member: dict) -> CoordinateList:
    polygon: dict | str = (
        surface_member.get("gml:Polygon", {})
        .get("gml:exterior", {})
        .get("gml:LinearRing", {})
        .get("gml:posList", {})
    )

    if isinstance(polygon, dict):
        polygon = str(polygon.get("#text", ""))

    if not polygon:
        return []

    coords = [float(c) for c in polygon.split(" ")]

    if len(coords) % 3 != 0:
        return []

    if len(coords) < 6:
        return []

    return [coords[i : i + 6] for i in range(0, len(coords) - 3, 3)]


def extract_surface_members(surface: dict) -> CoordinateList:
    surface_members: list | dict = (
        surface.get("bldg:lod2MultiSurface", {})
        .get("gml:MultiSurface", {})
        .get("gml:surfaceMember", [])
    )

    if not surface_members:
        return []

    coords: CoordinateList = []

    if isinstance(surface_members, list):
        for surface_member in surface_members:
            coords.extend(handle_surface_member(surface_member))
    else:
        coords.extend(handle_surface_member(surface_members))

    return coords


def parse_building_bounds(bounds: list[dict]) -> CoordinateList:
    building_coordinates: CoordinateList = []
    for surfaces in bounds:
        for surface in surfaces.values():
            building_coordinates.extend(extract_surface_members(surface))

    return building_coordinates


def parse_building_data(building_data: dict) -> CoordinateList:
    building_coordinates: CoordinateList = []

    if "bldg:Building" not in building_data:
        return building_coordinates

    building = building_data["bldg:Building"]

    if "bldg:boundedBy" in building:
        bounded_by = [building["bldg:boundedBy"]]
        for bounds in bounded_by:
            building_coordinates.extend(parse_building_bounds(bounds))

    if "bldg:consistsOfBuildingPart" in building:
        building_parts = building["bldg:consistsOfBuildingPart"]
        for part in building_parts:
            building_part = part["bldg:BuildingPart"]
            bounds = building_part["bldg:boundedBy"]
            building_coordinates.extend(parse_building_bounds(bounds))

    return building_coordinates


def extract_lod2_coords(gml: str) -> CoordinateList:
    data = xmltodict.parse(gml)
    building_coordinates: CoordinateList = []

    if "core:CityModel" not in data:
        return building_coordinates

    if "core:cityObjectMember" not in data["core:CityModel"]:
        return building_coordinates

    buildings = data["core:CityModel"]["core:cityObjectMember"]

    if not isinstance(buildings, list):
        buildings = [buildings]

    for bdata in buildings:
        building_coordinates.extend(parse_building_data(bdata))

    return building_coordinates


def extract_lod1_coords(gml: str) -> CoordinateList:
    data = xmltodict.parse(gml)
    cityobject_members = data.get("core:CityModel", {}).get("core:cityObjectMember", {})

    building_coordinates: CoordinateList = []
    if not cityobject_members:
        return building_coordinates

    if not isinstance(cityobject_members, list):
        cityobject_members = [cityobject_members]

    for cobj in cityobject_members:
        bldg = cobj.get("bldg:Building", {})

        # single lod1Solid
        if lod1solid := bldg.get("bldg:lod1Solid", {}):
            building_coordinates.extend(parse_lod1solid(lod1solid))

        # multiple lod1Solids
        if bldg_parts := bldg.get("bldg:consistsOfBuildingPart", {}):
            for bpart in bldg_parts:
                lod1solid = bpart.get("bldg:BuildingPart", {}).get("bldg:lod1Solid", {})
                building_coordinates.extend(parse_lod1solid(lod1solid))

    return building_coordinates


def parse_lod1solid(lod1solid: dict) -> CoordinateList:
    """
    Parses the lod1Solid element of a building

    Args:
        lod1solid (dict): The lod1Solid element of a building.

    Returns:
        list[float]: A list representing the start and end points of the building edges
    """
    surface_members = (
        lod1solid.get("gml:Solid", {})
        .get("gml:exterior", {})
        .get("gml:CompositeSurface", {})
        .get("gml:surfaceMember", {})
    )

    building_coordinates: CoordinateList = []

    if not surface_members:
        return building_coordinates

    for surface in surface_members:
        building_coordinates.extend(handle_surface_member(surface))

    return building_coordinates


@lru_cache(maxsize=128)
def parse_citygml(filepath: str, lod: int = 2) -> CoordinateList:
    if not filepath.endswith(".gml"):
        return []

    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File {filepath} not found!")

    with open(filepath, "r", encoding="utf-8") as f:
        data = f.read()
        return extract_lod2_coords(data) if lod == 2 else extract_lod1_coords(data)
