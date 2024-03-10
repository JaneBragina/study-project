from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

def train_and_evaluate(X_train, y_train, X_test, y_test):
    clf = DecisionTreeClassifier(criterion="gini", random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    cm = confusion_matrix(y_test, y_pred)
    
    return accuracy, precision, recall, f1, cm

def lab_2_tab_4_5():
    wine_df = pd.read_csv("wine.csv", header=None, skiprows=1) 

    X = wine_df.drop(columns=[0])
    y = wine_df[0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    correlation_matrix = wine_df.corr()

    corr_features = correlation_matrix.abs().nlargest(3, 0).index[1:]
    X_train_corr = X_train[corr_features]
    X_test_corr = X_test[corr_features]

    accuracy_corr, precision_corr, recall_corr, f1_corr, cm_corr = train_and_evaluate(X_train_corr, y_train, X_test_corr, y_test)

    uncorr_features = correlation_matrix.abs().nsmallest(2, 0).index[1:]
    X_train_uncorr = X_train[uncorr_features]
    X_test_uncorr = X_test[uncorr_features]

    accuracy_uncorr, precision_uncorr, recall_uncorr, f1_uncorr, cm_uncorr = train_and_evaluate(X_train_uncorr, y_train, X_test_uncorr, y_test)

    print("Метрики для двух самых коррелирующих признаков:")
    print("Accuracy:", accuracy_corr)
    print("Precision:", precision_corr)
    print("Recall:", recall_corr)
    print("F1 Score:", f1_corr)
    print("Confusion Matrix:\n", cm_corr)

    print("\nМетрики для двух не коррелирующих признаков:")
    print("Accuracy:", accuracy_uncorr)
    print("Precision:", precision_uncorr)
    print("Recall:", recall_uncorr)
    print("F1 Score:", f1_uncorr)
    print("Confusion Matrix:\n", cm_uncorr)

    svm = SVC(kernel='linear', probability=True, random_state=42)
    svm.fit(X_train, y_train)
    svm_y_pred = svm.predict(X_test)

    svm_accuracy = accuracy_score(y_test, svm_y_pred)
    svm_precision = precision_score(y_test, svm_y_pred, average='weighted')
    svm_recall = recall_score(y_test, svm_y_pred, average='weighted')
    svm_f1 = f1_score(y_test, svm_y_pred, average='weighted')

    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    rf_y_pred = rf.predict(X_test)

    rf_accuracy = accuracy_score(y_test, rf_y_pred)
    rf_precision = precision_score(y_test, rf_y_pred, average='weighted')
    rf_recall = recall_score(y_test, rf_y_pred, average='weighted')
    rf_f1 = f1_score(y_test, rf_y_pred, average='weighted')

    svm_probs = svm.predict_proba(X_test)
    rf_probs = rf.predict_proba(X_test)

    svm_fpr, svm_tpr, _ = roc_curve(y_test, svm_probs[:, 1], pos_label=1)
    rf_fpr, rf_tpr, _ = roc_curve(y_test, rf_probs[:, 1], pos_label=1)

    svm_auc = auc(svm_fpr, svm_tpr)
    rf_auc = auc(rf_fpr, rf_tpr)

    plt.figure(figsize=(8, 6))
    plt.plot(svm_fpr, svm_tpr, linestyle='--', label='SVM (AUC = %0.2f)' % svm_auc)
    plt.plot(rf_fpr, rf_tpr, marker='.', label='Random Forest (AUC = %0.2f)' % rf_auc)

    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')

    plt.legend()
    plt.title('ROC Curve')
    plt.show()

    feature_importance = rf.feature_importances_
    plt.figure(figsize=(10, 6))
    sns.barplot(x=feature_importance, y=X.columns)
    plt.title('Feature Importance')
    plt.show()