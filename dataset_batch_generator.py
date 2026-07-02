def dataset_batches(records, batch_size):
    for start in range(0, len(records), batch_size):
        yield records[start:start + batch_size]


students = list(range(1, 21))

for batch in dataset_batches(students, 5):
    print(batch)