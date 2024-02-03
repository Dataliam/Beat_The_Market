# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:38:01 2024

@author: liamb
"""
from portfolio_manager import PortfolioManager
from visualizer import Visualizer

def main():
    # Initialisation avec des exemples de symboles d'actions et des poids
    symbols = ['AAPL', 'MSFT', 'GOOGL','LVMH']  # Exemple de symboles d'actions
    weights = [0.3, 0.5, 0.1, 0.1]  # Exemple de répartition du portefeuille
    start_date = '2023-01-01'
    end_date = '2023-12-31'
    
    # Demander à l'utilisateur le montant de l'argent misé
    try:
        initial_investment = float(input("Veuillez entrer le montant de l'argent misé (en €) : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return
    
    portfolio_manager = PortfolioManager(symbols, weights, start_date, end_date)
    portfolio_performance, cac40_performance, eurostoxx50_performance = portfolio_manager.get_performance()

    # Utiliser le montant saisi par l'utilisateur pour le calcul de la valeur finale
    final_value_portfolio = portfolio_manager.calculate_final_value(portfolio_performance, initial_investment)
    final_value_cac40 = portfolio_manager.calculate_final_value(cac40_performance, initial_investment)
    final_value_eurostoxx50 = portfolio_manager.calculate_final_value(eurostoxx50_performance, initial_investment)

    print(f"Valeur finale de l'investissement de {initial_investment}€ dans le portefeuille : {final_value_portfolio.iloc[-1]:.2f}€")
    print(f"Valeur finale de l'investissement de {initial_investment}€ dans le CAC40 : {final_value_cac40.iloc[-1]:.2f}€")
    print(f"Valeur finale de l'investissement de {initial_investment}€ dans l'Euro Stoxx 50 : {final_value_eurostoxx50.iloc[-1]:.2f}€")

    # Visualisation
    visualizer = Visualizer()
    visualizer.compare_performances(portfolio_performance, cac40_performance, eurostoxx50_performance, start_date, end_date)

if __name__ == "__main__":
    main()