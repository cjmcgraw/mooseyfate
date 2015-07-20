To run the specific modules for your project execute them using pythons module command above the root of the project:
```
[~/workspace/lab/ml]$ tree -I '.*egg-info|.*pyc|__init.*'
.
└── mooseyfate
    ├── README.md
    ├── setup.py
    ├── src
    │   ├── Decisioner.py
    │   ├── hypothesis
    │   │   ├── BraveHypothesis.py
    │   │   ├── ChunkyWimpyHypothesis.py
    │   │   ├── Hypothesis.py
    │   │   ├── KMeansHypothesis.py
    │   │   ├── SimpleProbabilityHypothesis.py
    │   │   └── WimpyHypothesis.py
    │   └── lib
    │       ├── HelperFunctions.py
    │       └── TestingEnvironment.py
    └── test
        ├── DecisionerTest.py
        ├── hypothesis
        │   └── MockHypothesis.py
        └── lib
            └── HelperFunctionsTest.py

7 directories, 14 files

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

