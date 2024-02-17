import os
import json
import pickle
from typing import List

import xarray
import numpy as np

import pandas as pd
import geopandas as gpd

from tqdm import tqdm
from pathlib import Path


def load_from_pickle(path, crs):
    p_df = pd.read_pickle(path)
    return gpd.GeoDataFrame(p_df, geometry=p_df["geometry"], crs=crs)


class Preprocessor:
    def __init__(self, config_file: str, verbose = True, **kwargs):
        r"""
        :param config_file: The path to the config.json file. See the official PyPI docs for more information.
        :param verbose: enable step logging
        :key record_out: An optional function to generate a value from a file name.
        :key region_out: An optional function to generate a value from a region's file name
        :key out_out: An optional function that returns a label to be appended to the end of an output file name.
        :returns: A preprocessor instance
        """
        super().__init__()

        self.config_file = config_file
        self.verbose = verbose
        self.record_out = kwargs.get("record_out", lambda x: '')
        self.region_out = kwargs.get("region_out", lambda x: '')
        self.out_out = kwargs.get("out_out", lambda : '')
        self.load_config(config_file)

    def log(self, m):
        if self.verbose: print(m)

    def load_config(self, c_f):
        self.log(f"Loading Config {c_f}")
        with open(c_f) as f:
            config = json.load(f)
            self.PATH_OF = lambda x: config["data_path"] + x
            self.COMPRESS_FILES = config["compress"]
            self.CRS = config["crs"]
            self.DATA_DIR = config["data_dir"]
            self.COUNTRIES_DIR = config["regions_dir"]
            self.OUT_DIR = config["out_dir"]
            self.REGIONS = config["regions_file_map"]
            self.SELECTED_REGIONS = config["selected_regions"]
            self.JOIN_ON = config["join_on"]
            self.JOINS = config["joins"]
            self.EXTENSION = config["file_extension"]
            self.COMPRESS_EXTENSION = config["compress_extension"]

    def load_all_regions(self):
        return {r: gpd.read_file(self.PATH_OF(f"{self.COUNTRIES_DIR}/{self.REGIONS[r]}")) for r in self.SELECTED_REGIONS}

    def initialize_dirs(self):
        for d in ["", self.DATA_DIR, self.OUT_DIR, "Countries"]:
            if not os.path.exists(self.PATH_OF(d)):
                os.mkdir(self.PATH_OF(d))

    def pickle_all_in_dir(self, path_to_dir):
        self.log(f"Compressing GeoJsons in {path_to_dir}")
        for f in tqdm(Path(path_to_dir).glob(self.COMPRESS_EXTENSION)):
            out_path = self.PATH_OF(f"{self.DATA_DIR}/{'.'.join(str(f).split('.')[:-1])[len(path_to_dir):]}.pkl")
            if not Path(out_path).is_file():
                gdf = gpd.read_file(f, engine='pyogrio', use_arrow=True)
                gdf.to_pickle(out_path)

    def get_all_from_dir(self, path_to_dir, extension):
        for f in Path(path_to_dir).glob(extension):
            match extension:
                case "*.pkl":
                    yield f, load_from_pickle(f, self.CRS)
                case "*.json":
                    yield f, gpd.read_file(f, engine='pyogrio', use_arrow=True)
                case _:
                    raise ValueError("Unsupported File Extension")

    def permute_and_layer(self, path_to_dir, extension, regions):
        self.log(f"Joining and Concatenating GeoJsons")
        out = {}
        for f, gdf in tqdm(self.get_all_from_dir(path_to_dir, extension)):
            for r, rdf in regions.items():
                gdf.to_crs(rdf.crs)
                joined = gpd.sjoin(rdf, gdf, how="left", predicate="intersects")
                aggregate = joined.dissolve(by=self.JOIN_ON, aggfunc=self.JOINS)
                aggregate.columns = [''.join([s[1], s[0].title()]) if type(s) == tuple else s for s in
                                     aggregate.columns]
                aggregate.to_pickle(
                    self.PATH_OF(f"{self.OUT_DIR}/{r}_{self.region_out(self.REGIONS[r])}_{self.record_out(f)}.pkl")
                )

                if r not in out:
                    out[r] = [aggregate.drop("geometry", axis=1)]
                else:
                    out[r].append(aggregate.drop("geometry", axis=1))

        for r, rdf in out.items():
            rdf = xarray.DataArray([rdf]).to_numpy()
            np.save(self.PATH_OF(f"{self.OUT_DIR}/{r}_time_series_{self.DATA_DIR}_{self.out_out()}.npy"), rdf)
            with open(self.PATH_OF(f"{self.OUT_DIR}/{r}_time_series_{self.DATA_DIR}_{self.out_out()}.pkl"), 'wb') as f:
                pickle.dump(rdf, f, protocol=-1)

    def preprocess(self):
        self.initialize_dirs()
        if self.COMPRESS_FILES: self.pickle_all_in_dir(self.PATH_OF(self.DATA_DIR))
        self.permute_and_layer(self.PATH_OF(self.DATA_DIR), self.EXTENSION, self.load_all_regions())

    def preprocess_multi(self, config_list: List[str]):
        """
        :param config_list: A list of config file names
        """
        for c_f in config_list:
            self.load_config(c_f)
            self.preprocess()