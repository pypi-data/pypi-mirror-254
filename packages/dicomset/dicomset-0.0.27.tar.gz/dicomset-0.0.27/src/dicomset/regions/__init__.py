from typing import List

from dicomset import types

from .colours import to_255, RegionColours
from .list import RegionList
from .regions import RegionNames
from .tolerances import get_region_tolerance, RegionTolerances

def is_region(name: str) -> bool:
    return name in RegionNames

def region_to_list(region: types.PatientRegions) -> List[str]:
    if type(region) == str:
        if region == 'all':
            return RegionNames
        else:
            if not region in RegionNames:
                raise ValueError(f"'{region}' is not a valid region. Should be one of '{RegionNames}'.")
            return [region]
    else:
        for r in region:
            if not r in RegionNames:
                raise ValueError(f"'{r}' is not a valid region. Should be one of '{RegionNames}'.")
        return region
