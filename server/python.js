fetch('http://localhost:8000/api/unique_number/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      unique_number: '4',
      unique_number_count_id: 'some_existing_id'
    }),
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
  