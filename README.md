# blossom_filter

Short Explanation:
Model:
BlossomFilter: A Bloom filter that uses a bit array and multiple hash functions to store and check for the existence of unique numbers.
UniqueNumberCount: A model that tracks how many times a unique number has been added. It increments the count each time.
BlossomFilterRecord: A model that links each UniqueNumberCount to its associated Bloom filter (serializing and deserializing the filter).

Execution:
POST Request to /unique_number:
If it’s the first time adding a number, it creates a new UniqueNumberCount and a corresponding BlossomFilterRecord.
Adds the unique_number to the Bloom filter and increments the count.
Returns the unique_number_count and unique_number_count_id.

POST Request to /check_number_in_filter:
Checks if a unique_number exists in the filter using the provided unique_number_count_id.
Returns True if the number exists, False otherwise, or an error if the ID is invalid.



This code efficiently manages sets of unique numbers using Bloom filters and tracks their occurrences using Django models.


### Endpoints BACKEND

  #### **POST** 'http://127.0.0.1:8000/api/unique_number/' 
  **Body**

       ```
       {
        "unique_number": "9"
       }
       ```
  - When making your first request, simply provide the unique_number to the backend. The backend will generate a unique_number_count_id and return it to you. For subsequent POST requests, you must include the unique_number_count_id so the backend can add and verify the number in the same Blossom filter list.
  
  #### **POST** 'http://127.0.0.1:8000/api/check_number/' 
  - You need to pass unique_number and unique_number_count_id to the backend. The backend will respond by indicating whether the unique_number exists in the list or not.
  
  **Body**

  ```bash
  {
  "unique_number": "7",
  "unique_number_count_id": 1
  }

  ```


