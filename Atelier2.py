import numpy as np


print("--- Partie 1 ---")

temperature = np.array([22.5, 24.0, 19.8, 21.2, 23.5, 25.1, 20.7])

print("1) Type :", type(temperature))

print("2) Dimension :", temperature.ndim)


print("3) Forme :", temperature.shape)

print("4) Première température :", temperature[0])

print("5) Dernière température :", temperature[-1])

print("6) Trois premières :", temperature[:3])

temp_modifie = temperature.copy()
temp_modifie[0] += 1
temp_modifie[-1] += 1
print("7) Après augmentation :", temp_modifie)

temp_triee = np.sort(temperature)
print("8) Tableau trié :", temp_triee)
print("\n")


print("--- Partie 2 ---")

Temperatures = np.array([
    [22, 25, 20, 19, 24, 28, 30],
    [18, 21, 19, 22, 25, 27, 26],
    [30, 32, 29, 28, 27, 33, 35],
    [15, 17, 16, 18, 19, 20, 21],
    [25, 26, 24, 27, 29, 31, 30]
])

Precipitations = np.random.uniform(0, 20, (5, 7))
Precipitations = Precipitations.round(1)

print("3) Forme de Temperatures :", Temperatures.shape)
print("   Forme de Precipitations :", Precipitations.shape)

jours = np.arange(1, 8)
print("5) Jours :", jours)

t_transpose = Temperatures.T
print("6) Transposée de Temperatures :\n", t_transpose)

produit = np.dot(Temperatures, Precipitations.T)
print("7) Produit matriciel :\n", produit)
print("\n")


print("--- Partie 3 ---")

moyenne_par_ville = Temperatures.mean(axis=1)
print("1) Moyenne par ville :", moyenne_par_ville)

max_ville = Temperatures.max(axis=1)
min_ville = Temperatures.min(axis=1)
print("2) Max par ville :", max_ville)
print("   Min par ville :", min_ville)

moyenne_generale = Temperatures.mean()
print("3) Moyenne générale :", round(moyenne_generale, 2))

mediane_ville = np.median(Temperatures, axis=1)
print("4) Médiane par ville :", mediane_ville)

std_ville = np.std(Temperatures, axis=1)
print("5) Écart-type par ville :", std_ville.round(2))

total_precip_jour = Precipitations.sum(axis=0) 
total_precip_ville = Precipitations.sum(axis=1) 
print("6) Total précipitations par jour :", total_precip_jour.round(1))
print("   Total précipitations par ville :", total_precip_ville.round(1))

masque = Temperatures[1, :] > 25
jours_chauds = jours[masque]
print("7) Jours chauds (>25°C) pour la 2e ville :", jours_chauds)

masque1 = Precipitations[1, :] == 0
jours_sec = jours[masque1]
print("8) Jours sans pluie pour la 2e ville :", jours_sec)

temp_triee_par_ville = np.sort(Temperatures, axis=1)
print("9) Températures triées par ville :\n", temp_triee_par_ville)

indice_max = Temperatures.argmax(axis=1)
print("10) Indice du jour le plus chaud par ville :", indice_max)
print("\n")


print("--- Partie 4 ---")

print("1) 3 premiers jours de la 2e ville :", Temperatures[1, :3])

print("2) 4 derniers jours de la dernière ville :", Temperatures[-1, -4:])

villes_sup_26 = np.where(moyenne_par_ville > 26)[0]
print("3) Indices des villes avec moyenne > 26°C :", villes_sup_26)

temp_fahrenheit = Temperatures * (9 / 5) + 32
print("4) Températures en Fahrenheit :\n", temp_fahrenheit)

temp_rechauffement = Temperatures + 2
print("5) Températures avec +2°C :\n", temp_rechauffement)

temp_limitee = np.clip(Temperatures, a_min=None, a_max=35)
print("6) Températures limitées à max 35°C :\n", temp_limitee)