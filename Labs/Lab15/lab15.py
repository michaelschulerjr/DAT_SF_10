import pandas as pd
import numpy as np
import datetime as dt
from sklearn.cross_validation import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB


def cross_validate(X, y, classifier, k_fold):
    "Scores classifier using kfold cross_validation"
    # derive a set of (random) training and testing indices
    k_fold_indices = KFold(len(X), n_folds=k_fold,
                           shuffle=True, random_state=0)

    k_score_total = 0
    # train and score classifier for each slice
    for train_slice, test_slice in k_fold_indices :
        model = classifier(X[train_slice],y[train_slice])
        k_score = model.score(X[test_slice], y[test_slice])
        k_score_total += k_score

    # return the average accuracy
    return k_score_total/k_fold


def cleanData():
    "Loads and cleans heart disease data"
    df = pd.read_csv("heart_disease.csv",header=None)
    df.columns = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach',
                  'exang','oldpeak','slope','ca','thal','num']
    df = df.convert_objects(convert_numeric=True)
    df.dropna(inplace=True)
    df['num'] = df['num'].replace(to_replace=[2.0, 3.0, 4.0], value=1.0)
    features = df.ix[:, 0:13].values
    target = df.num.values

    return features, target


def scoreModels(features, target, folds=10):
    "Calcs crovs-validation scores for multiple algorithms"
    models = []
    models.append(RandomForestClassifier(random_state=0).fit)
    models.append(LogisticRegression(C=1.0).fit)
    models.append(KNeighborsClassifier(3).fit)
    models.append(SVC(C=1.0))
    models.append(GaussianNB().fit)

    for alg in models:
        print alg
        print cross_validate(features, target, alg, folds)


def main():
    features, target = cleanData()
    scoreModels(features, target)


if __name__ == '__main__':
    main()



