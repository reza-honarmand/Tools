import re

def extract_comments(input_file, output_file):
    with open(input_file, 'r') as python_file, open(output_file, 'w') as text_file:
        in_comment_block = False

        for line in python_file:
            # Check for multi-line comments (""" or ''')
            if re.match(r'^\s*("""|\'\'\')', line):
                in_comment_block = not in_comment_block
                if in_comment_block:
                    continue

            # Check for single-line comments (#)
            if not in_comment_block and line.lstrip().startswith('#'):
                text_file.write(line.lstrip('#').strip() + '\n')

# Example usage
input_file = 'your_python_file.py'
output_file = 'comments.txt'
extract_comments(input_file, output_file)
