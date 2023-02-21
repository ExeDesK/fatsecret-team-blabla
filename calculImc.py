import argparse

def calculer_imc(taille_cm, poids):
    """Fonction pour calculer l'IMC à partir de la taille en cm et du poids"""
    taille_m = taille_cm / 100
    imc = poids / (taille_m ** 2)
    return imc

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calcul de l\'IMC')
    parser.add_argument('taille', type=float, help='Taille en centimètres')
    parser.add_argument('poids', type=float, help='Poids en kilogrammes')
    args = parser.parse_args()

    imc = calculer_imc(args.taille, args.poids)
    print(f"{imc:.2f}")
