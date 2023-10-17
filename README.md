# genetic_algorithm
Computing the Himmelblau Function Using Genetic Algorithm

Here are three different versions of the genetic algorithm files, each with variations in the mutation process.

VERSION: 
1. [tugas1.py](https://github.com/tirtaagungjati/genetic_algorithm/blob/main/tugas1.py) 
"In the mutation process, a check is performed with a random value between 0 and 1. If the value is less than the mutation probability, a random selection is made on each individual result generated after the crossover process between variables x or y. The selected value is then incremented by a random value between -1 and 1, which can be a decimal. This concept is derived from the reading of the paper 'A Study of Genetic Algorithm in Solving TSP' by Arief Widhiyasa."

2. [tugas1_ver2.py](https://github.com/tirtaagungjati/genetic_algorithm/blob/main/tugas1_ver2.py) 
"In the second code, mutation is performed a total of 'n_mut' times, which is determined by calculating the mutation probability multiplied by the population size and the number of variables or genes in a chromosome. The result should be rounded to the nearest integer, which is why we use 'int()'. Subsequently, 'n_mut' mutations are applied to individuals within the population resulting from the crossover process. These individuals are randomly selected from a pool of 100 populations. After selection, another random process determines whether variable 'x' or 'y' will undergo mutation, and its value will be replaced with a random value within the range of -6 to 6, as estimated based on Figure 2. This concept was inspired by the following YouTube video: https://www.youtube.com/watch?v=1CIIlk6saak&t=298s."

3. [tugas1_ver3.py](https://github.com/tirtaagungjati/genetic_algorithm/blob/main/tugas1_ver3.py) 
"In the third code, mutation is performed 'n_mut' times, just like in the second code, due to the same calculation. However, the key difference lies in the fact that instead of replacing the value with a random value from -6 to 6, the value of either variable 'x' or 'y' is randomly selected, and then it's incremented by a random value between 0 and 1, which can be a decimal. This addition is done using a normal distribution (Gaussian) with a mean of 0 and a standard deviation of 1 for mutation. This concept was inspired by the book 'Practical Genetic Algorithms' by Randy L. Haupt."