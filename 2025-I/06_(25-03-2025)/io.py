# # Reading a writing files
# To manipulate a file, we too first open it using the `open` built-in function. When called, the class returns an 

# | Parameter | Description |
# |-----------|-------------|
# | `file`    | The path and name of the file |
# | `mode`    | A string defining the file opening mode (see below) |
#
# ### File Modes
# | Mode | Name    | Description |
# |------|---------|-------------|
# | `"r"` | Read    | Default value. Opens a file for reading, error if the file does not exist |
# | `"a"` | Append  | Opens a file for appending, creates the file if it does not exist |
# | `"w"` | Write   | Opens a file for writing, creates the file if it does not exist |
# | `"x"` | Create  | Creates the specified file, returns an error if the file exists |
#
# ### File Types
# | Mode | Name    | Description |
# |------|---------|-------------|
# | `"t"` | Text    | Default value. Text mode |
# | `"b"` | Binary  | Binary mode (e.g. images) |

# ### Reading

a  = open('example.txt','r')
type(a)

# We can read one by one
for i in range(20):
    print(a.read(2))

# Or we can read all at once
a  = open('example.txt','r')
print(a.read())

# Or we can read line by line
a  = open('example.txt','r')
for i in a.readlines():
    print("line:",i)
a.close()

# We always need to close the file to avoid undesidred behavior
a  = open('example.txt','r')
for i in range(300): 
    print(a.read(1))


# +
# Let's read bytes
a  = open('luxembourg.png','br')
print(a.read(1))
print(a.read(3))
print(a.read(2))
print(a.read(1))
print(a.read(1))
for _ in range(100):
    print(a.read(1))



a.close()

# -
from rich import print
import yaml
a = open('parameters.yaml','r')
content = a.read()
a.close()
data = yaml.safe_load(content)
print(data)

# reading files in different formats: yaml file
import yaml
with open('parameters.yaml', 'r') as f:
    parameters = yaml.safe_load(f.read())
print(parameters)


# reading files in different formats: csv file
import csv
with open('data.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    my_data = list(reader)

my_data

# ### Writing

my_message="\nThis is a test\nthis is the best test\nthis test is over"
print(my_message)

a = open('example_2.txt','w')
a.write(my_message)
a.close() # What happens if we don't close the file?

# Now in append mode
for i in range(10):
    a = open('example_2.txt','a')
    a.write(my_message)
    a.close()



# # File paths

# In python, we can access a file from the operating system through a file path. This is a string that represents the location of a file.
#
#     It offers an OOP way of handling paths instead of the older os.path functions.
#
#     Automatically manages path separators across different OS (Windows, Linux, macOS)
#
#     Includes handy methods for performing common path-related tasks

# +
from pathlib import Path

p = Path('example.txt')

abs_path = p.absolute()

if p.exists():
    print("File exists!")
# -

abs_path

p = Path('this/is/a/nested')


p.mkdir(
    parents=True,
    exist_ok=True
    )

p = Path('example.txt')
p.parent.parent

p.parent.parent

# These are the most useful:
#
# | Method | Description | Example |
# |--------|-------------|---------|
# | `.exists()` | Check if path exists | `Path('file.txt').exists()` |
# | `.is_file()` | Check if path is a file | `Path('file.txt').is_file()` |
# | `.is_dir()` | Check if path is a directory | `Path('folder').is_dir()` |
# | `.mkdir()` | Create directory | `Path('new_folder').mkdir()` |
# | `.rename()` | Rename file/directory | `Path('old.txt').rename('new.txt')` |
# | `.unlink()` | Delete file | `Path('file.txt').unlink()` |
# | `.glob()` | Find files matching pattern | `Path('.').glob('*.py')` |
# | `.rglob()` | Recursive glob | `Path('.').rglob('**/*.py')` |
# | `.absolute()` | Get absolute path | `Path('file.txt').absolute()` |
# | `.resolve()` | Resolve symbolic links | `Path('link').resolve()` |
# | `.parent` | Get parent directory | `Path('a/b/c.txt').parent` |
# | `.name` | Get filename with extension | `Path('a/b/c.txt').name` |
# | `.stem` | Get filename without extension | `Path('a/b/c.txt').stem` |
# | `.suffix` | Get file extension | `Path('a/b/c.txt').suffix` |
# | `.with_suffix()` | Change file extension | `Path('file.txt').with_suffix('.csv')` |
# | `.with_name()` | Change filename | `Path('file.txt').with_name('new.txt')` |
# | `.read_text()` | Read file as text | `Path('file.txt').read_text()` |
# | `.write_text()` | Write text to file | `Path('file.txt').write_text('content')` |
# | `.read_bytes()` | Read file as bytes | `Path('file.txt').read_bytes()` |
# | `.write_bytes()` | Write bytes to file | `Path('file.txt').write_bytes(b'content')` |
# | `.touch()` | Create empty file | `Path('new.txt').touch()` |
# | `.iterdir()` | List directory contents | `[p for p in Path('.').iterdir()]` |
# | `.joinpath()` | Join paths | `Path('a').joinpath('b', 'c.txt')` |
#


