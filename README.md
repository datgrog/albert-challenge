curl http://localhost:8080/ping
poetry run task api

custom loggin for prod / dev
enable optimization for prod run task script
some global API error handling

"In production, I’d use a library like python-jcs or a canonicalization method defined by the spec (e.g., RFC 8785 for JSON signatures), but for this exercise, json.dumps(..., sort_keys=True, separators=(',', ':')) gives us deterministic output for signing."

openssl rand -base64 32

update better error message

provide curl command