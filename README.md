# Organizer

This is a small Python project that organizes all files in a folder into subfolders based on their extensions. I always had a mess with files in my Download directory. Now I just have to run *main.py* and files will be sorted into subfolders according to their file types.


## Usage

Download the repository and place it in the desired directory. **It will organize the parent (../) directory**
```
Parent Directory
└───   organizer
│   │   __init__.py
│   │   main.py
│   │   handler.py
│   file1.jpg
│   file2.pdf
│   ...
```

Now, open a terminal in the organizer directory and run:
```bash
python main.py
```

## How to change
### Directory name
To change a directory name, modify the value in the *type_to_directory_name* to the desired value. For example:
```python
type_to_directory_name = {
    'text': 'Texts',
}
```
can be changed to:
```python
type_to_directory_name = {
    'text': 'NewText',
}
```
### Add new extension
To add a new extension, edit *extension_to_handler* in *FileHandlerDispatcher*: 
```python
self.extension_to_handler = {
            ...
            'stl': '3d'
        }
```
And add the corresponding folder name:
```python
type_to_directory_name = {
    '3d': '3D Files',
}
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)