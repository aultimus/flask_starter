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
```	poetry shell```

```make run-local```

## Development
### Dependencies
To add a package use:
```poetry add $PACKAGENAME```


## TODO
Sending passwords over non TLS connections is bad, this should not be done in
production.