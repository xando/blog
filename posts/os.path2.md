Title:   from os import path2
Date:    May 05, 2013
Publish: preview

# from os import path2

There are things that are a bit annoying in **os** module inside
Python standard library. First thing that really annoys me is
**os.path** and path handling in it. Python as objected oriented
language has this really cool idea that everything is an object, even
class definition and functions are objects as well. Well path is a object
in there but it's string object not path object. Since is really easy to observe that by design path file,
directory have something to say about themselves. 
I decided to propose something on this subject and created an Python package called **os.path2**. 


## the thing

Python is often compared with Ruby, then let's have a look how things are
done there
[Pathname](http://www.ruby-doc.org/stdlib-1.9.3/libdoc/pathname/rdoc/Pathname.html), 
despite the fact that you like Ruby or not, we can say that the **Pathname** API is pretty good. 
Following few ideas borrowed Ruby, decided to create my own path implementation created
[os.path2](http://ospath2.xando.org/) a "more" object oriented
approach to path handling in Python. 

*********

	:::python
	
	>>> from os import path2 as path

    >>> path('/var/log')
    /var/log

    >>> path('/var', 'log')
    /var/log

    >>> path('/home/you/file').user
    'you'

    >>> [(element.user, element.group, element.mod) for element in path('.')]
    [('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0664'),
     ('user', 'user', '0775'),
     ('user', 'user', '0664')]


Path is also  a instance of basestring so all  methods implemented for
[string/unicode](http://docs.python.org/2/library/stdtypes.html#string-methods)
should work as well.

	:::python
	
	>>> path('/home/user/Projects/os.path2').split('/')
	['', 'home', 'user', 'Projects', 'os.path2']

	>>> path('/home/user/test_tmp_directory').replace('_', '-')
	'/home/user/test-tmp-directory'
	
	>>> location = path('/home/user/test_tmp_directory')
	>>> location.mv(location.replace('_', '-'))


Since I didn't want to copy and paste API all calls here, if you are still interested visit os.path2 docs site


Alternatives
------------

The idea is not new. Even though I really like me implementation, need to be honest here 
and point few other **path** projects that were create a bit earlier than mine 
and have similar approach to solve the path problem:


* [path.py](https://github.com/jaraco/path.py) by Jason R. Coombs,
* [Unipath](https://github.com/mikeorr/Unipath) by Mike Orr.


And There are actually two PEPs about it as well

* [PEP 355](http://www.python.org/dev/peps/pep-0355/) (2006 rejected), 
* [PEP 428](http://www.python.org/dev/peps/pep-0428/) (2012 draft).

