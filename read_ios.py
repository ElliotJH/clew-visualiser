import json

import pandas as pd
import numpy as np

def retrieve_test(test_name):
    with open("test_resources/%s.json" % test_name) as f:
        payload = json.load(f)

    heading_data = pd.DataFrame(payload["compass"])
    heading_data["date"] = pd.to_datetime(heading_data["date"])
    heading_data["heading"] = np.deg2rad(heading_data["heading"].astype(np.float64))
    print heading_data["heading"]
    heading_data = heading_data.set_index("date")
    heading_data["distance"] = 0.1
    heading_data["height"] = 0.0
    print heading_data.columns
    return heading_data.as_matrix(columns=["distance", "heading", "height"])

