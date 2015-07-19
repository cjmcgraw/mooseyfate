To run the specific modules for your project execute them using pythons module command above the root of the project:
```
[~/workspace/lab/ml]$ tree | grep -v 'pyc'
.
└── mooseyfate
    ├── Decisioner.py
    ├── hypothesis
    │   ├── BraveHypothesis.py
    │   ├── ChunkyWimpyHypothesis.py
    │   ├── Hypothesis.py
    │   ├── __init__.py
    │   ├── KMeansHypothesis.py
    │   ├── SimpleProbabilityHypothesis.py
    │   ├── WimpyHypothesis.py
    ├── __init__.py
    ├── lib
    │   ├── HelperFunctions.py
    │   ├── __init__.py
    │   ├── TestingEnvironment.py
    └── README.md

3 directories, 21 files

[~/workspace/lab/ml]$ python -m mooseyfate.hypothesis.KMeansHypothesis
```
