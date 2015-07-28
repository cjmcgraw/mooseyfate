import unittest
import matplotlib.pyplot as plt
import numpy as np
from src.hypothesis.LogRegressionHypothesis import LogRegressionHypothesis
from sklearn import metrics
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn import datasets

class LogRegressionHypothesisTest(unittest.TestCase):

    def setUp(self):
        self._hypothesis = LogRegressionHypothesis()

    def tearDown(self):
        self._hypothesis = None

    def test_idea(self):
        """
            win:    [1, 1, 1], [0, 1, -1]

            lose:   [1, 1, -1], [0, 1, 1]

            no/info:[1, 0, 0], [0, 0, 0]
        """
        X_training = [[1, 1],[0, 1],[1, 1],[0, 1],[1, 0],[0, 0]]

        y_target = [1, -1, -1, 1, 0, 0]

        model = LogisticRegression() #LinearRegression
        model.fit(X_training, y_target)
        print("-------------==================###########Model")
        print(model)
        # make predictions
        expected = y_target
        predicted = model.predict(X_training)
        # summarize the fit of the model
        print("-------------==================###########Fitness")
        print("Predicted:"+str(predicted))
        print(metrics.classification_report(expected, predicted))
        print(metrics.confusion_matrix(expected, predicted))
        # Show / Debug the regression line
        print("-------------==================###########Plot")
        npX = np.array(X_training)
        plt.scatter(npX[:,0], npX[:,1],  color='black')
        plt.plot(X_training, model.predict(X_training), color='blue',linewidth=3)
        plt.show()
