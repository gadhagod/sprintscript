# What is sprintscript?
*sprintscript* is a command line utility that simplifies repetitive commands for any kind of scripting. 

### A simple use case
Let's say, you are collaborating with a team of developers, and you want them to easily be able to setup their enviroment and run a script. You would usually have to keep it all in a README or something similar, like this:

    To install the requirements, run `pip3 install -r ./main/reqs.txt`.
    To export the enviroment variables run `cat conf/env-vars.sh >> .bashrc`.
    To convert to a zip file run `scripts/build.sh main.py`.
    To open the ZIP run `open dist/project.zip`.

This is hard to read and quite disorganized. One would have to keep returning to this file, look for the section and copy all the commands into their terminal.

However, with `sprintscript`, you can now easily configure this into a repo or directory.
To have the same commands above run easily, you would be able to place this into a configuration file in the same directory, called `scripts.json`:
```json
{
    "install": {
        "brew": "brew install mypackage mysecondpackage",
        "pip": "pip3 install -r ./main/reqs.txt"
    },
    "env-setup": "cat conf/env-vars.sh >> .bashrc",
    "build": "sh scripts/build.sh $1",
    "test": "open dist/project.zip"
}
```
You can execute any of these scripts conviniently from your command line now:
```bash
run install <command> <subcommands> <arguments>
```

So if you wanted to run the commands, you could do the following from the right directory:

```txt
run install pip      # install from pip
#run install brew    # alternatively, install from brew
run env-setup        # env var setup
run build "main.py"  # zip file building
run test             # open zip file
```

If you check the configuration file into you repo, your team can now run these commands with ease and memory.
The source of these commands can also be read easily from the neat configuration file.

### Differences from NPM scripts
This project was inspired by NPM scripts, but have some major enhancements.

1. Nested commands. You can add subcommands to commands from your configuration file like the following:
    
```json
{
    "install": {
        "backend": {
            "brew": "brew install mypackage",
            "pip": "pip3 install mypackage",
        },
        "frontend": {
            "npm": "npm i bootstrap",
            "cdn": "./scripts/add-cdn.sh" 
        }
    }
}
```

2. Made for all kinds of scripting. NPM scripts are primarily made for node projects only. Commands like `npm install` only can install from `package.json`, whereas with sprintscript you can run whatever you want.

3. Easily readable. Let's be honest: reading NPM scripts are hard. Take [electron's scripts](https://github.com/electron/electron/blob/master/package.json#L79), for example. With a configuration file JUST for the diffrent scripts in your project, things are much easier to read. In addition, [command lists](adding-scripts?id=command-lists) makes command with many steps MUCH easier to read.