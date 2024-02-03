# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:33:56 2024

@author: liamb
"""

#pip install pandas matplotlib yfinance
import yfinance as yf
import pandas as pd

class PortfolioManager:
    def __init__(self, symbols, weights, start_date, end_date):
        self.symbols = symbols
        self.weights = weights
        self.start_date = start_date
        self.end_date = end_date
        self.portfolio_df = self.download_data()

    def download_data(self):
        # Télécharge les données historiques pour chaque action dans le portefeuille
        data = yf.download(self.symbols, start=self.start_date, end=self.end_date)['Adj Close']
        
        # Assure que les données sont dans le format DataFrame
        if isinstance(data, pd.Series):
            data = data.to_frame()
        return data

    def calculate_daily_returns(self):
        # Calcule les rendements quotidiens pour le portefeuille
        daily_returns = self.portfolio_df.pct_change()
        return daily_returns

    def calculate_portfolio_performance(self):
        # Calcule la performance du portefeuille en se basant sur les rendements quotidiens pondérés
        daily_returns = self.calculate_daily_returns()
        portfolio_returns = (daily_returns * self.weights).sum(axis=1)
        cumulative_returns = (1 + portfolio_returns).cumprod() - 1
        return cumulative_returns

    def get_cac40_performance(self):
        # Télécharge les données du CAC40 et calcule sa performance
        cac40 = yf.download('^FCHI', start=self.start_date, end=self.end_date)['Adj Close']
        cac40_returns = cac40.pct_change()
        cac40_cumulative_returns = (1 + cac40_returns).cumprod() - 1
        return cac40_cumulative_returns

    def get_performance(self):
        # Retourne la performance du portefeuille et du CAC40
        portfolio_performance = self.calculate_portfolio_performance()
        cac40_performance = self.get_cac40_performance()
        eurostoxx50_performance = self.get_eurostoxx50_performance()
        return portfolio_performance, cac40_performance, eurostoxx50_performance

    def calculate_final_value(self, cumulative_returns, initial_investment=100):
    # Calcule la valeur finale basée sur les rendements cumulatifs et l'investissement initial
        final_value = initial_investment * (1 + cumulative_returns)
        return final_value

    def get_eurostoxx50_performance(self):
    # Télécharge les données de l'Euro Stoxx 50 et calcule sa performance
        eurostoxx50 = yf.download('^STOXX50E', start=self.start_date, end=self.end_date)['Adj Close']
        eurostoxx50_returns = eurostoxx50.pct_change()
        eurostoxx50_cumulative_returns = (1 + eurostoxx50_returns).cumprod() - 1
        return eurostoxx50_cumulative_returns
