Title:   from os import path2
Date:    01-12-2013
status:  publish

# from os import path2

There are a few things that are a bit annoying in the **os** module inside the Python standard library. For me, one of the biggest bugbears is the **os.path** module, and path handling within this. Python, as an object oriented language, has this really cool idea that everything is an object; even class definition and functions are objects. So how come the path module is different?

Well, path is an object as well, but it's a string object, not a **path** object. Since it is really easy to observe that files and directories have something to say about themselves by design, and that what they say is more than a string object can carry, I decided to write a simple alternative.

## the thing

Python is often compared with Ruby, so let's have a look at how things are done there in 
[Pathname](http://www.ruby-doc.org/stdlib-1.9.3/libdoc/pathname/rdoc/Pathname.html). Whether or not you are a Ruby fan, I think we can say that the **Pathname** API is pretty good. Following a few ideas borrowed Ruby, I decided to propose something on this subject and create my own path implementation. As a result, I created a Python package and called it [os.path2](http://ospath2.xando.org/), which would be the new version of **os.path** with a ‘more’ object oriented approach to path handling in Python.

Below are a few examples of what is possible with the package.


	:::python
	
	>>> from os import path2

    >>> path2('/var/log')
    /var/log

    >>> path2('/var', 'log')
    /var/log
	
	>>> path2('/var/log/syslog').a_time
	1358549788.7512302

    >>> path2('/home/you/file').user
    'you'
	
	>>> path2('.').mod
	'0775'

    >>> [(element.user, element.group, element.mod) for element in path2('.')]
    [('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0775'),
     ('user', 'user', '0664')]


The **path2** object is also an instance of basestring, so all methods implemented for 
[string/unicode](http://docs.python.org/2/library/stdtypes.html#string-methods) 
will work here as well.

	:::python
	
	>>> path2('/home/user/Projects/os.path2').split('/')
	['', 'home', 'user', 'Projects', 'os.path2']

	>>> path2('/home/user/test_tmp_directory').replace('_', '-')
	'/home/user/test-tmp-directory'
	
	>>> location = path2('/home/user/test_tmp_directory')
	>>> location.mv(location.replace('_', '-'))


If you are interested, give it a go. 
The full API description if available [here](http://ospath2.xando.org/en/latest/). 
The code is on [github](http://ospath2.xando.org/). 
The package is available in the usual way, from PyPi.

	:::bash
	$ pip install os.path2

Alternatives
------------

This idea is not new. Even though I really like my implementation, I need to be honest here and suggest a few other **path** projects that were created a bit earlier than mine and have broadly similar approaches to solving the path problem:


* [path.py](https://github.com/jaraco/path.py) by Jason R. Coombs,
* [Unipath](https://github.com/mikeorr/Unipath) by Mike Orr.


And there are actually two PEPs about it as well:

* [PEP 355](http://www.python.org/dev/peps/pep-0355/) (2006 rejected), 
* [PEP 428](http://www.python.org/dev/peps/pep-0428/) (2012 draft).

