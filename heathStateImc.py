import argparse

def calculer_heathState(imc):
    if imc < 18.5:
        return "You are underweight"
    elif imc < 25:
        return "You are in good health"
    elif imc < 30:
        return "You are overweight"
    else:
        return "You are obese"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Etat de santé d\'arpès l\'IMC')
    parser.add_argument('IMC', type=float, help='IMC')
    args = parser.parse_args()

    heathState = calculer_heathState(args.imc)
    print(heathState)
