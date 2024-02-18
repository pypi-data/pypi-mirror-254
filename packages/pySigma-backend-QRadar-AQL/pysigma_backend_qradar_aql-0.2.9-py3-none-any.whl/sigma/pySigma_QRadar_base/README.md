# `PySigma QRadar`
This is the QRadar backend submodule for 
[pySigma QRadar AQL](https://github.com/IBM/pySigma-backend-QRadar-aql).

### Backend
- [QRadarBackend](QRadarBackend.py): It provides a base backend for pySigma 
  QRadar AQL.

### Pipelines
- [QRadar_fields_pipeline](QRadarFieldsPipeline.py): Supports only the 
  mapped `Sigma fields` in the field 
mapping.
- [QRadar_payload_pipeline](QRadarPayloadPipeline.py): Uses `payload` search 
  instead of unmapped fields.

  For payload search, the following value types are not supported:
  - Boolean
  - Null
  - CIDR
  - Regular Expression
  - Numeric Comparison
  
## License
pySigma_QRadar_base is licensed under the MIT [License](./LICENSE).

## Maintainers
* [Cyber Center of Excellence - IBM](https://github.com/noaakl/)
