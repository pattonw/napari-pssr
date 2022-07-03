import bioimageio.core

import torch

from pathlib import Path


model_file = "scripts/baseline_pssr_512_torch.model"
model = torch.load(model_file)

print(model)
raise Exception()

RDF = None

# get architecture source
def get_architecture_source():
    raw_resource = bioimageio.core.load_raw_resource_description(RDF)
    model_source = raw_resource.weights["pytorch_state_dict"].architecture
    # download the source file if necessary
    source_file = bioimageio.core.resource_io.utils.resolve_source(
        model_source.source_file
    )
    # if the source file path does not exist, try combining it with the root path of the model
    if not Path(source_file).exists():
        source_file = Path(
            raw_resource.root_path,
            Path(source_file).relative_to(Path(".").absolute()),
        )
    assert Path(source_file).exists(), source_file
    class_name = model_source.callable_name
    return f"{source_file}:{class_name}"


# the path to save the new model with torchscript weights
zip_path = Path("PSSR_8nm_er.zip")
assert zip_path.name.endswith(".zip"), "Must save model in a zip"

preprocessing = [
    [{"name": prep.name, "kwargs": prep.kwargs} for prep in inp.preprocessing]
    for inp in None.inputs
    if inp.preprocessing != missing
]
postprocessing = [
    [
        {"name": post.name, "kwargs": post.kwargs}
        for post in outp.postprocessing
    ]
    if outp.postprocessing != missing
    else None
    for outp in None.outputs
]
citations = [
    {k: v for k, v in dataclasses.asdict(citation).items() if v != missing}
    for citation in None.cite
]
authors = [dataclasses.asdict(author) for author in None.authors]
if (
    self.save_widget.author.value is not None
    and len(self.save_widget.author.value) > 0
):
    authors += [{"name": self.save_widget.author.value}]
name = (
    self.save_widget.model_name.value
    if self.save_widget.model_name.value is not None
    and len(self.save_widget.model_name.value) > 0
    else None.name
)

kwargs = {
    "weight_uri": None.weights["pytorch_state_dict"].source,
    "test_inputs": None.test_inputs,
    "test_outputs": None.test_outputs,
    "input_axes": ["".join(inp.axes) for inp in None.inputs],
    "input_min_shape": [inp.shape.min for inp in None.inputs],
    "input_step": [inp.shape.step for inp in None.inputs],
    "output_axes": ["".join(outp.axes) for outp in None.outputs],
    "output_path": zip_path,
    "name": name,
    "description": f"{None.description}\nFinetuned with the napari-affinities plugin!",
    "authors": authors,
    "license": None.license,
    "documentation": None.documentation,
    "covers": None.covers,
    "tags": None.tags,
    "cite": citations,
    "parent": None.parent,
    "architecture": get_architecture_source(),
    "model_kwargs": None.weights["pytorch_state_dict"].kwargs,
    "preprocessing": preprocessing,
    "postprocessing": postprocessing,
    "training_data": None.training_data
    if None.training_data != missing
    else None,
    "config": None.config,
}

# build the model! it will be saved to 'zip_path'
new_model_raw = build_model(**kwargs)
