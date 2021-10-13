# Key-Value Cache challenge

Implement a key value cache to speed up the retrieval of information. The cache is a proxy that sits between the client and an upstream data source. Clients access values only via the cache. For example, a CDN is a cache that implements this paradigm: a CDN sits between a browser (client) and a website (upstream data source) and returns either cached items or 'fresh' ones.

**Requirements:**

- Implement a library, not a client/server application.
- The Cache should provide a single method to retrieve a cached object or a fresh one
- Write unit tests to validate your implementation
- Immutability: mutation of retrieved values should not mutate cached or upstream values
