# Docker_compose

Cache implementation using redis. Gets the data from the cache if it exists, otherwise it gets it from the API/database and stores it in the cache.

``` url: http://127.0.0.1:5000/universities?country=Nepal ```

Returns a list of universities in specified country.
