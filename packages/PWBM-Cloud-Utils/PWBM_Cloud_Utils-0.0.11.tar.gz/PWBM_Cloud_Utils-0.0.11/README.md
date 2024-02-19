# PWBM_Cloud_Utils

## Introduction
This Python module provides a convenient interface for handling input/output configurations, reading from different sources (local or cloud), and writing data to cloud storage (Amazon S3) or locally. It is designed to be flexible, supporting various data formats and compression options.

## Installation
To use this module, ensure that you have the required dependencies installed. You can install them using the following command:
```bash
pip install PWBM_Cloud_Utils
```
## Loacl Environment Setup

To configure the environment, create an instance of `IO_Config` by providing the path to your environment file (`.env`), which should contain the necessary configuration variables. If no environment file is provided, default values will be used.

```bash
from dotenv import load_dotenv
from io_util import IO_Config

# Load environment variables from .env file
load_dotenv(".env")

# Create config
config = IO_Config(".env")
```

# PWBM_Utils Module Instructions

To integrate the `PWBM_Utils` module into your project, follow these steps:
```markdown

## Step 1: Update main.py

In your `main.py` file (located in the root directory of your project), add the following `_parse_args()` function:

```python
import argparse

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--id", help="Id of a task in the database", type=int, required=False
    )
    return parser.parse_args()
```

## Step 2: Import CloudUtils Functions

Import several functions from `CloudUtils` for reading, writing, and loading parameters:

```python
# Read and Write functions
from PWBM_Cloud_Utils.io_config import IO_Config
from PWBM_Cloud_Utils.io_reader import IO_Reader
from PWBM_Cloud_Utils.io_reader import IO_Writer

# Load parameters from UI
from PWBM_Cloud_Utils.load_parameter import get_runtime, input_config, save_output
```

## Step 3: Define Main Function

Define a `main()` function in your `main.py` file to handle different execution environments (cloud or local):

```python
import json
from pathlib import Path
from PWBM_Cloud_Utils import utils

def main():
    args = _parse_args()

    if args.id is not None:
        # Cloud version code
        path = # the path to load secrets credential
        file_path = Path(path)
        config = IO_Config(path=file_path)

        # Load data from the database
        ID = args.id
        RUN = get_runtime(args.id)
        NAME = RUN["name"]
        RUNTIME_OPTIONS = json.loads(RUN["runtime_configuration"])
        CONFIG_OF_FILES = input_config(RUNTIME_OPTIONS["stacking_order"])
        (
            scenarios,
            run_stacked_estimates,
            years,
            mtr_vars,
            olg_inputs,
            dist_years,
            numba_mode,
            sample_rate,
            batch_size,
        ) = utils.parse_runtime_options_api(RUNTIME_OPTIONS)

        # Output data to S3
        print(save_output(ID, NAME))

    else:
        # Local version code
        path = "C:\\Users\\yunyej\\Documents\\GitHub\\PWBM_Cloud_Utils\\src\\PWBM_Cloud_Utils\\.env"  # the path to your secrets credential
        file_path = Path(path)
        config = IO_Config(path=file_path)

        # Load local parameters
        config_path = "../config/counterfactuals/debug/test"
        rto = utils.parse_runtime_options(config_path)
        (
            scenarios,
            run_stacked_estimates,
            years,
            mtr_vars,
            olg_inputs,
            dist_years,
            numba_mode,
            sample_rate,
            batch_size,
            run_baseline,
        ) = rto

# Your code follows the main function.
```

# Usage
## Reading Data
The IO_Reader class allows you to read data from either cloud storage (Amazon S3) or a local file, depending on the configuration.

```bash
from io_util import IO_Reader

## Create reader instance
reader = IO_Reader(config)

## Read data as bytes
data_bytes = reader.read("bucket_name", "path/to/file", compress=True)

## Read data as a string
data_string = reader.read_string("bucket_name", "path/to/text_file", compress=False)
```

## Writing Data

The IO_Writer class enables you to write data to cloud storage (Amazon S3) or a local file.

```bash
from io_util import IO_Writer

## Create writer instance

writer = IO_Writer(config)

## Write data to cloud storage
success = writer.write("bucket_name", "path/to/output/file", "data_to_write", compress=True, cache=False)

# Check if an object exists in cloud storage
exists = writer.object_exists("path/to/file", "recipe")
```

Feel free to adjust the paths and configurations according to your project structure.


# Notes
Ensure that your environment file (.env) contains the necessary variables, such as Region_Name, AWS_ACCESS_KEY_ID, and AWS_ACCESS_KEY_SECRET.
Compression options (compress) are available for both reading and writing, allowing you to handle compressed data.
The module uses the boto3 library for Amazon S3 interactions.
