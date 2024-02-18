NAME

::

    ZBOT - python3 irc bot

SYNOPSIS

::

    zbot <cmd> [key=val] [key==val]
    zbot [-a] [-c] [-d] [-h] [-v] [-w]

    options are:

    -a     load all modules
    -c     start console
    -d     start daemon
    -h     display help
    -v     use verbose
    -w     wait for services


DESCRIPTION

::

    ZBOT is a python3 irc bot, it can connect to IRC, fetch and display RSS
    feeds, take todo notes, keep a shopping list and log text. You can also
    copy/paste the service file and run it under systemd for 24/7 presence
    in a IRC channel.

    ZBOT users BOTL, containing all the python3 code to program a unix cli
    program, such as disk perisistence for configuration files, event handler
    to handle the client/server connection, code to introspect modules for
    commands, deferred exception handling to not crash on an error, a parser
    to parse commandline options and values, etc.

    ZBOT uses OBJX, an module that allows for easy json save//load
    to/from disk of objects. It provides an "clean namespace" Object class
    that only has dunder methods, so the namespace is not cluttered with
    method names. This makes storing and reading to/from json possible.

    ZBOT is Public Domain.

USAGE

::

    without any argument the program does nothing

    $ zbot
    $

    see list of commands

    $ zbot cmd
    cmd,err,mod,req,thr,ver

    list of modules

    $ zbot mod
    cmd,err,fnd,irc,log,mod,req,rss,tdo,thr

    use -c to start a console

    $ zbot -c

    use mod=<name1,name2> to load additional modules

    $ zbot -c mod=irc,rss
    >

    use -v for verbose

    $ zbot -cv mod=irc
    ZBOT started CV started Sat Dec 2 17:53:24 2023
    >


CONFIGURATION

::

    $ zbot cfg 
    channel=#zbot commands=True nick=zbot port=6667 server=localhost

    irc

    $ zbot cfg server=<server>
    $ zbot cfg channel=<channel>
    $ zbot cfg nick=<nick>

    sasl

    $ zbot pwd <nsvnick> <nspass>
    $ zbot cfg password=<frompwd>

    rss

    $ zbot rss <url>
    $ zbot dpl <url> <item1,item2>
    $ zbot rem <url>
    $ zbot nme <url> <name>

COMMANDS

::

    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    fnd - find objects 
    log - log some text
    met - add a user
    mre - displays cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    req - reconsider
    rss - add a feed
    thr - show the running threads

SYSTEMD

::

    save the following it in /etc/systems/system/zbot.service and
    replace "<user>" with the user running pipx

    [Unit]
    Description=python3 irc bot
    Requires=network-online.target
    After=network-online.target

    [Service]
    Type=simple
    User=<user>
    Group=<user>
    WorkingDirectory=/home/<user>/.zbot
    ExecStart=/home/<user>/.local/pipx/venvs/zbot/bin/zbot -d
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target

    then run this

    $ mkdir ~/.zbot
    $ sudo systemctl enable zbot --now

    default channel/server is #zbot on localhost

FILES

::

    ~/.zbot
    ~/.local/bin/zbot
    ~/.local/pipx/venvs/zbot/

AUTHOR

::

    Bart Thate <objx@proton.me>

COPYRIGHT

::

    ZBOT is Public Domain.
