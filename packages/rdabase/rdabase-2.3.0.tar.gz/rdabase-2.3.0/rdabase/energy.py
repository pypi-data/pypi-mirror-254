"""
ENERGY-related helpers
"""

from collections import defaultdict
from typing import List, Dict, Tuple, Set, Any, NamedTuple

from .graph import Graph
from .misc import Assignment
from .union_find import StrUnionFind, IntUnionFind
from .constants import geoid_field


class LatLong(NamedTuple):
    lat: float
    long: float


class Point(NamedTuple):
    geoid: str
    pop: float
    ll: LatLong


class IndexedPoint(NamedTuple):
    ll: LatLong
    pop: float


class IndexedWeightedAssignment(NamedTuple):
    site: int
    point: int
    pop: float


#


def mkPoints(
    data: Dict[str, Dict[str, str | int]],  # indexed by GEOID
    shapes: Dict[str, Any],
) -> List[Point]:
    """Join population from precinct data with x,y location from precinct shapes by GEOID."""

    points: List[Point] = list()

    for geoid, values in data.items():
        loc: LatLong = LatLong(shapes[geoid]["center"][1], shapes[geoid]["center"][0])
        point: Point = Point(geoid=geoid, pop=int(values["TOTAL_POP"]), ll=loc)

        points.append(point)

    return points


def mkAdjacencies(graph: Graph) -> List[Tuple[str, str]]:
    """Convert an adjacency graph to a list of pairs of adjacent GEOIDs."""

    adjacencies: List[Tuple[str, str]] = list()
    for one, two in graph.adjacencies():
        if one != "OUT_OF_STATE" and two != "OUT_OF_STATE":
            adjacencies.append((one, two))

    return adjacencies


#


def index_geoids(
    points: List[Point],
) -> Dict[str, int]:
    """Index point GEOIDs by offset."""

    offset_by_geoid: Dict[str, int] = {p.geoid: i for i, p in enumerate(points)}
    return offset_by_geoid


def index_data(data: List[Dict[str, str | int]]) -> Dict[str, Dict[str, str | int]]:
    """Index precinct data by GEOID. For making points."""

    indexed: Dict[str, Dict[str, str | int]] = dict()
    for row in data:
        geoid: str = str(row[geoid_field])
        indexed[geoid] = row

    return indexed


#


def index_points(
    points: List[Point],
    epsilon: float = 0.01,
) -> List[IndexedPoint]:
    """Index points by GEOID offset."""

    ps: List[IndexedPoint] = list()
    for p in points:
        ps.append(IndexedPoint(p.ll, p.pop))

    assert epsilon > 0 or sum(p.pop for p in ps) == sum(p.pop for p in points)

    return ps


def index_pairs(
    offset_by_geoid: Dict[str, int],
    pairs: List[Tuple[str, str]],
) -> List[Tuple[int, int]]:
    """Index adjacent pairs of precincts by GEOID offset."""

    pairs = [
        (p1, p2) for p1, p2 in pairs if p1 != "OUT_OF_STATE" and p2 != "OUT_OF_STATE"
    ]
    adjacent_pairs: List[Tuple[int, int]] = [
        (offset_by_geoid[p1], offset_by_geoid[p2]) for p1, p2 in pairs
    ]

    geoids: Set[str] = set(offset_by_geoid.keys())
    report_disconnect(pairs, geoids, "all points")

    return adjacent_pairs


def index_assignments(
    assignments: List[Assignment],
    offset_by_geoid: Dict[str, int],
    pop_by_geoid: Dict[str, int],
) -> List[IndexedWeightedAssignment]:
    """Index precinct assignments to districts by GEOID offset."""

    indexed_assignments: List[IndexedWeightedAssignment] = list()
    for p in assignments:
        indexed: IndexedWeightedAssignment = IndexedWeightedAssignment(
            site=int(p.district) - 1,
            point=offset_by_geoid[p.geoid],
            pop=float(pop_by_geoid[p.geoid]),
        )
        indexed_assignments.append(indexed)

    return indexed_assignments


def report_disconnect(pairs: List[Tuple[str, str]], geoids: Set[str], msg: str):
    ds = StrUnionFind(geoids)
    for p1, p2 in pairs:
        if (
            p1 != "OUT_OF_STATE"
            and p2 != "OUT_OF_STATE"
            and p1 in geoids
            and p2 in geoids
        ):
            ds.merge(p1, p2)
    if ds.n_subsets > 1:
        subset: Set[str] = min(ds.subsets(), key=len)
        if len(subset) > 10:
            summary = f"{list(subset)[:10]}..."
        else:
            summary = f"{list(subset)}"
        print(
            f"WARNING: {ds.n_subsets} disconnected {msg} regions, including: {summary}"
        )


#


def calc_energy(
    assignments: List[IndexedWeightedAssignment], points: List[IndexedPoint]
) -> float:
    """Calculate the energy of a map."""

    sites: List[LatLong] = get_centroids(assignments, points)
    total: float = sum(
        a.pop
        * squared_distance(
            sites[a.site], points[a.point].ll
        )  # not sqrt!!! moment of inertia!
        for a in assignments
    )

    return total


def squared_distance(a: LatLong, b: LatLong) -> float:
    return (a.lat - b.lat) * (a.lat - b.lat) + (a.long - b.long) * (a.long - b.long)


def get_centroids(
    assigns: List[IndexedWeightedAssignment], points: List[IndexedPoint]
) -> List[LatLong]:
    bysite: defaultdict[int, List[IndexedWeightedAssignment]] = defaultdict(list)
    for a in assigns:
        bysite[a.site].append(a)
    cs: List[LatLong] = []
    top: int = max(s for s in bysite.keys())
    for site in range(top + 1):
        persite: List[IndexedWeightedAssignment] = bysite[site]
        total: float = sum(a.pop for a in persite)
        lat: float = sum(points[a.point].ll.lat * a.pop for a in persite) / total
        long: float = sum(points[a.point].ll.long * a.pop for a in persite) / total
        cs.append(LatLong(lat, long))
    return cs


### END ###
