# Unix Shell

A Unix-like command-line shell built from scratch in Python.

## Features

* Interactive command-line interface
* `echo` builtin
* `exit` builtin
* `type` builtin
* `pwd` builtin
* `cd` builtin
* PATH-based executable lookup
* External program execution
* Command-line argument handling
* Absolute path navigation

## Tech Stack

* Python
* Unix/Linux process management
* Filesystem and environment APIs

## Current Progress

The shell currently supports:

```text
$ echo hello
hello

$ type ls
ls is /usr/bin/ls

$ pwd
/current/working/directory

$ cd /usr/bin

$ ls
...
```

## Project Structure

```text
unix-shell-python/
├── app/
│   └── main.py
├── your_program.sh
└── README.md
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/AkshanshCodes/unix-shell-python.git
cd unix-shell-python
```

Run the shell:

```bash
./your_program.sh
```

## Status

🚧 Work in progress.

More shell functionality will be added as development continues.


