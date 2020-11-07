class Batch:
    def __init__(self, db):
        self._db = db


    def __enter__(self):
        self._new_batch()
        return self


    def __exit__(self, a1, a2, a3):
        if self._operations_queued > 0:
            self._batch.commit()


    def _register_new_operation(self):
        self._operations_queued += 1
        if self._operations_queued >= 500:
            self._batch.commit()
            self._new_batch()


    def _new_batch(self):
        self._batch = self._db.batch()
        self._operations_queued = 0


    def set(self, *args, **kwargs):
        self._batch.set(*args, **kwargs)
        self._register_new_operation()


    def delete(self, *args, **kwargs):
        self._batch.delete(*args, **kwargs)
        self._register_new_operation()


    def update(self, *args, **kwargs):
        self._batch.update(*args, **kwargs)
        self._register_new_operation()