Title:   from os import path2
Date:    Jun 24, 2013
status:  publish

# from os import path2

There are few things that are a bit annoying for me in **os** module inside
Python standard library. One of those things surely for me would be
the **os.path** module and path handling in it. Python as objected oriented
language, and it has this really cool idea that everything is an object, even
class definition and functions are objects. 

Well path is a object as well
in there but it's a string object not a **path** object. 
Since is really easy to observe that by design files and 
directories have something more to say about themselves than a string object can carry.

## the thing

Python is often compared with Ruby, so let's have a look how things are
done there in
[Pathname](http://www.ruby-doc.org/stdlib-1.9.3/libdoc/pathname/rdoc/Pathname.html).
Despite the fact if you like Ruby or not, 
I think we can say that the **Pathname** API is pretty good. 
So following few ideas borrowed Ruby, I decided to propose something on this subject and decided to create my own path implementation. 
As a result created an Python package called it [os.path2](http://ospath2.xando.org/) the new version of **os.path** with a "more" object oriented
approach to path handling in Python. 


Bellow few examples what is possible with the package.


*********

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


The **path2** object is also a instance of basestring so all methods implemented for
[string/unicode](http://docs.python.org/2/library/stdtypes.html#string-methods)
will work as well.

	:::python
	
	>>> path2('/home/user/Projects/os.path2').split('/')
	['', 'home', 'user', 'Projects', 'os.path2']

	>>> path2('/home/user/test_tmp_directory').replace('_', '-')
	'/home/user/test-tmp-directory'
	
	>>> location = path2('/home/user/test_tmp_directory')
	>>> location.mv(location.replace('_', '-'))


If you are interested, give it a go. 
Full API description if available [here](http://ospath2.xando.org/en/latest/). 
The code is on [github](http://ospath2.xando.org/). 
The package is available usual way from PyPi.

	:::bash
	$ pip install os.path2

Alternatives
------------

The idea is not new. Even though I really like me implementation, need to be honest here 
and point few other **path** projects that were create a bit earlier than mine 
and have similar approach to solve the path problem:


* [path.py](https://github.com/jaraco/path.py) by Jason R. Coombs,
* [Unipath](https://github.com/mikeorr/Unipath) by Mike Orr.


And there are actually two PEPs about it as well:

* [PEP 355](http://www.python.org/dev/peps/pep-0355/) (2006 rejected), 
* [PEP 428](http://www.python.org/dev/peps/pep-0428/) (2012 draft).

