from WimpyHypothesis import WimpyHypothesis
from BraveHypothesis import BraveHypothesis
from ChunkyWimpyHypothesis import ChunkyWimpyHypothesis
from SimpleProbabilityHypothesis import SimpleProbabilityHypothesis

class HypothesisCollection:

    def __init__(self):

        brave = BraveHypothesis()
        wimpy = WimpyHypothesis()
        #kmeans = KMeansHypothesis(5,5)
        #probability = SimpleProbabilityHypothesis()
        #chunkywimp = ChunkyWimpyHypothesis()
        #coinflip = RandoHypothesis()

        self.hypoObjArray  = [brave, wimpy] #, kmeans, probability, chunkywimp, coinflip]
        self.hypoNameArray = [brave.getName(), wimpy.getName()] #, kmeans.getName(), probability.getName(), chunkywimp.getName(), coinflip.getName()]


    def getHypothesisArray(self):
        return self.hypoObjArray

    def getNameArray(self):
        return self.hypoNameArray
