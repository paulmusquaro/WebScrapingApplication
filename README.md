# Web Scraping Application

The program collects quotes and data about their authors directly from the site http://quotes.toscrape.com, and uploads the received data to the MongoDB database. The application uses Redis to cache search results to improve the performance of subsequent searches. This application provides an interface to search for authors and quotes in a database. 


## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.11 or above.
- You have installed MongoDB and it's running on the default port.
- You have installed Redis and it's running on the default port.
- You have installed Scrapy.
- You have installed Poetry.

## Installing & Using Web Scraping Application

1. Run Docker Engine via opening Docker Desktop.
2. Activate Virtual Environment:
    ```
    poetry shell
    ```
3. Create Docker Container (Redis)
    ```
    docker-compose -f docker-compose.yaml up --force-recreate
    ```
4. Run the main script:
    ```
    python main.py
    ```
    When prompted, enter the command `run` or `run spider` to find information about new quotes and their authors, then enter `exit`

5. Upload data on DB:
   ```
   python seeds.py
   ```


6. Then run `main.py` anew and input your search command followed by a colon and the search term. For example:
    - To search for an author named "Steve Martin", enter: `name:Steve Martin`
    - To search for quotes with the tag "life", enter: `tag:life`

    If you want to perform a search with a partial term, you can use:
    - `name:st` for authors with names starting with "st"
    - `tag:li` for tags starting with "li"

The search results will be displayed in the console. If the results have been cached, subsequent searches with the same term will be faster.

To exit the application, type `exit`.

## Database Structure

The application utilizes MongoDB for data storage and consists of two main collections: `authors` and `quotes`.

### Authors Collection

This collection stores details about authors. Each document in the `authors` collection has the following structure:

- `fullname`: The full name of the author.
- `born_date`: The date of birth of the author.
- `born_location`: The place of birth of the author.
- `description`: A short biography of the author.

Example document fom db:

```json
{
  "fullname": "Albert Einstein",
  "born_date": "March 14, 1879",
  "born_location": "in Ulm, Germany",
  "description": "A detailed biography of Albert Einstein..."
}
```

### Quotes Collection

This collection contains the quotes from various authors. Each quote is linked to an author from the `authors` collection via a `ReferenceField`. Each document in the `quotes` collection has the following structure:

- `tags`: An array of tags relevant to the quote.
- `author`: A reference to an author document in the `authors` collection.
- `quote`: The textual content of the quote.

Example document for db:
```json
{
  "tags": ["inspirational", "life"],
  "author": "Albert Einstein",
  "quote": "Life is like riding a bicycle. To keep your balance, you must keep moving."
}
```

### Indexing
For performance optimization, especially for search operations, the following fields are indexed:

- `authors.fullname`: To quickly search authors by their name.
- `quotes.tags`: To allow fast searching of quotes by their associated tags.


### Caching with Redis
Redis is used as an in-memory data store to cache the search results. It stores the results of queries made to the `authors` and `quotes` collections so that subsequent searches can be served from the cache, which is significantly faster than querying the database again.