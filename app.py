from flask import Flask, render_template, request, jsonify
from portfolio_manager import PortfolioManager
# Supposons que visualizer.py contienne une fonction pour générer des visualisations

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            symbols = request.form.get('symbols').split(',')
            weights = list(map(float, request.form.get('weights').split(',')))
            initial_investment = float(request.form.get('initial_investment'))
            start_date = request.form.get('start_date')
            end_date = request.form.get('end_date')
            
            # Création de l'instance et calcul
            portfolio_manager = PortfolioManager(symbols, weights, start_date, end_date)
            # Supposons que PortfolioManager peut calculer et retourner les résultats désirés
            results = portfolio_manager.calculate_results()  # À implémenter selon vos besoins

            # Générer et sauvegarder la visualisation, ou préparer les données pour l'affichage
            # visualizer.plot_results(results)  # À adapter selon votre logique de visualisation

            return render_template('index.html', results=results, submitted=True)
        except Exception as e:
            return render_template('index.html', error=str(e), submitted=False)

    return render_template('index.html', submitted=False)

if __name__ == '__main__':
    app.run(debug=True)
