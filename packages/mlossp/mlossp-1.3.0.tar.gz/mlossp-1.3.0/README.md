# Satellite Data Preprocessor

A package built for preprocessing a list of geopandas dataframe pickles or GeoJSON files by joining them spatially and concatenating them into time-series numpy pickles.

### Usage:
* Create an instance of Preprocessor and provide the path to a config json file.
* Call Preprocessor.preprocess to preprocess data according to the provided config.
* It is possible to define multiple configs for different data sources. In this case, Preprocesser.preprocess_multi will load and individually preprocess each config file.

```python
import mlossp as sp

config_path = "config.json"
preprocessor = sp.Preprocesser(config_path)
preprocessor.preprocess()

config_list = ["config_1.json", "../configs/config_2.json"]
preprocessor.preprocess_multi(config_list)
```

### Configs
Config.json should be defined as follows:
```json
{
  "data_path": "Data/",
  "compress": true,
  "crs": "EPSG:4326",
  "data_dir": "GeoJson",
  "regions_dir": "Countries",
  "out_dir": "LayeredGSON",
  "regions_file_map":  {
    "Sri Lanka": "gadm41_LKA_1.json",
    "USA": "gadm41_USA_1.json",
    "China": "gadm41_CHN_1.json",
    "Brazil": "gadm41_BRA_1.json"
  },
  "selected_regions": ["Sri Lanka"],
  "join_on": "NAME_1",
  "joins": {
    "precipitationCal": ["mean", "min", "max"]
  },
  "file_extension": "*.pkl",
  "compress_extension": "*.geojson"
}
```

* data_path is the path to the data directory, data_dir, regions_dir, and out_dir are the subdirectories of data_path that contain the satellite data, location data, and ouput data respectively.
* compress should be set to true to pickle all geojson files inside data_dir. This will significantly improve runtime across future runs.
* crs must be a geopandas supported crs label.
* regions_file_map is a mapping of region name to their file name in regions_dir.
* selected_regions is the list of regions that will be used in the preprocessing.
* join_on is the feature that the duplicate data will be aggregated on.
* joins is the aggregate metrics that will be stored in the aggregate row. Each column will be named as the concatenation of the aggregate function and the original feature. A list must be defined for all columns that should be kept.
* file_extension is format of all data being layered. This can be either *.pkl or *.json.
* config_extension is the format of all data being compressed. This can be .geojson or .json