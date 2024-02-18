import copy
import re
import warnings
from dataclasses import dataclass
from typing import Optional, Union, Iterable, List, Pattern

from sigma.processing.transformations import SetStateTransformation, \
    FieldMappingTransformation

# See https://sigmahq-pysigma.readthedocs.io/en/latest/Processing_Pipelines.html
# for further documentation.
from sigma.rule import SigmaDetection, SigmaRule
from sigma.types import SigmaType

IPV4 = "ipv4"
IPV6 = "ipv6"


def is_ipv6(val):
    return re.match('^[0-9a-zA-Z:]+$', val) and re.search(
        r"^([0-9A-Fa-f]{0,4}:){0,7}[0-9A-Fa-f]{0,4}$", val)


def is_ipv4(val):
    return re.match(r"^(?:\d{1,3}\.){0,3}\d{0,3}(?:\/\d{1,2})?$", val)


def ip_type(value):
    ip = None
    if is_ipv6(value):
        ip = IPV6
    elif is_ipv4(value):
        ip = IPV4
    return ip


@dataclass
class QRadarFieldMappingTransformation(FieldMappingTransformation):
    """
    Map a field name to one or multiple different, and quote if the field contains
    spaces and doesn't contain parentheses.
    """
    field_quote_pattern: Pattern

    def apply_field_name(self, field: str) -> Union[str, List[str]]:
        mappings = copy.deepcopy(self.get_mapping(field)) or []
        if isinstance(mappings, str):
            mappings = [mappings]
        for i, mapping in enumerate(mappings):
            if not self.field_quote_pattern.match(mapping):
                mappings[i] = '"' + mapping + '"'
        return mappings


@dataclass
class SetEventSourceTransformation(SetStateTransformation):
    """
    set the logsources values from the field devicetype in state, to use it in the
    backend's finalize query
    """
    device_type_field_name: str
    log_source_mapping: dict

    def device_type_mapping(
            self, field: str, val: SigmaType
    ) -> Optional[Union[SigmaType, Iterable[SigmaType]]]:
        log_sources = self.log_source_mapping
        str_value = str(val)
        if field == self.device_type_field_name:
            if str_value in log_sources:
                return log_sources[str_value]
            warnings.warn(
                f"'{val}' is not a supported log source type and therefore is being "
                f"removed"
            )
            return None

    def detection_log_sources(self, detection: SigmaDetection, device_types: list):
        for i, detection_item in enumerate(detection.detection_items):
            if isinstance(detection_item,
                          SigmaDetection):  # recurse into nested detection items
                self.detection_log_sources(detection_item, device_types)
            else:
                for value in detection_item.value:
                    res = self.device_type_mapping(detection_item.field, value)
                    if res:
                        if isinstance(res, Iterable) and not isinstance(res, SigmaType):
                            device_types.extend(res)
                        else:
                            device_types.append(res)
                    self.processing_item_applied(detection_item)
        return device_types

    def apply(self, pipeline, rule: SigmaRule) -> None:
        device_types = []
        for detection in rule.detection.detections.values():
            log_source = self.detection_log_sources(detection, device_types) or []
            device_types.extend(log_source)
        self.val = device_types
        super().apply(pipeline, rule)
