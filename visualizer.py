import numpy as np
import matplotlib.pyplot as plt


def visualize(data):
 
    data = np.array(data)

    mean = np.mean(data, axis=0)
    standardized_data = data - mean

    cov_matrix = np.cov(standardized_data, rowvar=False)

    eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)

    sorted_indices = np.argsort(eigen_values)[::-1]  
    eigen_values = eigen_values[sorted_indices]
    eigen_vectors = eigen_vectors[:, sorted_indices]

    num_components = 4  
    selected_vectors = eigen_vectors[:, :num_components]

    reduced_data = np.dot(standardized_data, selected_vectors)

    colors = ['red' if row[-1] == 1 else 'blue' for row in data]

    plt.figure(figsize=(8, 6))
    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c= colors, edgecolor='k')
    plt.title("k-NN")
    plt.grid()
    plt.show()

