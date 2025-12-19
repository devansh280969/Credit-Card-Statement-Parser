from parsers.hdfc import HDFCParser
from parsers.icici import ICICIParser
from parsers.citi import CITIParser
from parsers.axis import AxisParser
from parsers.idfc import IDFCParser


def get_parser(issuer: str):
    if issuer == "HDFC":
        return HDFCParser()
    if issuer == "ICICI":
        return ICICIParser()
    if issuer == "CITI":
        return CITIParser()
    if issuer == "AXIS":
        return AxisParser()
    if issuer == "IDFC":
        return IDFCParser()

    return None
