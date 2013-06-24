Title:   Virtualenv in Python and how I roll!
Summary: A brief description of my document.
Date:    May 2, 2013
status:  publish


# Virtualenv in Python and how I roll! #

A few words about Virtualenv in Python. It's a simple approach to
isolate your python development environment from other development
environments, and, equally importantly, from your global Python
packages. If you're using any Unix based system (this includes any
Linux and MacOS system) you have Python installed and most in cases
you will have other packages installed with it as well. Virtualenv
will prevent packages being imported if you haven't installed them for
your project, it will keep your different versions of the same package
separate, and allows you to freeze the project state and send this to
your team member who can then recreate the environment seamlessly.


Virtualenv comes with nice extension called virtualenvwrapper which
will give you a lot of useful commands. So let's get it working.

	:::bash
	$ sudo pip install virtualenv virtualenvwrapper

	# or

	$ sudo easy_install virtualenv virtualenvwrapper


and then append this line to  your ~/.bashrc or ~/.zshrc.

	:::bash
	[[ -e /usr/local/bin/virtualenvwrapper.sh ]] && source /usr/local/bin/virtualenvwrapper.sh


You are ready to go, your virtualenv is set up and ready.  You can
read more about the details
[http://virtualenv.readthedocs.org](http://virtualenv.readthedocs.org)
and
[http://virtualenvwrapper.readthedocs.org](http://virtualenvwrapper.readthedocs.org)


* * * * *


## How I roll ##

	:::bash
    upsearch() {
        test / == "$PWD" && return || \
            test -f "$1" && echo "$PWD/$1" && return || \
            cd .. && upsearch "$1"
    }

    has_virtualenv() {
        VIRTUALENV_FILE=`upsearch .virtualenv`
        if [ $VIRTUALENV_FILE ]
        then
            VIRTUALENV_NAME=$(cat $VIRTUALENV_FILE)
            if [ -d "$WORKON_HOME/$VIRTUALENV_NAME" ]; then
                if [ -z $VIRTUAL_ENV ] || [ $VIRTUAL_ENV -a $(basename "$VIRTUAL_ENV") != $VIRTUALENV_NAME ]; then
                    workon $VIRTUALENV_NAME
                fi
            else
                VIRTUALENV_REQUIREMENTS="$PWD/requirements.txt"
                if [ -f $VIRTUALENV_REQUIREMENTS ]; then
                    mkvirtualenv $VIRTUALENV_NAME -r $VIRTUALENV_REQUIREMENTS
                else
                    mkvirtualenv $VIRTUALENV_NAME
                fi
                site_packages="`virtualenvwrapper_get_site_packages_dir`"
                ln -s `virtualenvwrapper_get_site_packages_dir` "$PWD/.site-packages"
            fi
        else
            if [ $VIRTUAL_ENV ]; then
                deactivate
            fi
        fi
    }

    function venv_cd () {
        builtin cd $@ && has_virtualenv
    }

    alias cd="venv_cd"



This is a part of my **~/.zshrc**, but it should work with
**~/.bashrc** as well. Also plese note that
**/usr/local/bin/virtualenvwrapper.sh** in your case maybe located
somewhere else.


If Bash is all Greek to you, here's your plain English guide to the
code above. The very last line is responsible for overwriting the
**cd** command in your shell.  Every single time you try to change
your current directory the function has_virtualenv will be executed.
The function will try to do upsearch for the .virtualenv file. Let's
say that you right now:

	:::bash
	/home/user/mystuff/projects/AllTheThings/


The upsearch function will try to locate the .virtualenv file and read
its content, which is a single, simple line saying which virtualenv to
launch. The current location and all parent locations will be
searched.

	:::bash
	/home/user/mystuff/projects/AllTheThings/.virtualenv
	/home/user/mystuff/projects/.virtualenv
	/home/user/mystuff/.virtualenv
	/home/user/.virtualenv
	/home/.virtualenv
	/.virtualenv


If the file is located, virtualenv will be launched. But why read all
parent locations?  Well, maybe all parent locations is a bit too much,
but nevertheless I'm reading parent locations, because sometimes
projects are decoupled into smaller units.  Your virtualenv can be
overwritten on different levels, and sometimes it happens that when
using <b>cd</b> you will jump to a directory deeper than the main one,
and you will miss the .virtualenv file.

The next things that will happen are: if a virtualenv environment with
a name matching the content of the first found .virtualenv already
exists, it will simply switch to this one.  If not, a new one will be
created and, if you have defined requirements.txt file , this file
will be picked up as well and all requirements stored there will be
installed to the new virtualenv.  If the new virtualenv has been
created, the symlink to **site-packages** will be created as well.

The last thing worth mentioning is that when you leave the range of
upsearch, virtualenv will be deactivated, which means that you're not
going to drag it to different projects or locations in your system.


* * * * *
