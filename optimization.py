"""
optimization.py

NSGA-II Optimization Module
for Hybrid DWT-DCT Watermarking
"""

import numpy as np
import matplotlib.pyplot as plt

from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga2 import NSGA2

from pymoo.optimize import minimize

from watermark_core import (
    embed_watermark,
    extract_watermark
)

from metrics import (
    compute_psnr,
    compute_ssim,
    compute_nc,
    compute_ber
)


# =====================================================
# NSGA-II Optimization Problem
# =====================================================

class WatermarkOptimization(
        Problem):

    def __init__(
            self,
            image,
            watermark):

        self.image = image
        self.watermark = watermark

        super().__init__(
            n_var=2,
            n_obj=4,
            n_constr=0,
            xl=np.array([1, 1]),
            xu=np.array([20, 20])
        )

    def _evaluate(
            self,
            X,
            out,
            *args,
            **kwargs):

        results = []

        for solution in X:

            alpha = solution[0]
            beta = solution[1]

            try:

                watermarked = embed_watermark(
                    self.image,
                    self.watermark,
                    alpha,
                    beta
                )

                extracted = extract_watermark(
                    self.image,
                    watermarked,
                    (
                        self.watermark.shape[1],
                        self.watermark.shape[0]
                    )
                )

                psnr = compute_psnr(
                    self.image,
                    watermarked
                )

                ssim = compute_ssim(
                    self.image,
                    watermarked
                )

                nc = compute_nc(
                    self.watermark,
                    extracted
                )

                ber = compute_ber(
                    self.watermark,
                    extracted
                )

                # NSGA-II minimizes
                results.append([
                    -psnr,
                    -ssim,
                    -nc,
                    ber
                ])

            except Exception:

                results.append([
                    1000,
                    1000,
                    1000,
                    1000
                ])

        out["F"] = np.array(results)


# =====================================================
# Run Optimization
# =====================================================

def run_nsga2(
        image,
        watermark,
        population_size=30,
        generations=20):

    problem = WatermarkOptimization(
        image,
        watermark
    )

    algorithm = NSGA2(
        pop_size=population_size
    )

    result = minimize(
        problem,
        algorithm,
        ('n_gen', generations),
        seed=42,
        verbose=False
    )

    return result


# =====================================================
# Get Best Solution
# =====================================================

def get_best_solution(
        result):

    F = result.F
    X = result.X

    scores = []

    for i in range(len(F)):

        score = (
            -F[i][0] +
            -F[i][1] +
            -F[i][2] -
            F[i][3]
        )

        scores.append(score)

    best_idx = np.argmax(scores)

    best_alpha = X[
        best_idx
    ][0]

    best_beta = X[
        best_idx
    ][1]

    return (
        best_alpha,
        best_beta
    )


# =====================================================
# Pareto Data
# =====================================================

def get_pareto_data(
        result):

    data = []

    for f in result.F:

        data.append({

            "PSNR":
                -f[0],

            "SSIM":
                -f[1],

            "NC":
                -f[2],

            "BER":
                f[3]
        })

    return data


# =====================================================
# Pareto Plot
# =====================================================

def plot_pareto_front(
        result):

    F = result.F

    fig = plt.figure(
        figsize=(8, 6)
    )

    plt.scatter(
        -F[:, 0],
        -F[:, 2],
        c='blue'
    )

    plt.xlabel(
        "PSNR"
    )

    plt.ylabel(
        "NC"
    )

    plt.title(
        "Pareto Front"
    )

    plt.grid(True)

    return fig


# =====================================================
# Alpha-Beta Visualization
# =====================================================

def plot_parameter_space(
        result):

    X = result.X

    fig = plt.figure(
        figsize=(8, 6)
    )

    plt.scatter(
        X[:, 0],
        X[:, 1],
        c='red'
    )

    plt.xlabel(
        "Alpha"
    )

    plt.ylabel(
        "Beta"
    )

    plt.title(
        "Optimized Parameter Space"
    )

    plt.grid(True)

    return fig


# =====================================================
# Optimization Summary
# =====================================================

def optimization_summary(
        result):

    alpha,
    beta = get_best_solution(
        result
    )

    summary = {

        "Optimal Alpha":
            float(alpha),

        "Optimal Beta":
            float(beta),

        "Population":
            len(result.X),

        "Pareto Solutions":
            len(result.F)
    }

    return summary