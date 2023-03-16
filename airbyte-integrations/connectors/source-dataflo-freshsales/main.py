#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_dataflo_freshsales import SourceDatafloFreshsales

if __name__ == "__main__":
    source = SourceDatafloFreshsales()
    launch(source, sys.argv[1:])
