import numpy as np
def euclidean_distance(row1, row2):
    distance = 0
    for i in range(len(row1)):
        distance += (row1[i] - row2[i])**2
    return np.sqrt(distance)

if __name__=="__main__":
    dataset = [[2.7810836,2.550537003],
                [1.465489372,2.362125076],
                [3.396561688,4.400293529],
                [1.38807019,1.850220317],
                [3.06407232,3.005305973],
                [7.627531214,2.759262235],
                [5.332441248,2.088626775],
                [6.922596716,1.77106367],
                [8.675418651,-0.242068655],
                [7.673756466,3.508563011]]
    row0 = dataset[0]
    for row in dataset:
        distance = euclidean_distance(row0, row)
        print(distance)
    new_d = np.array(dataset)
    row0_new = np.array(row0)
    new_distance = np.sqrt(np.sum((row0_new - new_d) ** 2, axis=1))