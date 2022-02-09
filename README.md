# MOB-REST

## Usage

All responses will have the form
```json
{
  "data": "Content of the response"
}
```

### List All Objects

**Definition:**

`GET /objects`

**Response:**

- `200 OK` on success

```json
[
  {
    "id": 1,
    "name": "Object",
    "date+created": "MM-DD-YYYY"
  },
  {
    "id": 2,
    "name": "Object",
    "date+created": "MM-DD-YYYY"
  },
]
```

### Creating New Object

**Definition:**

`POST /objects`

**Arguments:**

- `"name":string` Object name

**Response:**

- `201 Created` on success

```json
{
  "id": 1,
  "name": "Object",
  "date+created": "MM-DD-YYYY"
}
```

### Get Object

**Definition:**

`GET /objects/:id`

**Response:**

-`404 Not Found` if the object does not exists
-`200 OK` on success

```json
{
  "id": 1,
  "name": "Object",
  "date+created": "MM-DD-YYYY"
}
```

### Delete Object

**Definition:**

`DELETE /objects/:id`

**Response:**

-`404 Not Found` if the object does not exists
-`200 OK` on success
