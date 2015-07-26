import pandas as pd
import numpy as np

def retrieve_test(filename, var_threshold=20):
    android_data = pd.read_csv("test_resources/%s" %filename, delimiter=" ", header=None)
    android_data.columns = ["heading", "steps", "time"]
    android_data["round_time"] = (np.round(android_data["time"]/500, 0)*500).astype(np.int64)
    android_data["step_diff"] = android_data["steps"].diff()
    heading_bin_var = android_data.groupby("round_time")["heading"].var()
    heading_bin_mean = android_data.groupby("round_time")["heading"].mean()
    step_bin_max = android_data.groupby("round_time")["step_diff"].sum()
    step_bin_max.name = "steps"
    heading_bin_mean.name = "heading_mean"
    heading_bin_var.name = "heading_var"

    rounded_df = pd.concat([heading_bin_var, heading_bin_mean, step_bin_max], 1)
    rounded_df["turn"] = rounded_df["heading_var"] > var_threshold
    rounded_df["cum_turn"] = rounded_df["turn"].cumsum()
    grouped = rounded_df.groupby("cum_turn")
    headings = grouped["heading_mean"].median()
    start_step = grouped["steps"].min()
    end_step = grouped["steps"].max()
    steps = grouped["steps"].sum()

    instructions = pd.concat([headings, steps], 1)
    instructions.columns=["heading", "steps"]
    instructions["height"] = 0.0
    instructions["heading"] = np.deg2rad(instructions["heading"])
    return instructions.as_matrix(["steps", "heading", "height"])
