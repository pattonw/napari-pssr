from napari_pssr.widgets.pssr import ModelWidget
import numpy as np


def test_train_pssr_widget(make_napari_viewer, capsys, models):
    viewer = make_napari_viewer()
    model_widget = ModelWidget(viewer)
    
    model_widget.load_model(models)
