To run the specific modules for your project execute them using pythons module command above the root of the project:
`
[~/workspace/lab/ml]$ tree
.
└── mooseyfate
    ├── Decisioner.py
    ├── hypothesis
    │   ├── BraveHypothesis.py
    │   ├── BraveHypothesis.pyc
    │   ├── ChunkyWimpyHypothesis.py
    │   ├── Hypothesis.py
    │   ├── Hypothesis.pyc
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── KMeansHypothesis.py
    │   ├── SimpleProbabilityHypothesis.py
    │   ├── WimpyHypothesis.py
    │   └── WimpyHypothesis.pyc
    ├── __init__.py
    ├── __init__.pyc
    ├── lib
    │   ├── HelperFunctions.py
    │   ├── HelperFunctions.pyc
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── TestingEnvironment.py
    │   └── TestingEnvironment.pyc
    └── README.md

3 directories, 21 files

[~/workspace/lab/ml]$ python -m mooseyfate.hypothesis.KMeansHypothesis
`
