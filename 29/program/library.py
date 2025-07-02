from file_manager import read_data, write_data

def add_record(filename, reader, book, issue_date, return_date):
    records = read_data(filename)
    records.append({
        'reader': reader,
        'book': book,
        'issue_date': issue_date,
        'return_date': return_date
    })
    write_data(filename, records)

def return_book(filename, reader, book):
    records = read_data(filename)
    records = [r for r in records if not (r['reader'] == reader and r['book'] == book)]
    write_data(filename, records)
