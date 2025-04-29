# flask-jwt-decorator
This library offers a decorator to protect Flask routes with JWT authentication. The token_required decorator checks for a valid JWT, parses and validates it, and injects the payload into the request context.

# Usage example
The token_required decorator can be applied to any Flask route to ensure that requests include a valid JWT token.

```
@app.route("/protected")
@token_required()  # Protect the route with the decorator
def protected():
    ...
```

The token_required decorator lets you customize JWT parsing, validation, and payload injection by providing custom classes. By default, it uses DefaultJWTParser, DefaultJWTValidator, and DefaultPayloadInjector, but you can replace them by passing your own classes as arguments.

```
@app.route("/protected")
@token_required(
    parser=CustomJWTParser(),
    validator=CustomJWTValidator(),
    payload_injector=CustomPayloadInjector()
)
def protected():
    ...
```


# DefaultJWTParser
The DefaultJWTParser class looks for certain configuration values in the Flask application's configuration. These values are required only if you're using the DefaultJWTParser.

- JWT_SECRET_KEY
- JWT_ALGORITHMS

```
class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

app = Flask(__name__)

app.config.from_object(Config)
```
