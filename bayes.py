from sklearn.naive_bayes import MultinomialNB

def my_bayes(X_train, Y_train):
    model = MultinomialNB().fit(X_train,Y_train)
    return model