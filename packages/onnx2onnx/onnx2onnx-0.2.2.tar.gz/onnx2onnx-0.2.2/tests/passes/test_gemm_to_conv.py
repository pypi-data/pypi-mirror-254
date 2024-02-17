"""
Copyright Jianjin Liao 2024

:Author: Jianjin Liao
:Email: jianjin.liao@intel.com

"""

import numpy as np
from onnx.helper import (
    make_graph,
    make_model,
    make_node,
    make_tensor,
    make_tensor_type_proto,
    make_value_info,
)

from onnx2onnx.graph import OnnxGraph
from onnx2onnx.passes import PASSES


def _build_test_graph():
    gemm = make_node(
        "Gemm",
        inputs=["x", "B", "C"],
        outputs=["y"],
        name="gemm",
        alpha=1.0,
        beta=1.0,
        transB=1,
    )
    graph = make_graph(
        [gemm],
        "graph",
        [make_value_info("x", make_tensor_type_proto(1, [1, 64]))],
        [make_value_info("y", make_tensor_type_proto(1, [1, 32]))],
        [
            make_tensor("B", 1, [32, 64], np.random.rand(32, 64)),
            make_tensor("C", 1, [32], np.random.rand(32)),
        ],
    )
    return make_model(graph)


def _build_quantize_test_graph():
    gemm = make_node(
        "Gemm",
        inputs=["A", "B", "C"],
        outputs=["Y"],
        name="gemm",
        alpha=1.0,
        beta=1.0,
        transB=1,
    )
    dequant = make_node(
        "DequantizeLinear",
        inputs=["x", "x_scale", "x_zero_point"],
        outputs=["B"],
        name="dequantzie",
        axis=0,
    )

    graph = make_graph(
        [dequant, gemm],
        "graph",
        [make_value_info("A", make_tensor_type_proto(1, [1, 64]))],
        [make_value_info("Y", make_tensor_type_proto(1, [1, 32]))],
        [
            make_tensor("C", 1, [32], np.random.rand(32)),
            make_tensor(
                "x", 3, [32, 64], np.random.randint(-128, 128, [32, 64], dtype="int8")
            ),
            make_tensor("x_scale", 1, [32], np.random.rand(32)),
            make_tensor("x_zero_point", 1, [32], np.random.rand(32)),
        ],
    )
    return make_model(graph)


def test_rewriter():
    graph = OnnxGraph(_build_test_graph())
    rewriter = PASSES.get("initializer_to_constant")
    graph = rewriter(graph)
    rewriter = PASSES.get("gemm_to_conv")
    graph = rewriter(graph)


def test_quantize_rewriter():
    graph = OnnxGraph(_build_quantize_test_graph())
    rewriter = PASSES.get("initializer_to_constant")
    graph = rewriter(graph)
    rewriter = PASSES.get("gemm_to_conv")
    graph = rewriter(graph)
