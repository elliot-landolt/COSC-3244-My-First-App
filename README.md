# COSC-3244-My-First-App
In-Class My First App Exercise

## Setup

Create a virtual environment (first-time only):
```sh
conda create -n reports-env python=3.10
```

Activate the environment (whenever you come back):
```sh
conda activate reports-env
```

Install packages:
```sh
pip install -r requirements.txt
```



## Usage

run the unemployment report:

```sh
ALPHAVANTAGE_API_KEY ="..." python -m app.unemployment_report
```
