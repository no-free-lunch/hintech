from typing import Any

from kedro.pipeline import Pipeline, node

from hintech.pipelines.data_engineering.nodes import preprocess_train


def create_pipeline(**kwargs: Any) -> Pipeline:
    return Pipeline(
        [node(func=preprocess_train, inputs="train", outputs="preprocessed_train", name="preprocessing_train",)]
    )
