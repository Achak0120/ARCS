import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from loguru import logger
import os
import datetime
import numpy as np
from pathlib import Path


def clean_data(log_path: str) -> pd.DataFrame:
    df = pd.read_csv(log_path)
    df.to_csv("full_output.csv", index=False)  # Don't assign it back to df
    
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(df)


csv_path = Path(r"C:\Users\Aishik C\Desktop\ARCS\ARCS\src\test_logs\ILCH_Q70_rio_2025-03-29_11-42-10_CSV.csv")
clean_data(csv_path)