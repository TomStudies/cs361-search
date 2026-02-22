# cs361 (Group 17) - Small Pool Microservice: Search

**What does this microservice do?**

This microservice allows the user to search a list of objects for a string term. The service returns a list containing the same objects as was provided to it, but sorted based on the following priorities:

1. Any object containing a value exactly matching the search string is sorted to the top of the list.
2. Any object containing a value with a partial substring match is sorted to come after the exact matches. Longer partial substring matches come first (e.g. a 3 character substring match will come higher in the list than a 2 character substring match.)
3. Any object containing no values with even single character partial substring matches to the search term will be at the bottom of the list.

Note that matches are not case sensitive.

**How do I request data from this microservice?**

To request data from the microservice, you need to make an `HTTP POST reuqest` to the `/search` endpoint followed by the `search_term`.

The body of this POST request should contain a JSON list of objects to be searched.

_Example call:_ `POST http://127.0.0.1:8000/search/cat`

JSON body:
```yaml
[
  {"name": "Martin", "species": "fish"},
  {"name": "Carlos", "species": "dog"},
  {"name": "Fred", "species": "cat"},
  {"name": "Friend", "species": "fish"}
]
```

**How will I receive data from this microservice?**

The microservice returns a `JSON object`. This object contains a list of objects that have been sorted based on matches found.

_Example response_:

Status code: `200`
```yaml
[
  {
    "name": "Fred",
    "species": "cat"
  },
  {
    "name": "Carlos",
    "species": "dog"
  },
  {
    "name": "Martin",
    "species": "fish"
  },
  {
    "name": "Friend",
    "species": "fish"
  }
]
```

**UML Sequence Diagram**

![UML Diagram](/assets/diagram.png?raw=true "UML Diagram")

**How to test this service locally?**
+ Install dependencies: `pip install fastapi uvicorn requests`
+ Run the microservice from within the app folder: `uvicorn main:app --reload`
+ Run the tests: `python test_api.py`