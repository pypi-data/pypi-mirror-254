# **loom**anager 📦
The new version manager based on zenyxvm.
Features:
- Version handling
- Commiting to git
- Publishing to PyPi

## Install
Install the module from [PyPi](https://pypi.org/project/loomanager/):
```bash 
python -m pip install loomanager
```

## How to use?
loomanager has many features, let's go over them.
### New Project 📰
To setup loomanager in a new project, run the following:
```bash
python -m loomanager new --bat
```
This will create the `loom.toml` and `loom.bat` files.
To run the package, you can do:
```bash
./loom <command>
```

### Update ♻️
Collect the latest version of `loomanager`
```bash
./loom update
```

### Publish 🛠️
This is the main command. Configure your publish types in the `loom.toml` file, and run the command.
```bash
./loom publish
```