# rinkrat
Rinkrat is a command line tool to query the NHL's public API for statistics.

## Install
You can install rinkrat from PyPi

    python -m pip install rinkrat

It is supported by python 3.8 and above.

## Usage

    rinkrat [ command ] [ sub-command ] { parameters }

Rinkrat uses the command line interface to get statistics from the public NHL api. With the current version you can access team standings data and rank it based on several criteria:

### Commands
Commands give you access to different data. Sub-commands determine how that data is organized and presented. For command snippits and descriptions, please see the [commands](docs/commands) directory.
