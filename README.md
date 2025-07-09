[![CI](https://github.com/datgrog/albert-challenge/actions/workflows/ci.yaml/badge.svg)](https://github.com/datgrog/albert-challenge/actions/workflows/ci.yaml)

# 🔐 Albert Home Challenge

A small Python API for secure JSON encryption and digital signature verification.

Built with:

- **Flask** for simplicity
- **Poetry** for Dependency Management and locking deps
- **Gunicorn** for web serving
- **Taskipy** for dev ergonomics
- .env for *albert* secret 👨‍🦳🤐
- **Black**, **Ruff**, **Mypy**, and 🧪 **Pytest** for code quality (Prettifier, Linter, Static Type Checking and testing)
- Add Github actions for CI (Lint, Format, Test)

## Getting Started

### Using Docker

> Require `ALBERT_HMAC_SECRET` in .env
>

```bash
# 💡 Tips
openssl rand -base64 32
# rename `.env.example` to `.env`
# set `ALBERT_HMAC_SECRET` with openssl previous command
```

Build: `docker build -t albert_challenge .`

Run and start API: `docker run --rm -it -p 8080:8080 albert_challenge bash`

then
```bash
poetry run task api
poetry run task test
```

### Prerequisites

> Requires Python 3.10+
> 

```bash
# Install Python 3.10 with pyenv
brew install pyenv
pyenv install 3.10
pyenv local 3.10
```

> Requires Poetry
> 

```bash
# Install Poetry
curl -sSL <https://install.python-poetry.org> | python3
```

> Require `ALBERT_HMAC_SECRET` in .env
> 

```bash
# 💡 Tips
openssl rand -base64 32
# rename `.env.example` to `.env`
# set `ALBERT_HMAC_SECRET` with openssl previous command
```

### Installation

```bash
# Install project dependencies
poetry install
```

## Commands

### API

```bash
poetry run task api # Start the API
```

Or, enter the dev shell first:

```bash
poetry shell
task api
# ... as above
```

API is now running on: [http://localhost:8080](http://localhost:8080/)

### Dev Commands

```bash
poetry run task test
poetry run task lint
poetry run task format

# or

poetry shell
task test
task lint
task format
```

## 🔁 Endpoints

### 🔐 Encrypt `/v0/crypto/encrypt`

```bash
curl -X POST http://localhost:8080/v0/crypto/encrypt \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Albert",
    "age": 999,
    "contact": {
      "email": "hello@albert.com",
      "phone": "+1-800-ALBERT-42"
    }
  }'
```

### 🔓 Decrypt `/v0/crypto/decrypt`

```bash
curl -X POST http://localhost:8080/v0/crypto/decrypt \
  -H "Content-Type: application/json" \
  -d '{
    "name": "IkFsYmVydCI=",
    "age": "OTk5",
    "contact": "eyJlbWFpbCI6ICJoZWxsb0BhbGJlcnQuY29tIiwgInBob25lIjogIisxLTgwMC1BTEJFUlQtNDIifQ=="
  }'

```

### ✍️ Sign `/v0/crypto/sign`

```bash
curl -X POST http://localhost:8080/v0/crypto/sign \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Albert",
    "age": 999,
    "contact": {
      "email": "hello@albert.com",
      "phone": "+1-800-ALBERT-42"
    }
  }'

```

### ✅ Verify `/v0/crypto/verify`

```bash
curl -X POST http://localhost:8080/v0/crypto/verify \
  -H "Content-Type: application/json" \
  -d '{
    "signature": "9344b6a38aae164f66752747d997add35f0691f6e2207326afd99be74f8c0ae2",
    "data": {
      "name": "Albert",
      "age": 999,
      "contact": {
        "email": "hello@albert.com",
        "phone": "+1-800-ALBERT-42"
      }
    }
  }'

```

## 📁 Project Structure

```
.
├── poetry.lock                # Locked dependency versions
├── pyproject.toml             # Project and dependency configuration
├── pytest.ini                 # Pytest configuration
├── README.md                  # Project documentation
├── src/
│   ├── app.py                 # Flask app entrypoint
│   ├── crypto/                
│   │   ├── __init__.py
│   │   ├── crypto_service.py  # Abstraction layer to switch encoder/signer
│   │   ├── encoder/
│   │   │   ├── __init__.py
│   │   │   ├── base64_encoder.py # Encoder current impl
│   │   │   └── encoder.py     # Encoder interface
│   │   └── signer/
│   │       ├── __init__.py
│   │       ├── hmac_signer.py # Signer current impl
│   │       └── signer.py      # Signer interface
│   ├── exceptions.py          # Custom exception classes
│   └── routes/
│       ├── encode.py          # Encryption/decryption endpoints
│       └── sign.py            # Signing/verification endpoints
└── tests/                     # Test suite
    ├── test_api_error.py
    ├── test_decrypt.py
    ├── test_encrypt.py
    ├── test_sign.py
    └── test_verify.py
```
