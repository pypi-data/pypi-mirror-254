# statsframe

![PyPI - Version](https://img.shields.io/pypi/v/statsframe.svg) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/statsframe)
[![License](https://img.shields.io/github/license/NKeleher/statsframe)](https://img.shields.io/github/license/NKeleher/statsframe)
[![Repo Status](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

---

**Customizable data and model summaries in Python.**

`statsframe` creates tables that provide descriptive statistics of
numeric and categorical data.

The goal is to provide a simple -- yet customizable -- way to summarize
data and models in Python.

`statsframe` is heavily inspired by [`modelsummary`](https://modelsummary.com/)
in R. The goal is not to replicate all that `modelsummary` does, but to provide
a way of achieving similar results in Python.

In order to achieve this, `statsframe` builds on the [`polars`](https://docs.pola.rs/)
library to produce tables that can be easily customized and exported to other formats.

## Basic Usage

As an example of `statsframe` usage, the `skim_frame` function provides a
summary of a DataFrame (either `polars.DataFrame` or `pandas.DataFrame`).
The default summary statistics returned by `statsframe.skim_frame()` are unique values,
percentage missing, mean, standard deviation, minimum, median, and maximum.

Where possible, `statsframe` will print a table to the console and return a
polars DataFrame with the summary statistics. This allows for easy customization.
For example, the `polars.DataFrame` with statistics from `statsframe` can be
modified using the
[`Great Tables`](https://posit-dev.github.io/great-tables/reference/) package.

```python
import polars as pl
import statsframe as sf

df = (
        pl.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv")
          .drop("rownames")
    )

stats = sf.skim_frame(df)

Summary Statistics
Rows: 32, Columns: 11
┌──────┬────────────┬─────────────┬───────┬───────┬──────┬────────┬───────┐
│      ┆ Unique (#) ┆ Missing (%) ┆  Mean ┆    SD ┆  Min ┆ Median ┆   Max │
╞══════╪════════════╪═════════════╪═══════╪═══════╪══════╪════════╪═══════╡
│  mpg ┆         25 ┆         0.0 ┆  20.1 ┆   6.0 ┆ 10.4 ┆   19.2 ┆  33.9 │
│  cyl ┆          3 ┆         0.0 ┆   6.2 ┆   1.8 ┆  4.0 ┆    6.0 ┆   8.0 │
│ disp ┆         27 ┆         0.0 ┆ 230.7 ┆ 123.9 ┆ 71.1 ┆  196.3 ┆ 472.0 │
│   hp ┆         22 ┆         0.0 ┆ 146.7 ┆  68.6 ┆ 52.0 ┆  123.0 ┆ 335.0 │
│ drat ┆         22 ┆         0.0 ┆   3.6 ┆   0.5 ┆  2.8 ┆    3.7 ┆   4.9 │
│   wt ┆         29 ┆         0.0 ┆   3.2 ┆   1.0 ┆  1.5 ┆    3.3 ┆   5.4 │
│ qsec ┆         30 ┆         0.0 ┆  17.8 ┆   1.8 ┆ 14.5 ┆   17.7 ┆  22.9 │
│   vs ┆          2 ┆         0.0 ┆   0.4 ┆   0.5 ┆  0.0 ┆    0.0 ┆   1.0 │
│   am ┆          2 ┆         0.0 ┆   0.4 ┆   0.5 ┆  0.0 ┆    0.0 ┆   1.0 │
│ gear ┆          3 ┆         0.0 ┆   3.7 ┆   0.7 ┆  3.0 ┆    4.0 ┆   5.0 │
│ carb ┆          6 ┆         0.0 ┆   2.8 ┆   1.6 ┆  1.0 ┆    2.0 ┆   8.0 │
└──────┴────────────┴─────────────┴───────┴───────┴──────┴────────┴───────┘
```

We can achieve the same result above with a pandas DataFrame.

```python
import pandas as pd
import statsframe as sf

trees_df = pd.read_csv(
    "https://vincentarelbundock.github.io/Rdatasets/csv/datasets/trees.csv"
).drop(columns=["rownames"])

trees_stats = sf.skim_frame(trees_df)

Summary Statistics
Rows: 31, Columns: 3
┌────────┬────────────┬─────────────┬──────┬──────┬──────┬────────┬──────┐
│        ┆ Unique (#) ┆ Missing (%) ┆ Mean ┆   SD ┆  Min ┆ Median ┆  Max │
╞════════╪════════════╪═════════════╪══════╪══════╪══════╪════════╪══════╡
│  Girth ┆         27 ┆         0.0 ┆ 13.2 ┆  3.1 ┆  8.3 ┆   12.9 ┆ 20.6 │
│ Height ┆         21 ┆         0.0 ┆ 76.0 ┆  6.4 ┆ 63.0 ┆   76.0 ┆ 87.0 │
│ Volume ┆         30 ┆         0.0 ┆ 30.2 ┆ 16.4 ┆ 10.2 ┆   24.2 ┆ 77.0 │
└────────┴────────────┴─────────────┴──────┴──────┴──────┴────────┴──────┘

```

## Contributing

If you encounter a bug, have usage questions, or want to share ideas to make
the `statsframe` package more useful, please feel free to file an
[issue](https://github.com/NKeleher/statsframe/issues).

## Code of Conduct

Please note that the **statsframe** project is released with a
[contributor code of conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

By participating in this project you agree to abide by its terms.

## License

**statsframe** is licensed under the MIT license.

## Governance

This project is primarily maintained by [Niall Keleher](https://twitter.com/nkeleher).
Contributions from other authors is welcome.
