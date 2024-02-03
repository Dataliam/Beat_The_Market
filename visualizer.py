# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:39:26 2024

@author: liamb
"""

import matplotlib.pyplot as plt

class Visualizer:
    def compare_performances(self, portfolio_performance, cac40_performance,eurostoxx50_performance, start_date, end_date):
        # Configure le tracé
        plt.figure(figsize=(14, 7))
        plt.plot(portfolio_performance, label='Portfolio')
        plt.plot(cac40_performance, label='CAC40', linestyle='--')
        plt.plot(eurostoxx50_performance, label='Euro Stoxx 50', linestyle='-.')
        # Définit les titres et les légendes
        plt.title('Comparaison de la Performance du Portfolio vs CAC40')
        plt.xlabel('Date')
        plt.ylabel('Rendement Cumulatif')
        plt.legend(loc='best')
        
        # Formatte les axes
        plt.xticks(rotation=45)
        plt.grid(True)
        
        # Affiche le graphique
        plt.show()