[![CodeQL](https://github.com/kirajano/cwe-89-mock/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/kirajano/cwe-89-mock/actions/workflows/codeql-analysis.yml)

## CWE-89

Mock scenario to exploit SQL injection

How to run?

```
docker build --no-cache -t cwe89-demo .
docker run --rm -p 5001:5000 cwe89-demo
```
Go to localhost:5001 in browser and exploit to get all passwords
