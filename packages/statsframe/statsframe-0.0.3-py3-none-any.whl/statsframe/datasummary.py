from __future__ import annotations

# Main sf.imports ----
import pandas as pd
import polars as pl
import polars.selectors as cs
from great_tables import GT

from ._tbl_data import DataFrameLike  # , SeriesLike

cat_cols = []


def correlation_frame(
    data: DataFrameLike,
    method: str = "pearson",
    output: str = "polars",
    float_precision: int = 2,
    title: str = "Correlation Matrix",
    notes: str = None,
    align: str = "r",
    color_palette: str = None,
    na_color: str = None,
):
    """
    Generates a correlation matrix based on the given data.

    Args:
        data: The input data to compute the correlation matrix on.
        method: The method used to compute the correlation matrix.
        Supported methods are "pearson", "kendall", and "spearman".
        output: The output format of the correlation matrix.
        Supported formats are "polars", "markdown", "simple", and "gt".
        float_precision: The number of decimal places to round the correlation
        values to.
        title: The title of the correlation matrix.
        notes: Additional notes or comments to include in the correlation matrix.
        align: The alignment of the table cells.
        Supported alignments are "r" (right), "l" (left), and "c" (center).
        color_palette: The color palette to use for formatting the correlation
        matrix when output is "gt".
        na_color: The color to use for representing missing values in the
        correlation matrix when output is "gt".

    Returns:
        The correlation matrix as a DataFrameLike object.

    Raises:
        ValueError: If an unsupported method or output format is specified.

    """
    ...

    data = convert_to_polars(data).select(cs.numeric())
    if method == "pearson":
        corr_tab = data.corr()
        var_list = corr_tab.columns
        corr_tab = corr_tab.with_columns(var=pl.Series(corr_tab.columns)).select(
            ["var"] + var_list
        )
    elif method == "kendall":
        corr_tab, var_list = _use_pandas_corr(data, "kendall")
    elif method == "spearman":
        corr_tab, var_list = _use_pandas_corr(data, "spearman")
    else:
        raise ValueError("Supported methods are pearson, spearman, kendall correlation")

    align_dict = {"r": "RIGHT", "l": "LEFT", "c": "CENTER"}
    tbl_align = align_dict[align]

    if output in {"polars", "markdown", "simple"}:
        format_dict = {"polars": None, "markdown": "ASCII_MARKDOWN", "simple": "NOTHING"}
        tbl_formatting = format_dict[output]
        shape_details = f"Rows: {data.height}, Columns: {data.width}"

        with pl.Config(
            float_precision=float_precision,
            tbl_formatting=tbl_formatting,
            tbl_cell_alignment=tbl_align,
            tbl_hide_column_names=False,
            tbl_hide_column_data_types=True,
            tbl_hide_dataframe_shape=True,
        ):
            print(f"{title}")
            print(f"{shape_details}")
            print(corr_tab)
    elif output == "gt":
        if color_palette is None:
            color_palette = [
                "#636363",
                "#bdbdbd",
                "#f0f0f0",
                "#ffffff",
                "#f0f0f0",
                "#bdbdbd",
                "#636363",
            ]
        if na_color is None:
            na_color = "#ffffff"

        (
            GT(corr_tab)
            .data_color(
                domain=[-1, 1],
                palette=color_palette,
                na_color=na_color,
            )
            .fmt_number(columns=var_list, decimals=float_precision)
            .cols_align(align=tbl_align.lower())
            .tab_header(title=title)
            .tab_source_note(source_note=f"{notes}")
        )
    else:
        raise ValueError("Supported outputs are polars, markdown, simple, and gt")

    return corr_tab


def _use_pandas_corr(data, method):
    result = data.to_pandas().corr(method=method).pipe(pl.from_pandas)
    var_list = result.columns
    result = result.with_columns(var=pl.Series(result.columns)).select(["var"] + var_list)
    return result, var_list


def skim_frame(
    data: pl.DataFrame,
    type: str = "numeric",
    stats: str = "simple",
    output: str = "polars",
    float_precision: int = 1,
    histogram: bool = False,
    title: str = "Summary Statistics",
    notes: str = None,
    align: str = "r",
) -> pl.DataFrame:
    """
    Summary Statistics.

    Generates summary statistics for a given DataFrame.

    Args:
        data (DataFrameLike): The input DataFrame. Can be pandas or polars.
        type (str, optional): The type of summary statistics to generate.
            Defaults to "numeric".
        output (str, optional): The output format for the summary statistics.
            Defaults to None.
        stats (str, optional): The summary statistics to return. Defaults to "simple".
        float_precision (int, optional): The number of decimal places to round
            float values when formatting in table output.
            Defaults to 2.
        histogram (bool, optional): Whether to include a histogram in the output.
            Defaults to False.
        title (str, optional): The title of the summary statistics table.
            Defaults to "Summary Statistics".
        notes (str, optional): Additional notes or comments.
            Defaults to None.
        align (str, optional): The alignment of the table columns.
            Defaults to "r".

    Returns:
        pl.DataFrame: The summary statistics table.

    Examples:
        # Generate summary statistics for a numeric DataFrame
        summary = skim_frame(data)

        # Generate summary statistics for a categorical DataFrame
        summary = skim_frame(data, type="categorical")

        # Generate summary statistics in markdown format
        summary = skim_frame(data, output="markdown")

    """

    # methods depend on the data being a polars DataFrame
    data = convert_to_polars(data)

    # check if the data is numeric or categorical
    if type == "numeric":
        stats_tab, float_cols = _skim_numeric(data, stats=stats)
    elif type == "categorical":
        stats_tab, float_cols = _skim_categorical(data, stats=stats)
    else:
        raise ValueError("Invalid type argument")

    align_dict = {"r": "RIGHT", "l": "LEFT", "c": "CENTER"}
    tbl_align = align_dict[align]

    if output in {"polars", "markdown", "simple"}:
        format_dict = {"polars": None, "markdown": "ASCII_MARKDOWN", "simple": "NOTHING"}
        tbl_formatting = format_dict[output]
        shape_details = f"Rows: {data.height}, Columns: {data.width}"

        with pl.Config(
            float_precision=float_precision,
            tbl_formatting=tbl_formatting,
            tbl_cell_alignment=tbl_align,
            tbl_hide_column_names=False,
            tbl_hide_column_data_types=True,
            tbl_hide_dataframe_shape=True,
        ):
            print(f"{title}")
            print(f"{shape_details}")
            print(stats_tab)
    elif output == "gt":
        (
            GT(stats_tab)
            .fmt_number(columns=float_cols, decimals=float_precision)
            .cols_align(align=tbl_align.lower())
            .tab_header(
                title=title,
                subtitle=f"Rows: {data.height}, Columns: {data.width}",
            )
            .tab_source_note(source_note=f"{notes}")
        )
    else:
        raise ValueError("Supported outputs are polars, markdown, simple, and gt")

    return stats_tab


def _skim_numeric(data: pl.DataFrame, stats: str = "simple") -> pl.DataFrame:
    """
    Generates summary statistics for a numeric datatypes in a DataFrame.

    Args:
        data (pl.DataFrame): The input DataFrame.
        stats (str, optional): The summary statistics to return. Defaults to "simple".

    Returns:
        pl.DataFrame: The summary statistics table.

    """
    stats_dict = {
        "simple": ["Missing (%)", "Mean", "SD", "Min", "Median", "Max"],
        "moments": ["Mean", "Variance", "Skewness", "Kurtosis"],
        "detail": [
            "Missing (%)",
            "Mean",
            "SD",
            "Min",
            "Median",
            "Max",
            "Skewness",
            "Kurtosis",
        ],
    }

    float_cols = stats_dict[stats]
    int_cols = ["Unique (#)"]
    stats_cols = int_cols + float_cols

    if stats == "simple":
        stats_tab = (
            data.select(cs.numeric().n_unique())
            .cast(pl.Float64, strict=True)
            .extend(
                data.select(
                    cs.numeric()
                    .null_count()
                    .truediv(data.height)
                    .cast(pl.Float64, strict=True)
                )
            )
            .extend(data.select(cs.numeric().mean()))
            .extend(data.select(cs.numeric().std()))
            .extend(data.select(cs.numeric().min().cast(pl.Float64, strict=True)))
            .extend(data.select(cs.numeric().median()))
            .extend(data.select(cs.numeric().max().cast(pl.Float64, strict=True)))
            .transpose(include_header=True, header_name="", column_names=stats_cols)
            .with_columns(pl.col("Unique (#)").cast(pl.Int64, strict=True))
        )
    elif stats == "moments":
        stats_tab = (
            data.select(cs.numeric().n_unique())
            .cast(pl.Float64, strict=True)
            .extend(data.select(cs.numeric().mean()))
            .extend(data.select(cs.numeric().std()))
            .extend(data.select(cs.numeric().skew()))
            .extend(data.select(cs.numeric().kurtosis()))
            .transpose(include_header=True, header_name="", column_names=stats_cols)
            .with_columns(pl.col("Unique (#)").cast(pl.Int64, strict=True))
        )
    elif stats == "detail":
        stats_tab = (
            data.select(cs.numeric().n_unique())
            .cast(pl.Float64, strict=True)
            .extend(
                data.select(
                    cs.numeric()
                    .null_count()
                    .truediv(data.height)
                    .cast(pl.Float64, strict=True)
                )
            )
            .extend(data.select(cs.numeric().mean()))
            .extend(data.select(cs.numeric().std()))
            .extend(data.select(cs.numeric().min().cast(pl.Float64, strict=True)))
            .extend(data.select(cs.numeric().median()))
            .extend(data.select(cs.numeric().max().cast(pl.Float64, strict=True)))
            .extend(data.select(cs.numeric().skew()))
            .extend(data.select(cs.numeric().kurtosis()))
            .transpose(include_header=True, header_name="", column_names=stats_cols)
            .with_columns(pl.col("Unique (#)").cast(pl.Int64, strict=True))
        )
    else:
        raise ValueError("Invalid stats argument")
    return stats_tab, float_cols


def _skim_categorical(data: pl.DataFrame, stats: str = "simple") -> pl.DataFrame:
    """
    Generates summary statistics for a numeric datatypes in a DataFrame.

    Args:
        data (pl.DataFrame): The input DataFrame.
        stats (str, optional): The summary statistics to return. Defaults to "simple".

    Returns:
        pl.DataFrame: The summary statistics table.

    """
    raise NotImplementedError("Not implemented")


def convert_to_polars(data: DataFrameLike) -> pl.DataFrame:
    """
    Converts a DataFrame-like object to a polars DataFrame.

    Args:
        data (DataFrameLike): The input DataFrame-like (pandas or polars DataFrame`)
            object.

    Returns:
        pl.DataFrame: The converted polars DataFrame.

    Raises:
        ValueError: If the input data is not a polars or pandas DataFrame.

    """
    if isinstance(data, pl.DataFrame):
        return data
    elif isinstance(data, pd.DataFrame):
        return pl.from_pandas(data)
    else:
        raise ValueError("Input data must be a polars or pandas DataFrame")
