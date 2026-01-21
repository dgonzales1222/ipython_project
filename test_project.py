import datetime as dt
import pandas as pd
from project import compute_daily_gdd, determine_growing_stage, CropSeason, crops


def test_compute_daily_gdd():
    # Test computed GDD if the average temperature is below the base temperature.
    result = compute_daily_gdd(tmin=5.0, tmax=7.0, t_base=10.0, t_upper=30.0)
    assert result == 0.0
    # Test computed GDD if the average temperature is between thresholds.
    result = compute_daily_gdd(tmin=10.0, tmax=20.0, t_base=10.0, t_upper=30.0)
    assert result == 5.0
    # Test computed GDD if the average temperature is above the upper temperature.
    result = compute_daily_gdd(tmin=40.0, tmax=42.0, t_base=10.0, t_upper=30.0)
    assert result == 20.0
