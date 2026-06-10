"""
visualization.py

Visualization Module
for Hybrid DWT-DCT Watermarking
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# =====================================================
# Pareto Front Plot
# =====================================================

def plot_pareto_front(result):

    F = result.F

    fig, ax = plt.subplots(
        figsize=(8, 6)
    )

    ax.scatter(
        -F[:, 0],
        -F[:, 2],
        s=50
    )

    ax.set_title(
        "Pareto Front"
    )

    ax.set_xlabel(
        "PSNR"
    )

    ax.set_ylabel(
        "NC"
    )

    ax.grid(True)

    return fig


# =====================================================
# Parameter Space Plot
# =====================================================

def plot_parameter_space(result):

    X = result.X

    fig, ax = plt.subplots(
        figsize=(8, 6)
    )

    ax.scatter(
        X[:, 0],
        X[:, 1]
    )

    ax.set_title(
        "Alpha-Beta Search Space"
    )

    ax.set_xlabel(
        "Alpha"
    )

    ax.set_ylabel(
        "Beta"
    )

    ax.grid(True)

    return fig


# =====================================================
# PSNR vs Alpha
# =====================================================

def plot_psnr_vs_alpha(
        alpha_values,
        psnr_values):

    fig, ax = plt.subplots(
        figsize=(8, 6)
    )

    ax.plot(
        alpha_values,
        psnr_values,
        marker='o'
    )

    ax.set_title(
        "PSNR vs Alpha"
    )

    ax.set_xlabel(
        "Alpha"
    )

    ax.set_ylabel(
        "PSNR (dB)"
    )

    ax.grid(True)

    return fig


# =====================================================
# NC vs Alpha
# =====================================================

def plot_nc_vs_alpha(
        alpha_values,
        nc_values):

    fig, ax = plt.subplots(
        figsize=(8, 6)
    )

    ax.plot(
        alpha_values,
        nc_values,
        marker='o'
    )

    ax.set_title(
        "NC vs Alpha"
    )

    ax.set_xlabel(
        "Alpha"
    )

    ax.set_ylabel(
        "NC"
    )

    ax.grid(True)

    return fig


# =====================================================
# SSIM vs Alpha
# =====================================================

def plot_ssim_vs_alpha(
        alpha_values,
        ssim_values):

    fig, ax = plt.subplots(
        figsize=(8, 6)
    )

    ax.plot(
        alpha_values,
        ssim_values,
        marker='o'
    )

    ax.set_title(
        "SSIM vs Alpha"
    )

    ax.set_xlabel(
        "Alpha"
    )

    ax.set_ylabel(
        "SSIM"
    )

    ax.grid(True)

    return fig


# =====================================================
# Attack Robustness Plot
# =====================================================

def plot_attack_robustness(
        attack_names,
        nc_scores):

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    ax.bar(
        attack_names,
        nc_scores
    )

    ax.set_title(
        "Attack Robustness"
    )

    ax.set_ylabel(
        "NC Score"
    )

    ax.set_xticklabels(
        attack_names,
        rotation=45
    )

    return fig


# =====================================================
# BER Under Attacks
# =====================================================

def plot_ber_attack(
        attack_names,
        ber_scores):

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    ax.bar(
        attack_names,
        ber_scores
    )

    ax.set_title(
        "BER under Attacks"
    )

    ax.set_ylabel(
        "BER"
    )

    ax.set_xticklabels(
        attack_names,
        rotation=45
    )

    return fig


# =====================================================
# Baseline Comparison
# =====================================================

def plot_baseline_comparison(
        comparison_df):

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    methods = comparison_df[
        "Method"
    ]

    psnr = comparison_df[
        "PSNR"
    ]

    ax.bar(
        methods,
        psnr
    )

    ax.set_title(
        "Baseline Comparison"
    )

    ax.set_ylabel(
        "PSNR"
    )

    return fig


# =====================================================
# Metrics Radar Chart
# =====================================================

def plot_radar_chart(
        metrics_dict):

    labels = list(
        metrics_dict.keys()
    )

    values = list(
        metrics_dict.values()
    )

    values += values[:1]

    angles = np.linspace(
        0,
        2*np.pi,
        len(labels),
        endpoint=False
    ).tolist()

    angles += angles[:1]

    fig = plt.figure(
        figsize=(8, 8)
    )

    ax = plt.subplot(
        polar=True
    )

    ax.plot(
        angles,
        values
    )

    ax.fill(
        angles,
        values,
        alpha=0.25
    )

    ax.set_xticks(
        angles[:-1]
    )

    ax.set_xticklabels(
        labels
    )

    return fig


# =====================================================
# Convert Metrics to DataFrame
# =====================================================

def metrics_to_dataframe(
        metrics_dict):

    df = pd.DataFrame(
        [metrics_dict]
    )

    return df


# =====================================================
# Attack Result DataFrame
# =====================================================

def attack_results_dataframe(
        attack_results):

    df = pd.DataFrame(
        attack_results
    )

    return df


# =====================================================
# Baseline DataFrame
# =====================================================

def baseline_dataframe(
        baseline_results):

    df = pd.DataFrame(
        baseline_results
    )

    return df