import re
from collections import OrderedDict
import pandas as pd


def generate_mapping(ql):

    def field_mapping():
        mapping = OrderedDict(ql.get("fields"))
        mapping_table = pd.DataFrame({
            "<u>Sigma field</u>": mapping.keys(),
            f"<u>QRadar {ql.get('name')} field</u>": [
                re.sub(r"[\[\]']", "", str(val)) for val in mapping.values()
            ]})
        return mapping_table.to_markdown(index=False)

    def log_source_mapping(log_source):
        mapping = OrderedDict(ql.get(log_source))
        log_source_device_type = [
            [list(ql.get("log_sources").keys())[list(
                ql.get("log_sources").values()).index(device_type)] for device_type
             in device_types]
            for device_types in mapping.values()
        ]
        mapping_table = pd.DataFrame({
            f"<u>Sigma {log_source}</u>": mapping.keys(),
            f"<u>QRadar {ql.get('name')} {ql.get('log_source_name')} name</u>": [
                re.sub(r"[\[\]']", "", str(val)) for val in log_source_device_type
            ],
            f"<u>QRadar {ql.get('name')} {ql.get('log_source_name')} id</u>": [
                re.sub(r"[\[\]']", "", str(val)) for val in mapping.values()
            ]}
        )
        return mapping_table.to_markdown(index=False)

    mappings = {
        "{{field_mapping}}": field_mapping(),
        "{{service_mapping}}": log_source_mapping("service"),
        "{{product_mapping}}": log_source_mapping("product")
    }
    with open(f"readme_template.md", 'r') as f:
        template = f.read()
        for t, m in mappings.items():
            template = template.replace(t, m)
    with open(f"README.md", 'w+') as f:
        f.write(template)
