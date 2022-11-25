def test_open(make_napari_viewer):
    viewer = make_napari_viewer()
    viewer.open_sample(plugin="napari-pssr", sample="lr_em_small")
    viewer.open_sample(plugin="napari-pssr", sample="hr_em_small")
    viewer.open_sample(plugin="napari-pssr", sample="lr_em_large")
