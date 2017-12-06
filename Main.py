import os
import support_function
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB

Root = 'db/'
for data_direct in os.listdir(Root):
    folder_direct = Root + data_direct + '/'
    X_train, Y_train = support_function.get_features_labels_from_folder(folder_direct,'train')
    X_test, Y_test = support_function.get_features_labels_from_folder(folder_direct,'dev')

    # #SVM run + score ( 0.9 )
    model = svm.SVC(kernel='linear').fit(X_train,Y_train)
    score = model.score(X_test, Y_test)
    print("SVM: %d",score)

    # # Knn run + score (0.64 )
    model = KNeighborsClassifier(5).fit(X_train,Y_train)
    score = model.score(X_test, Y_test)
    print("Knn: %d",score)

    # #native Bayes + score (0.436)
    model = MultinomialNB().fit(X_train, Y_train)
    score = model.score(X_test, Y_test)
    print("Bayes: %d",score)