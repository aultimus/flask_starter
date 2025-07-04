# flask_starter
basic flask setup for new project


## Installation
### Installing tools
#### Poetry
```curl -sSL https://install.python-poetry.org | python3 -```

```poetry self add poetry-plugin-shell```


### Creating DB file
```make create-db-file```

## Running in Docker
```make run`

### Running outside of Docker
```eval $(poetry env activate)```

```make run-local```

## Development
### Dependencies
To add a package use:
```poetry add $PACKAGENAME```


## TODO
- Sending passwords over non TLS connections is bad, this should not be done in
production.
- Add running under debugger support
- Replace SQLLite with mysql database
- Add stubs for unit, integration and system tests
- Add env variable parsing