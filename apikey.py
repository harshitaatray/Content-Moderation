apikey = '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'

import re

def process_large_responses(filename):
    large_response_count = 0
    total_large_bytes = 0

    pattern = re.compile(r'(\d+)$')

    with open(filename, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                response_size = int(match.group(1))
                if response size > 5000:
                    large_response_count += 1
                    total_large_bytes += response_size

    output_filename = "bytes_" + filename
    with open(output_filename, 'w') as file:
        file.write(str(large_response_count) + "\n" )
        file.write(str(total_large_bytes) + "\n")
        
    return output_filename