This package contains built-in tasks for docop.

### fetch_html

Fetch and store HTML from source URLs.

Expects input source with a set of resources (URLs) to fetch
Output document fields set:
    - 'reference' to the URL
    - 'type' to "html"
    - 'title' and 'html' set to the fetched HTML title & rendered HTML content
    - 'uuid' generated from the URL
    - 'modified' field set to Last-Modified header value

