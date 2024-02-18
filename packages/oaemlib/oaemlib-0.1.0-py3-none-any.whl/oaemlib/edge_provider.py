import logging
from functools import lru_cache
from typing import Protocol

from pointset import PointSet

from oaemlib.edge import Edge
from oaemlib.filepicker import FilePicker
from oaemlib.gml import GMLData, GMLFileList, parse_citygml
from oaemlib.wfs import WFSSettings, edge_list_from_wfs

logger = logging.getLogger("root")


class EdgeProvider(Protocol):
    """
    Protocol for edge providers.

    Edge providers are used to retrieve building edges from a given position.
    They need to implement the get_edges method.
    """

    def get_edges(self, pos: PointSet) -> list[Edge]: ...


class LocalEdgeProvider:
    """
    Edge provider for local CityGML data.

    This edge provider uses local CityGML data to retrieve building edges from a given position.
    The level of detail (LOD) of the data can be specified as 1 or 2. The path to the corresponding
    LOD1 or LOD2 data needs to be provided.
    """

    def __init__(self, file_picker: FilePicker) -> None:
        self.file_picker = file_picker

    @lru_cache(maxsize=128)
    def _build_gml_data(self, filepaths: GMLFileList) -> GMLData:
        """
        Builds a GMLData object from a list of filepaths.

        The GMLData object is cached to avoid unnecessary parsing of the same file(s).
        """
        coords: list[list[float]] = []

        for file in filepaths.files:
            coords.extend(parse_citygml(file, self.file_picker.settings.lod))

        return GMLData(coordinates=coords)

    @lru_cache(maxsize=512)
    def get_edges(self, position: PointSet) -> list[Edge]:
        """
        Returns a list of edges for a given position.
        """
        filepaths = self.file_picker.get_files(position)
        gml_data = self._build_gml_data(filepaths)
        return gml_data.query_edges(
            position.xyz, n_range=self.file_picker.settings.n_range
        )


class WFSEdgeProvider:
    """
    Edge provider for WFS data.

    This edge provider uses the WFS API to retrieve building edges from a given position.
    By default, the WFS API of North Rhine-Westphalia (NRW), Germany is used. This API
    only provides LOD1 data.
    """

    def __init__(self, wfs_settings: WFSSettings) -> None:
        self.wfs_settings = wfs_settings

    def get_edges(self, position: PointSet) -> list[Edge]:
        return edge_list_from_wfs(position=position, wfs_settings=self.wfs_settings)
