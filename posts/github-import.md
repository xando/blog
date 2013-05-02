Title:   Import python modules from Github (PEP 302)
Summary: A brief description of my document.
Authors: Waylan Limberg
         John Doe
Date:    October 2, 2010


# Import python modules from Github (PEP 302) #

or what if this would be possible?

	:::python
	from github.com.kennethreitz.requests import requests

	requests.get('http://google.com')


Recently I've created a simple library which is a proof of concept for
this idea in python.  Thanks to
[PEP 302](http://www.python.org/dev/peps/pep-0302/) apparently it's
quite possible.


	:::python
	import github_import
	from github.com.kennethreitz.requests import requests

	print requests.get('http://google.com')
	

The magic will happen in github_import module.  The module is messing
around with import hooks and use of PEP 302.  If you are interested
how it works, implementation might be find
[here](https://github.com/xando/github_import).

