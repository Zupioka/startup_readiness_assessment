import pandas as pd
from typing import Dict, List

def load_questions(path="data/questions.csv") -> pd.DataFrame:
    # read IDs as strings so "200" or "BRL-01" both work
    return pd.read_csv(path, dtype=str).fillna("")

def compute_final_levels(history_by_dim: Dict[str, List[int]]) -> Dict[str, int]:
    """
    Final level for a dimension = the last valid (>0) score recorded while branching.
    """
    final = {}
    for dim, vals in history_by_dim.items():
        vals = [int(v) for v in vals if str(v).strip().isdigit() and int(v) > 0]
        if vals:
            final[dim] = int(vals[-1])
    return final
