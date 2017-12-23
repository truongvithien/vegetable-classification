import SVM
import os
import support_function
import knn
import bayes


"""
Author: Trinh Man Hoang
:usage:
    1. Load features have been extracted respected to the train_dev split order
    2. Apply those feature to SVM model 
    3. Predict and evaluate
    4. Store result into each lbval.txt and val.txt
    5. Also print result by console
"""


Root = 'db'
SVM_score = 0
KNN_score = 0
Bayes_score = 0

for data_direct in os.listdir(Root):

    folder_direct = os.path.join(Root, data_direct)
    #folder_direct = Root + data_direct + '/'
    X_train, Y_train = support_function.get_features_labels_from_folder(folder_direct,'train', 'xception')
    X_test, Y_test = support_function.get_features_labels_from_folder(folder_direct,'dev', 'xception')

    SVM_model = SVM.my_svm(X_train, Y_train)
    SVM_pred_labels = SVM_model.predict(X_test)
    SVM_batch_score = SVM_model.score(X_test, Y_test)

    KNN_model = knn.my_knn(5,X_train, Y_train)
    KNN_pred_labels = KNN_model.predict(X_test)
    KNN_batch_score = KNN_model.score(X_test, Y_test)

    Bayes_model = bayes.my_bayes( X_train, Y_train)
    Bayes_pred_labels = Bayes_model.predict(X_test)
    Bayes_batch_score = Bayes_model.score(X_test, Y_test)

    with open(os.path.join(folder_direct, "lbval.txt"), 'w+') as predict_result:
        predict_result.write('SVM\n')
        for label in SVM_pred_labels:
            predict_result.write(str(label) + "\n")
        predict_result.write('KNN\n')
        for label in KNN_pred_labels:
            predict_result.write(str(label) + "\n")
        predict_result.write('Bayes\n')
        for label in Bayes_pred_labels:
            predict_result.write(str(label) + "\n")


    with open(os.path.join(folder_direct, "val.txt"), 'w+') as score_file:
        score_file.write('SVM\n')
        score_file.write(str(SVM_batch_score))
        score_file.write('KNN\n')
        score_file.write(str(KNN_batch_score))
        score_file.write('Bayes\n')
        score_file.write(str(Bayes_batch_score))




    SVM_score += SVM_batch_score
    KNN_score += KNN_batch_score
    Bayes_score += Bayes_batch_score
    print("SVM: ",SVM_batch_score)
    print("KNN: ", KNN_batch_score)
    print("Bayes: ", Bayes_batch_score)



print("Mean SVM score: ", SVM_score/len(os.listdir(Root)))
print("Mean KNN score: ", KNN_score/len(os.listdir(Root)))
print("Mean Bayes score: ", Bayes_score/len(os.listdir(Root)))
