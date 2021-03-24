# Installation

### Globally
Installing globally is recommended, as it allows you to use runscript on any directories.

**Via pip**
```bash
pip3 install sprintscript
```

**Via homebrew**
```bash
brew install sprintscript
```

### In directory
You can install runscript into a directory to add it as a dependency or to make scripts available to those who don't have sprintscript installed (for some odd reason).

```bash
git clone https://github.com:gadhagod/sprintscript --branch <version>
```

Then you can run sprintscript with `./sprintscript/bin/run`.
Since this is not the most elegant solution, installing globally is recommended.

## Installing development build
Installing the development build is primarily for contributing to sprintscript, as it can be unstable.

```bash
pip3 install git+https://github.com:gadhagod/sprintscript
```