# You want to keep a limited history of the last few items seen during iteration
# or during some other kind of processing.

from collections import deque

def _generate_file(name: str):
    with open(name, 'w') as file_object:
        file_object.write('a\nb\nc\n1.python3\nd\ne\n2.python 3\n')

def search(lines, pattern: str, history: int):
    previous_lines_ = deque(maxlen=history)
    for line_ in lines:
        if pattern in line_:
            yield line_, previous_lines_
        previous_lines_.append(line_)

# Example use on a file
if __name__ == '__main__':
    file_name = 'keeping_last_n_items_some_file.txt'
    _generate_file(file_name)
    with open(file_name) as f:
        for line, previous_lines in search(f, 'python', 2):
            for p_line in previous_lines:
                print(p_line, end='')
            print(line, end='')
            print('-'*20)
