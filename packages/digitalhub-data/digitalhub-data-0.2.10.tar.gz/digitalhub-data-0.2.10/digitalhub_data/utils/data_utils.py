from __future__ import annotations

import json
import numpy as np
import pandas as pd


def get_data_preview(columns: list, data: list[list]) -> list[dict]:
    """
    Prepare preview.

    Parameters
    ----------
    columns : list
        Columns.
    data : list[list]
        Data.

    Returns
    -------
    list[dict]
        Data preview.
    """
    # transposed = transpose_data(data)
    df = pd.DataFrame(data, columns=columns)
    masked = mask_data(df)
    columns_to_filter = find_memoryview(masked)
    filtered_data = masked[columns_to_filter]
    preview = prepare_preview(filtered_data)
    return check_preview_size(preview)


def mask_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Mask data.

    Parameters
    ----------
    data : pd.DataFrame
        Data.

    Returns
    -------
    pd.DataFrame
        Masked data.
    """
    # Filter nan
    data = data.replace({np.nan: None})
    return data


def find_memoryview(data: pd.DataFrame) -> list[str]:
    """
    Find memoryview values.

    Parameters
    ----------
    data : pd.DataFrame
        Data.

    Returns
    -------
    list[str]
        Column to filter out from preview.
    """
    return [col for col in data.columns if not any(isinstance(val, memoryview) for val in data[col])]


def filter_data(data: pd.DataFrame, columns: list, columns_idx: list[int]) -> tuple[list, pd.DataFrame]:
    """
    Filter data.

    Parameters
    ----------
    data : pd.DataFrame
        Data.
    columns : list
        Columns.
    columns_idx : list[int]
        Column indexes to filter.

    Returns
    -------
    tuple[list, pd.DataFrame]
        Filtered columns and data.
    """
    return [columns[idx] for idx in columns_idx], pd.DataFrame([data[idx] for idx in columns_idx])


def prepare_preview(data: pd.DataFrame) -> list[dict]:
    """
    Get preview.

    Parameters
    ----------
    data : pd.DataFrame
        Data.

    Returns
    -------
    list[dict]
        Preview.
    """
    return [{"name": k, "value": v} for k, v in data.to_dict(orient="list").items()]


def check_preview_size(preview: list[dict]) -> list:
    """
    Check preview size. If it's too big, return empty list.

    Parameters
    ----------
    preview : list[dict]
        Preview.

    Returns
    -------
    list
        Preview.
    """
    if len(json.dumps(preview).encode("utf-8")) >= 64000:
        return []
    return preview
