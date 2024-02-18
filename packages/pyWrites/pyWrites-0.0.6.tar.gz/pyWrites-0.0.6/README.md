## pyWrites
- What is pyWrites? pyWrites is an package for Python, that lets you write, read and delete files with just some simple code!
- For what do you need pyWrites? With pyWrites you can improve your coding speed very easily.
- What will come in the future? pyWrites will get Multiple updates such as an ezEncrypt and ezDecrypt. 

# Stay Tuned!

## Changelogs:
- added pyJson 
- fixed some bugs with init file

# Installation

```python
pip install pyWrites
```

## Examples of pyWrites

Write to a file:
```python
from pyWrites import write_file
#Syntax: write_file(filename, content, path)
write_file('hello.txt', 'Hello World!')
```

Adding a path:
```python
from pyWrites import write_file
#Syntax: write_file(filename, content, path)
write_file('hello.txt', 'Hello World', 'C:\\Users\\User\\Desktop')
```

Append to a file:
```python
from pyWrites import append_file
#Syntax: append_file(filename, content, path)
append_file('hello.txt', 'Hello World')
```

Read file:
```python
from pyWrites import read_file
#Syntax: read_file(filename, path, line)
output = read_file('hello.txt', 'C:\\Users\\User\\Desktop')
print(output)
```

Read specific line of file:
```python
from pyWrites import read_file
#Syntax: read_file(filename, path, line)
output = read_file('hello.txt', 'C:\\Users\\User\\Desktop', 1)
print(output)
```

Read multiple lines:
```python
from pyWrites import read_lines
#Syntax: read_lines(filename, path, fromLine, toLine)
output = read_lines('hello.txt', 'C:\\Users\\User\\Desktop', 1, 5)
print(output)
```

Delete a File:
```python
from pyWrites import deleteFile
#Syntax: deleteFile(filename, path)
deleteFile('hello.txt', 'C:\\Users\\User\\Desktop')
```
## Examples of pyJson

Write to a file:
```python
from pyWrites import write_json
#Syntax: write_json(filename: str, content: str, path: str, sort_keys: bool)
write_json('hello', '{"hello": "world!"}', sort_keys=False)
```

Read from a json file:
```python
from pyWrites import read_data
#Syntax: read_data(filename: str, key: str, path: str)
output = read_data('hello', 'hello')
print(output) #>>> world!
```
```python
from pyWrites import read_dataset
#Syntax: read_dataset(filename: str, dataset: str, path: str)
output = read_dataset('hello', 'hello')
print(output) #>>> {"hello": "world!", "how": "are you?"}!
```
```python
from pyWrites import read_whole_file
#Syntax: read_whole_file(filename: str, path: str)
output = read_whole_file('hello')
print(output) #>>> ["helloworld":{"hello": "world!", "how": "are you?"}]!
```

Delete from json file:
```python
from pyWrites import delete_data
#Syntax: delete_data(filename: str, key: str, path: str)
delete_data('hello', 'hello')
```