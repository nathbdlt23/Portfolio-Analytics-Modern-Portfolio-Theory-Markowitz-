"""
Portfolio Optimization Toolkit
------------------------------
This module provides functions to perform portfolio analysis based on 
Markowitz Modern Portfolio Theory, including Monte Carlo simulations 
and Capital Market Line (CML) visualization.

Author: [BIDAULT Nathan / GitHub ID: nathbdlt23]
Year: 2026
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def log_returns(prices_df):
    """
    Calculate daily logaritmic returns from a DataFrame of prices.

    Args:
        prices_df: DataFrame containing asset prices.

    Returns:
        DataFrame of logarithmic returns with NaN values dropped.
    """
    return np.log(prices_df/prices_df.shift(1)).dropna()


def get_stats(returns_df):
    """
    Calculate anualized mean returns and the covariance matrix.
    assumes 252 trading days in a year.

    Args:
        returns_df: DataFrame of daily logarithmic returns.

    Returns:
        A tuple containing (Annualized Returns, Covariance Matrix, Annualized Volatilities).
    """
    # Annualized average returns
    ann_returns = returns_df.mean() * 252
    
    # Annualized covariance matrix
    ann_cov = returns_df.cov() * 252
    
    # Annualized Volatilities 
    ann_vol = returns_df.std() * np.sqrt(252)

    return ann_returns, ann_cov, ann_vol

def simulate_portfolios(mean_returns, cov_matrix, num_portfolios=5000):
    """
    Performs a Monte Carlo simulation to estimate the Efficient Frontier.

    Args:
        mean_returns: Annualized expected returns for each asset.
        cov_matrix: Annualized covariance matrix of asset returns.
        num_portfolios: Number of random portfolios to simulate.

    Returns:
        A tuple containing:
            - np.ndarray: Results array [Returns, Volatility, Sharpe Ratio].
            - list: Record of weights used for each simulation.
    """
    results = []
    weights_record = []
    num_assets = len(mean_returns)
    for i in range(num_portfolios):
        # Generate random weights for each asset
        weights = np.random.random(num_assets)
        
        # Normalize weights to ensure they sum to 1
        weights = weights / np.sum(weights)
        weights_record.append(weights)
        
        # Calculate expected portfolio return (Annualized)
        p_ret = np.dot(weights, mean_returns)

        # Calculate portfolio volatility (Annualized Standard Deviation)
        p_var = np.dot(weights.T, np.dot(cov_matrix, weights))
        p_vol = np.sqrt(p_var)

        # Calculate Sharpe Ratio (Risk-adjusted return)
        # Using 2% (0.02) as the Risk-Free Rate, reflecting the Euro Short-Term Rate (ESTR)
        risk_free_rate = 0.02
        p_sharpe = (p_ret - risk_free_rate) / p_vol

        results.append([p_ret, p_vol, p_sharpe])
        
    return np.array(results), weights_record

def plot_mc_ef(results, risk_free_rate=0.02):
    """
    Plots the Monte Carlo simulation and the Capital Market Line (CML).

    Args:
        results: Array containing simulated returns, volatility, and Sharpe ratios.
        risk_free_rate: The rate used to plot the CML.

    Returns:
        The matplotlib Axes object containing the plot.
    """
    # Convert NumPy results to a DataFrame for better readability 
    df = pd.DataFrame(results, columns=["Returns", "Volatility", "Sharpe"])
    
    # Create the scatter plot
    ax = df.plot.scatter(x="Volatility",
                         y="Returns",
                         c="Sharpe",
                         cmap="viridis",
                         colorbar=True,
                         title="Monte Carlo Efficient Frontier & Capital Market Line",
                         figsize=(12, 7),
                         alpha=0.3
                        )
    
    #Identify and plot the Max Sharpe Ratio (MSR) portfolio
    msr_portfolio = df.loc[df["Sharpe"].idxmax()]
    ax.plot([msr_portfolio["Volatility"]],
            [msr_portfolio["Returns"]],
            color="red",
            marker="*",
            markersize=15,
            label="Tangency Portfolio (MSR)"
           )
    x_cml = [0, df["Volatility"].max()]
    y_cml = [risk_free_rate,risk_free_rate + x_cml[1] * msr_portfolio['Sharpe']]
    ax.plot(x_cml, y_cml,
            color="darkblue", 
            linestyle="--", 
            linewidth=2, 
            label="Capital Market Line (CML)"
           )
    ax.plot(0, 
            risk_free_rate, 
            marker="o", 
            markersize=15, 
            color="black", 
            label=f"Risk Free Rate: {risk_free_rate}"
           )
    
    ax.set_xlim(left=0) # We start at 0 volatility to see the Rf point
    ax.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    return ax
           
    
                         





    