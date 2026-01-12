def process_pipeline(records):
    valid = [r for r in records if is_valid_record(r)]
    names = extract_column(valid, "name")
    return uppercase_all(names)
