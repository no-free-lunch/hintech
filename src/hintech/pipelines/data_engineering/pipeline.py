from kedro.pipeline import node, Pipeline

from hintech.pipelines.data_engineering.nodes import (
    preprocess_train,
)


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=preprocess_train,
                inputs="train",
                outputs="preprocessed_train",
                name="preprocessing_train",
            )
        ]
    )
