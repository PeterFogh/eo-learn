"""
A collection of input and output EOTasks
"""

from .sentinelhub_service import SentinelHubOGCInput, SentinelHubWMSInput, SentinelHubWCSInput, S2L1CWMSInput, \
    S2L1CWCSInput, L8L1CWMSInput, L8L1CWCSInput, S2L2AWMSInput, S2L2AWCSInput, S1IWWMSInput, S1IWWCSInput, \
    DEMWMSInput, DEMWCSInput, AddSen2CorClassificationFeature
from .sentinelhub_service_xarray import (SentinelHubOGCInputXarray, SentinelHubWMSInputXarray,
    SentinelHubWCSInputXarray, S2L1CWMSInputXarray, S2L1CWCSInputXarray, L8L1CWMSInputXarray, L8L1CWCSInputXarray,
    S2L2AWMSInputXarray, S2L2AWCSInputXarray, S1IWWMSInputXarray, S1IWWCSInputXarray, DEMWMSInputXarray, DEMWCSInputXarray,
    AddSen2CorClassificationFeatureXarray)
from .geopedia import AddGeopediaFeature
from .local_io import ExportToTiff, ImportFromTiff

__version__ = '0.5.0'
