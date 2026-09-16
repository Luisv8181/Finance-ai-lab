import math

import pandas as pd
import pytest

from market_watcher.market_data import moving_average, period_return_pct


def test_period_return_pct() -> None:
    close = pd.Series([100.0, 102.0, 105.0, 110.0])
    assert period_return_pct(close, 1) == pytest.approx((110 / 105 - 1) * 100)
    assert period_return_pct(close, 3) == pytest.approx(10.0)


def test_period_return_requires_history() -> None:
    close = pd.Series([100.0, 101.0])
    assert math.isnan(period_return_pct(close, 5))


def test_moving_average() -> None:
    close = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
    assert moving_average(close, 3) == pytest.approx(4.0)


def test_moving_average_requires_history() -> None:
    close = pd.Series([1.0, 2.0])
    assert math.isnan(moving_average(close, 3))


def test_invalid_windows() -> None:
    close = pd.Series([1.0, 2.0])
    with pytest.raises(ValueError):
        period_return_pct(close, 0)
    with pytest.raises(ValueError):
        moving_average(close, 0)
