import random
import numpy as np
import matplotlib.pyplot as plt

# Menentukan seed untuk generator bilangan acak
RANDOM_SEED = 0
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# Fungsi Himmelblau
def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

# Inisialisasi populasi
def init_populasi(n_pop,n_vab):
    return [[random.uniform(-6, 6) for _ in range(n_vab)] for _ in range(n_pop)]

# Evaluasi fitness
def evaluate(populasi):
    return [1/himmelblau(ind[0], ind[1]) for ind in populasi]

# Seleksi Mesin Roulette
def seleksi_mesin_roulette(populasi, fitness):
    total_fitness = sum(fitness)
    probabilities = [f/total_fitness for f in fitness]
    cumulative_probabilities = np.cumsum(probabilities)  
    index_terpilih = []
    for _ in range(len(populasi)):
        r = random.random()
        for i, cp in enumerate(cumulative_probabilities):
            if r <= cp:
                index_terpilih.append(i)
                break
    
    return [populasi[i] for i in index_terpilih]

# Crossover (Blending)
def crossover(parents):
    betha = random.random()
    child1 = [betha*parents[0][i] + (1-betha)*parents[1][i] for i in range(2)]
    child2 = [(1-betha)*parents[0][i] + betha*parents[1][i] for i in range(2)]
    return [child1, child2]

# Mutasi
def mutate(populasi, n_mut):
    for _ in range(n_mut):
        individual = random.choice(populasi)
        individual[random.randint(0, 1)] = random.uniform(-6, 6)
    return populasi

# Algoritma genetika utama
def genetic_algorithm(n_vab=2, n_pop=100, prob_cross=0.8, prob_mut=0.2, n_iter=500):
    populasi = init_populasi(n_pop,n_vab)
    fitness_over_time = []
    # Plot sebaran populasi awal generasi 
    plt.figure(1)
    globalMinima = [[3.0, 2.0], [-2.805118, 3.131312], [-3.779310, -3.283186], [3.584458, -1.848126]]
    plt.scatter(*zip(*globalMinima), marker='X', color='red', zorder=1)
    plt.scatter(*zip(*populasi))
    plt.title('Distribusi Populasi Awal Generasi')
    plt.xlabel('X')
    plt.ylabel('Y')
    
    for gen in range(n_iter):
        populasi_bycross = []
        new_populasi = []
        fitness = evaluate(populasi)
        max_fitness = max(fitness)
        best_individual = populasi[np.argmax(fitness)]
        
        print(f"Generation {gen}, Fitness: {max_fitness}, Best individual: {best_individual}")
        
        fitness_over_time.append(max_fitness)
        
        populasi_roulette = seleksi_mesin_roulette(populasi, fitness)
        
        while len(populasi_bycross) < n_pop:
            parents = random.sample(populasi_roulette, 2)
            
            if random.random() < prob_cross:
                children = crossover(parents)
            else:
                children = parents
                
            populasi_bycross.extend(children)

        n_mut = int(prob_mut * n_pop * n_vab) # Banyaknya individu yang dimutasi
        new_populasi = mutate(populasi_bycross, n_mut)   

        populasi = new_populasi
    
    best_x,best_y = best_individual
    hasil_terbaik = himmelblau(best_x,best_y)
    print(f"Nilai Terbaik yang dihasilkan untuk variabel x = {best_x}, sedangkan untuk variabel y = {best_y}")
    print(f"Dengan nilai minimum global dari fungsi Himmelblau = {hasil_terbaik}")
    
    # Plot sebaran populasi akhir generasi     
    plt.figure(2)
    globalMinima = [[3.0, 2.0], [-2.805118, 3.131312], [-3.779310, -3.283186], [3.584458, -1.848126]]
    plt.scatter(*zip(*globalMinima), marker='X', color='red', zorder=1)
    plt.scatter(*zip(*populasi))
    plt.title('Distribusi Populasi Akhir Generasi')
    plt.xlabel('X')
    plt.ylabel('Y')
        
    # Plot fitness over time
    plt.figure(3)
    plt.plot(range(n_iter), fitness_over_time)
    plt.title('Fitness over time')
    plt.xlabel('Generasi')
    plt.ylabel('Fitness')
    plt.show()
    
if __name__ == "__main__":
    genetic_algorithm()
