import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    os.system('clear')

    presidentHeights = pd.read_csv('./docs/presidentHeights.csv')

    # Transforma em array
    heightsInCm = np.array(presidentHeights['height(cm)'])

    print('Average: ', np.mean(heightsInCm))     # Média
    print('Standard Deviation: ', np.std(heightsInCm))  # Desvio padrão
    print('Maximun: ', heightsInCm.max())
    print('Minimun: ', heightsInCm.min())

    sns.set()
    plt.hist(heightsInCm)
    plt.title('Distribuição de altura dos presidendes dos EUA')
    plt.xlabel('Altura (cm)')
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.show()


main()
