from WimpyHypothesis import WimpyHypothesis
from BraveHypothesis import BraveHypothesis
from ChunkyWimpyHypothesis import ChunkyWimpyHypothesis
from KMeansHypothesis import KMeansHypothesis
from SimpleProbabilityHypothesis import SimpleProbabilityHypothesis

class HypothesisCollection:

    def __init__(self):

        brave = BraveHypothesis()
        wimpy = WimpyHypothesis()
        #kmeans = KMeansHypothesis(5,5)
        #probability = SimpleProbabilityHypothesis()
        #chunkywimp = ChunkyWimpyHypothesis()

        self.hypoObjArray  = [brave, wimpy] #, kmeans, probability, chunkywimp]
        self.hypoNameArray = [brave.getName(), wimpy.getName()] #, kmeans.getName(), probability.getName(), chunkywimp.getName()]


    def getHypothesisArray(self):
        return self.hypoObjArray

    def getNameArray(self):
        return self.hypoNameArray