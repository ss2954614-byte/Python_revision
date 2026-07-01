def dataset_summary(rows, columns):
    return {
        "Rows": rows,
        "Columns": columns
    }


def missing_percentage(missing_values, total_values):
    return round(
        (missing_values / total_values) * 100,
        2
    )