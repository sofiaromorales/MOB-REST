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
    "name": "Object",
    "date_created": "MM-DD-YYYY"
  },
  {
    "name": "Object",
    "date_created": "MM-DD-YYYY"
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
  "name": "Object",
  "date_created": "MM-DD-YYYY"
}
```

### Get Object

**Definition:**

`GET /objects/:name`

**Response:**

- `404 Not Found` if the object does not exists
- `200 OK` on success

```json
{
  "name": "Object",
  "date_created": "MM-DD-YYYY"
}
```

### Delete Object

**Definition:**

`DELETE /objects/:id`

**Response:**

- `404 Not Found` if the object does not exists
- `200 OK` on success

### Replicate Objects

**Definition:**

`POST /replicate`

**Arguments:**

- `"action":string` Commit || Abort

**Response:**

- `204 Replicated` on success

### Recover Objects

**Definition:**

`GET /recover`

**Response:**

- `200 OK` on success
