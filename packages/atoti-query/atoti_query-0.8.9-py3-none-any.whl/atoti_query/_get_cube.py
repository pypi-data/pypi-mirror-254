from __future__ import annotations

from ._cube_discovery import IndexedCubeDiscovery, IndexedDiscoveryCube


def get_cube(
    cube_name: str, /, *, discovery: IndexedCubeDiscovery
) -> IndexedDiscoveryCube:
    try:
        return next(
            (
                cube
                for catalog in discovery["catalogs"].values()
                for cube in catalog["cubes"].values()
                if cube["name"] == cube_name
            ),
        )
    except StopIteration as error:
        raise ValueError(
            f"No cube named `{cube_name}` in the passed discovery."
        ) from error
