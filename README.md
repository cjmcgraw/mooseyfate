To run the specific modules for your project execute them using pythons module command above the root of the project:
```
.
├── README.md
├── doc
│   ├── Hypo_oneRun_k11pt699_optpcp1ptpt680.mov
│   ├── ML\ -\ Hackathon.pptx
│   ├── ML\ -\ TimeSeriesPerceptron_themed.pptx
│   ├── json_ArrayOfObjects_final.json
│   └── ml-presentation-addendum.pptx
├── json_output.json
├── json_output.json.bak
├── json_output_final.json
├── mooseyfate.egg-info
│   └── PKG-INFO
├── runDecisioner.sh
├── setup.py
├── src
│   ├── Decisioner.py
│   ├── hypothesis
│   │   ├── BraveHypothesis.py
│   │   ├── ChunkyKNNHypothesis.py
│   │   ├── ChunkyWimpyHypothesis.py
│   │   ├── DrPerceptron.py
│   │   ├── Hypothesis.py
│   │   ├── HypothesisCollection.py
│   │   ├── KMeansHypothesis.py
│   │   ├── KNearestNeighbors.py
│   │   ├── NoLearnPerceptron.py
│   │   ├── OptimusPerceptron.py
│   │   ├── RandoHypothesis.py
│   │   ├── SimpleProbabilityHypothesis.py
│   │   └── WimpyHypothesis.py
│   └── lib
│       ├── HelperFunctions.py
│       └── TestingEnvironment.py
└── test
    ├── DecisionerIntegrationTest.py
    ├── DecisionerTest.py
    ├── hypothesis
    │   ├── BraveHypothesisTest.py
    │   ├── ChunkyKNNHypothesisTest.py
    │   ├── DrPerceptronHypothesisTest.py
    │   ├── KMeansHypothesisTest.py
    │   ├── KNearestNeighborsTest.py
    │   ├── MockHypothesis.py
    │   ├── OptimusPerceptronHypothesisTest.py
    │   ├── RandoHypothesisTest.py
    │   ├── SimpleProbabilityHypothesisTest.py
    │   └── WimpyHypothesisTest.py
    └── lib
        └── HelperFunctionsTest.py

8 directories, 41 files

[~/workspace/lab/ml]$ python -m mooseyfate.src.hypothesis.KMeansHypothesis
```

To run unit tests simply use pythons setup method:

```
[~/workspace/lab/ml/mooseyfate]$ python setup.py test
running test
running egg_info
writing pbr to mooseyfate.egg-info/pbr.json
writing mooseyfate.egg-info/PKG-INFO
writing top-level names to mooseyfate.egg-info/top_level.txt
writing dependency_links to mooseyfate.egg-info/dependency_links.txt
reading manifest file 'mooseyfate.egg-info/SOURCES.txt'
writing manifest file 'mooseyfate.egg-info/SOURCES.txt'
running build_ext
test_learn (test.DecisionerTest.DecisionerTest)
Tests the 'learn' method of the Decisioner ... ok
test_should_attack (test.DecisionerTest.DecisionerTest)
Tests the 'should_attack' method of the Decisioner ... ok
test_euclidean_distance_1dimension (test.lib.HelperFunctionsTest.HelperFunctionsTest)
Tests the euclidean distance in one dimension ... ok
test_euclidean_distance_2dimension (test.lib.HelperFunctionsTest.HelperFunctionsTest)
Tests the euclidean distance in 2 dimensions ... ok
test_euclidean_distance_Ndimension (test.lib.HelperFunctionsTest.HelperFunctionsTest)
Tests the euclidean distance in 2+ dimensions ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

