import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

def main():
    cities = pd.read_csv('./docs/californiaCities.csv')

    latitude, longitude = cities["latd"], cities["longd"]
    population, area = cities["population_total"], cities["area_total_km2"]

    seaborn.set()
    plt.scatter(longitude, latitude, label=None, c=np.log10(population), cmap='viridis', s=area, linewidth=0, alpha=0.5)
    
    plt.xlabel('Longitude')
    plt.ylabel('Longitude')
    plt.colorbar(label='log$_{10}$(population)')
    plt.clim(3, 7)
    
    for area in [100, 300, 500]:
        plt.scatter([], [], c='k', alpha=0.3, s=area, label=str(area) + 'km$^2$')
    plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Areas')
    plt.title("Area da população da califórnia")
    plt.show()
    
    
    
    
    print('running...')


main()
