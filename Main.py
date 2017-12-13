import SVM
import os
import support_function

"""
Author: Trinh Man Hoang
:usage:
    1. Load features have been extracted respected to the train_dev split order
    2. Apply those feature to SVM model 
    3. Predict and evaluate
    4. Store result into each lbval.txt and val.txt
    5. Also print result by console
"""


Root = 'db\\'
score = 0
for data_direct in os.listdir(Root):

    folder_direct = Root + data_direct + '\\'
    X_train, Y_train = support_function.get_features_labels_from_folder(folder_direct,'train', 'vgg16')
    X_test, Y_test = support_function.get_features_labels_from_folder(folder_direct,'dev', 'vgg16')

    model = SVM.my_svm(X_train, Y_train)
    pred_labels = model.predict(X_test)

    with open(folder_direct + "lbval.txt", 'w+') as predict_result:
        for label in pred_labels:
            predict_result.write(str(label) + "\n")

    batch_score = model.score(X_test, Y_test)
    with open(folder_direct + "val.txt", 'w+') as score_file:
        score_file.write(str(batch_score))
    score += batch_score
    print("SVM: ",batch_score)

print("Mean score: ", score/len(os.listdir(Root)))