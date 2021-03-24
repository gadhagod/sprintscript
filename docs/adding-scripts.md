# Adding scripts

### The basics
To configure scripts, create a `scripts.json` file.
Each key in the JSON file stands as it's own command or command category.
To add a simple script that prints "hello world" on the "hello" command, add the following to `scripts.json`:

```json
{
    "hello": "echo 'hello world'"
}
```

For complex scripts, creating files for them are recommended.

```bash
# scripts/hello.sh
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' - # print a horizontal a line
echo "hello world"
```

```json
{
    "hello": "sh scripts/hello.sh"
}
```

### Command categories
You can create command categories by adding a JSON object as a key's value. 
For example:

```json
{
    "foo": {
        "bar": "echo 'foo bar'",
        "baz": {
            "bam": "echo 'foo baz bam'"
        }
    }
}
```

You could run `echo 'foo baz bam'` with `run foo baz bam`. How simple!

### Command line arguments
You can pass command line arguments by adding `[]` before your last argument of the `run` call.
For example, let's say you have a script called `alert`, that takes an argument and print's that argument in read.
```json
{
    "alert": "./scripts/alert.sh"
}
```
```bash
# scripts/alert.sh
printf "\033[0;31mError: $1 \n\033[0m"
exit 1
```

You can call the script with the argument as "File not found" with the following:

```bash
run alert "File not found"
```

This will have the following output (in red):

```text
Error: File not found
```

### Command lists
Sprintscript is built to be readable. Command lists makes commands with multiple steps easier.
Consider the following:
```json
{
    "hi-bye-nye-cye": "echo hi && echo bye && echo nye && echo cye"
}
```

This can be made much more legible with command lists:

```json
{
    "hi-bye-nye-cye": [
        "echo hi",
        "echo bye",
        "echo nye",
        "echo cye"
    ]
}
```

This will execute the exact same commands.

```shell
$ run hi-bye-nye-cye
hi
bye
nye
cye
```