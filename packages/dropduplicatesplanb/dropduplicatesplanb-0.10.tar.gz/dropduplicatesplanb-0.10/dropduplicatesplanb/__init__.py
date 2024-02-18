import operator
import functools
import pandas as pd
import numpy as np
from arrayhascher import get_hash_column
from pandas.core.frame import DataFrame


def drop_duplis(df, *args, **kwargs):
    r"""
    Function to drop duplicate rows from a DataFrame, with the option to specify columns for identifying duplicates.
    Parameters:
        df: pandas DataFrame
        *args: variable length argument list
        **kwargs: keyword arguments
    Returns:
        pandas DataFrame without duplicate rows
    """
    inpl = kwargs.get("inplace", False)
    if inpl:
        raise NotImplementedError("inplace not implemented")
    subsu = kwargs.get("subset", df.columns.to_list())
    kwargs["subset"] = "__XXXX___DELETE____"
    df3 = df[subsu].map(repr)
    if isinstance(df3, pd.DataFrame):
        df["__XXXX___DELETE____0"] = functools.reduce(
            lambda a, b: operator.add(a, df3[b]), df3.columns
        ).__array__()
    else:
        df["__XXXX___DELETE____0"] = df3.__array__()
    return (
        df.assign(
            __XXXX___DELETE____=get_hash_column(
                np.ascontiguousarray(
                    df["__XXXX___DELETE____0"]
                    .__array__()
                    .astype("U")
                    .view(np.uint32)
                    .reshape((len(df), -1))
                ),
                fail_convert_to_string=True,
                whole_result=False,
            )
        )
        .drop_duplicates(**kwargs)
        .drop(columns=["__XXXX___DELETE____", "__XXXX___DELETE____0"])
    )


def pd_add_drop_duplicates_planB():
    DataFrame.d_drop_duplicates_planB = drop_duplis
