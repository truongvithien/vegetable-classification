from sklearn.neighbors import KNeighborsClassifier

def my_knn(k, X_TRAIN, Y_TRAIN):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_TRAIN, Y_TRAIN)
    return model
