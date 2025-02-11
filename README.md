# flask_starter
basic flask setup for new project


## Installation
### Making venv
```make venv```

### Assume venv
```	. .venv/bin/activate```

### Installing dependencies
```make install-deps```

### Creating DB file
```make create-db-file```

## Running
```make run```

## Development
### Dependencies
After assuming the virtualenv you can add a dependency via
```pip install $PACKAGENAME```

Once you have installed the package, you can add it to the project via:
```make save-deps```