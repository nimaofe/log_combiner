import re
from datetime import datetime

def parse_mysql_log(line):
    # Adjust the pattern to match your MySQL log format
    match = re.match(r'(\d{6} \d{2}:\d{2}:\d{2})\s+([^\s]+)\s+(.*)', line)
    if match:
        timestamp = datetime.strptime(match.group(1), '%y%m%d %H:%M:%S')
        query = match.group(3)
        return timestamp, query
    return None

def parse_iis_log(line):
    # Adjust the pattern to match your IIS log format
    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(.*)', line)
    if match:
        timestamp = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')
        entry = match.group(2)
        return timestamp, entry
    return None

def combine_logs(mysql_log_path, iis_log_path, output_path):
    with open(mysql_log_path, 'r') as mysql_file, open(iis_log_path, 'r') as iis_file, open(output_path, 'w') as output_file:
        mysql_lines = mysql_file.readlines()
        iis_lines = iis_file.readlines()
        
        logs = []
        for line in mysql_lines:
            parsed = parse_mysql_log(line)
            if parsed:
                logs.append(('MySQL', *parsed))
        
        for line in iis_lines:
            parsed = parse_iis_log(line)
            if parsed:
                logs.append(('IIS', *parsed))
        
        logs.sort(key=lambda x: x[1])  # Sort logs by timestamp
        
        for log in logs:
            output_file.write(f'[{log[0]}] {log[1]}: {log[2]}\n')
