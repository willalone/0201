def read_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    records = []
    for line in lines:
        if line.strip() and not line.startswith("#"):
            parts = line.strip().split(";")
            records.append({
                'reader': parts[0],
                'book': parts[1],
                'issue_date': parts[2],
                'return_date': parts[3]
            })
    return records

def write_data(filename, records):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# ReaderName;BookTitle;IssueDate;ReturnDate\n")
        for rec in records:
            line = f"{rec['reader']};{rec['book']};{rec['issue_date']};{rec['return_date']}\n"
            f.write(line)
