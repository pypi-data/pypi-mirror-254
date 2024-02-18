from dataclasses import dataclass
from io import TextIOBase
from pathlib import Path


@dataclass
class Scan:
    """
    .. code-block:: python
        ls = [
            Scan(
                path=Path("src/test/test.xy"),
                legend="test1",
                scantime_s=1.0,
            ),
            Scan(
                path=Path("src/test/test.xy"),
                legend="test2",
                scantime_s=2.0,
            ),
            Scan(
                path=Path("src/test/test.xy"),
                legend="test3",
                scantime_s=3.0,
            ),
        ]
        paths = [l.path for l in ls]
        legends = [l.legend for l in ls]
        scantimes = [l.scantime_s for l in ls]
    """

    path: TextIOBase | str | Path
    legend: str
    scantime_s: float


def example():
    ls = [
        Scan(
            path=Path("src/test/test.xy"),
            legend="test1",
            scantime_s=1.0,
        ),
        Scan(
            path=Path("src/test/test.xy"),
            legend="test2",
            scantime_s=2.0,
        ),
        Scan(
            path=Path("src/test/test.xy"),
            legend="test3",
            scantime_s=3.0,
        ),
    ]
    paths = [l.path for l in ls]
    legends = [l.legend for l in ls]
    scantimes = [l.scantime_s for l in ls]

    @dataclass
    class AddedScan(Scan):
        color: str

    AddedScan("src/test/test.xy", "test1", 1.0, "red")
