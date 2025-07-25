import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from loguru import logger
import os
import datetime
import numpy as np
from pathlib import Path


def clean_data(log_path: str) -> pd.DataFrame:
    # Read the log
    df = pd.read_csv(log_path)

    # Save full raw
    df.to_csv("full_output.csv", index=False)  # Don't assign it back to df
    
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(df)


def brown_out_detection(df, voltage_col=None, threshold=7.0):
    # Find the voltage column automatically if not provided
    if voltage_col is None:
        for col in df.columns:
            if any(keyword in col.lower() for keyword in ["voltage", "battery"]):
                voltage_col = col
                break
    
    if voltage_col is None:
        print("No voltage-related column found.")
        return

    print(f"Using voltage column: {voltage_col}")

    # Convert to numeric just in case
    voltages = pd.to_numeric(df[voltage_col], errors='coerce')

    for idx, voltage in enumerate(voltages):
        if pd.notna(voltage) and voltage < threshold:
            print(f"Brownout likely at row {idx}: Voltage = {voltage:.2f}V (Threshold = {threshold}V)")

    
    
