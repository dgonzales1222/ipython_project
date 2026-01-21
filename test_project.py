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



def test_determine_growing_stage_boundaries():
    # Define representative cumulative GDD thresholds for each crop growth stage.
    stages = {"initial": 100.0, "development": 200.0, "mid_season": 300.0, "harvest": 400.0}

    # Evaluate growth stage and progress at cumulative GDD values spanning all phenological phases.
    stage_init, progress_init = determine_growing_stage(50.0, stages)
    stage_dev, progress_dev = determine_growing_stage(150.0, stages)
    stage_mid, progress_mid = determine_growing_stage(250.0, stages)
    stage_harvest, progress_harvest = determine_growing_stage(350.0, stages)
    stage_post, progress_post = determine_growing_stage(450.0, stages)

    # Assert correct stage labels and ensure progress values remain within valid bounds.

    assert stage_init == "initial"
    assert 0.0 <= progress_init <= 1.0

    assert stage_dev == "development"
    assert 0.0 <= progress_dev <= 1.0

    assert stage_mid == "mid_season"
    assert 0.0 <= progress_mid <= 1.0

    assert stage_harvest == "harvest"
    assert 0.0 <= progress_harvest <= 1.0

    assert stage_post == "post_harvest"
    assert 0.0 <= progress_post <= 1.0