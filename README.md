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

[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Create a ".env" file and add contents like the following (using your own AlphaVantage API key):
```sh
#this is the ".env" file
ALPHAVANTAGE_API_KEY="..."

# optionally:
SENDGRID_API_KEY="..."
SENDGRID_SENDER_ADDRESS="..."
```

## Usage

Run the unemployment report:

```sh
python -m app.unemployment_report
```

Run the stocks report:
```sh
python -m app.stocks_report
```

Run the email service:
```sh
python -m app.email_service
```

## Testing

Run tests:
```sh
pytest
```