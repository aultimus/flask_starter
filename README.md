# flask_starter
basic flask setup for new project


## Development
#### Poetry
```curl -sSL https://install.python-poetry.org | python3 -```

```poetry self add poetry-plugin-shell```

### Dependencies
To add a package use:
```poetry add $PACKAGENAME```

### Creating DB file
```make create-db-file```

## Running in Docker
```make run`

### Running outside of Docker
```eval $(poetry env activate)```

```make run-local```

### Running in the Debugger (VS Code)

We recommend the following VS Code extensions:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) 

1. Standup the database. TODO
2. Open the project folder in VS Code.
3. Go to the Run and Debug panel (play icon in the sidebar).
4. Select "Python: Debugger Flask" from the dropdown.
5. Click the green "Run" button or press F5.
6. Set breakpoints in your Python files as needed.

## TODO
- Sending passwords over non TLS connections is bad, this should not be done in
production.
- Replace SQLLite with mysql database
- Add stubs for unit, integration and system tests
- Add env variable parsing