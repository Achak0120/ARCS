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


csv_path = Path(__file__).resolve().parents[2] / 'test_logs' / 'ILCH_Q70_rio_2025-03-29_11-42-10_CSV.csv'
clean_data('')