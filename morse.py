import random
import string
from datetime import datetime

date = datetime.now().strftime('%Y-%m-%d')
filename = f'{date}.txt'

def generate_random_file(filename, group=1, total=50):
    with open(filename, 'w') as f:
        for _ in range(total):
            # Create a group of characters
            char_group = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(group))

            # Write the group and a space to the file
            f.write(char_group + ' ')

# Use the function with the default group size
generate_random_file(filename, 1, 50)


