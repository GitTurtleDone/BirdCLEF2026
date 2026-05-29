import pytest
import nbimporter
from perch_v2_combined_cnn_ssm_transformer.ipynb import get_site_n_hour

def test_get_site_n_hour():
    site, hour = get_site_n_hour("BC2026_Train_0001_S08_20250606_030007.ogg")
    assert site == "S08"
    assert hour == 3
