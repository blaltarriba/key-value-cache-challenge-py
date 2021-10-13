# Key Value Cache challenge

This project implements [challenge](https://github.com/blaltarriba/key-value-cache-challenge-py/tree/master/challenge-description/README.md) using Python3 with FastAPI.

## Installation

To build the project run:

    make build

To run the container run:

    make env-start

then the API will be ready at `http://localhost:8005/`

To stop the container run:

    make env-stop

## Testing

To execute test run:

    make test

## Operations

### Fetch and item

To fetch and item by its code, in terminal execute:

    curl -w "%{http_code}" --location --request GET 'http://localhost:8005/fetch/a_code'

to check how the item is fetched, check app logs running:

    make view-logs

For the first requests when the cache it's empty and the item must be fetched from the repository/database, the log should be:

    Stored in cache

For the next requests when item it's stored in the cache and must not be fetched from repository/database, the log should be: 

    Already in cache

The items are hardcoded in [here](https://github.com/blaltarriba/key-value-cache-challenge-py/blob/e7d06a30bacc44460de4854458b7ecf8644d2f27/src/routes.py#L9)
