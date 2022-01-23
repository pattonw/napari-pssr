from napari_pssr import (
    train_pssr_widget,
    predict_pssr_widget,
)
import numpy as np


def test_train_pssr_widget(make_napari_viewer, capsys):
    viewer = make_napari_viewer()
    layer = viewer.add_image(np.random.random((100, 100)))

    my_widget = train_pssr_widget()

    my_widget(viewer.layers[0])


def test_predict_pssr_widget(make_napari_viewer, capsys):
    viewer = make_napari_viewer()
    layer = viewer.add_image(np.random.random((100, 100)))

    my_widget = predict_pssr_widget()

    my_widget(viewer.layers[0])
