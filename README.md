# Portfolio Analytics: Modern Portfolio Theory (Markowitz)

This project implements the **Markowitz Modern Portfolio Theory (MPT)** to identify the **Efficient Frontier** and the **Optimal Tangency Portfolio** using historical market data and Monte Carlo simulations.

##  Overview
This tool automates the process of portfolio optimization by:
* **Fetching real-time financial data** from the Yahoo Finance API.
* **Executing a Monte Carlo simulation** with 5,000+ random weight allocations.
* **Calculating risk-adjusted performance metrics**, including the Sharpe Ratio.
* **Visualizing the Efficient Frontier** and the Capital Market Line (CML).

##  Project Structure
* **Project_Markowitz.ipynb**: The main narrative notebook containing the analysis, visualizations, and critical conclusions.
* **functions_kit.py**: A dedicated Python module containing the computational engine (returns calculation, statistics, simulation, and plotting).

##  Getting Started

### Prerequisites 
You will need Python 3.x and the following libraries:

pip install pandas numpy matplotlib yfinance

### Installation

1. **Clone the repository.**
2. **Ensure `functions_kit.py` is in the same directory** as the notebook.
3. **Open `Project_Markowitz.ipynb`** in Jupyter or VS Code and run all cells.

###  Methodology

* **Risk-Free Rate**: Set at **2.0%**, reflecting the current Euro Short-Term Rate (€STR) environment.
* **Assets Selection**: Currently configured for major European tickers (e.g., LVMH, Sanofi, BNP Paribas).
* **Performance Metric**: Maximization of the Sharpe Ratio to find the Tangency Portfolio.

###  Disclaimer

This project is for **academic purposes only** (L3 Economics, University of Rouen). It represents a "perfect world" theoretical framework and does not account for market frictions, transaction costs, or non-linear risks.
