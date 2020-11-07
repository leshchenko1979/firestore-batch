# firestore-batch
A Python context manager for easy Google Forestore batched writes.

# What it does for you
- Creates a new batch on entering.
- Takes care of the 500-operation limit. When the limit is hit, it commits accumulated operations to the database and creates a new batch.
- Commits all operations on exit.

# Usage
Install with pip:
```
pip install firestore-batch
```

Use in your code:
```python
# Initialize the app
from firebase_admin import initialize_app, firestore
initialize_app()
db = firestore.client()

# Make lots of batched writes
from firestore_batch import Batch

with Batch(db) as batch:
    for i in range(1000):
        batch.set(doc_ref, {f'property_{i}': f'value_{i}'})
```

# Methods
- `set()`, `update()`, `delete()` - as in the original `WriteBatch` class (see [the documentation with usage examples](https://firebase.google.com/docs/firestore/manage-data/transactions?hl=en#batched-writes) and API Reference for the [`WriteBatch`](https://googleapis.dev/python/firestore/latest/batch.html) and [`DocumentReference`](https://googleapis.dev/python/firestore/latest/document.html) classes).