Title:   from subprocess import run
Date:    06-06-2013


# from subprocess import run


A while ago I wrote blog post about annoying bits of Python's std library.
I was complaining there about **os.path** and why file and directory should be a proper objects. 
Here I'm going to complain about one more thing, which could be solved a bit better than it is (in my opinion). Namely,
it will be running external processes in Python. So what is the current status? As far I know **subprocess** module will be current choice from std.
Inside the module you have few options:


* [subprocess.call](http://docs.python.org/2/library/subprocess.html#subprocess.call)
* [subprocess.check_call](http://docs.python.org/2/library/subprocess.html#subprocess.check_call)
* [subprocess.check_output](http://docs.python.org/2/library/subprocess.html#subprocess.check_output)
* [subprocess.Popen](http://docs.python.org/2/library/subprocess.html#popen-constructor)


I never used first two, and I would bet if you are planing to do something 
with external processes the last two are going to solve 90% cases that actual 
will have in relation to running external process, Or you can go wild with 
[subprocess.Popen](http://docs.python.org/2/library/subprocess.html#popen-constructor), 
which will solve you problem eventually. 


Few examples
------------

	:::python
	>>> from subprocess import run


Simple command call with argument and get stdout and stderr

	:::python
	>>> run('uname -r').stdout
	u'3.8.0-25-generic'
	
	>>> run('tail /nofile').stderr
	u'tail: cannot open \u2018/nofile\u2019 for reading: No such file or directory'
	
To get process' pid 

	:::python
	>>> run('uname -r').pid
	5972
	
To check status execution

	:::python
	>>> run('tail /var/log/auth.log').status
	0
	>>> run('tail /var/log/auth.logss').status
	1

Pipes everywhere, and get status from the each command executed

	:::python
	>>> run('ls -la', 'wc -l', 'wc -c').stdout
	3
	
To look inside pipes

	:::python
	>>> run('ls -la', 'wc -l', 'wc -c').chain
	[ls -la | wc -l | wc -c]

get partials stdout/stderr 
	
	:::python
	>>> run('ls -la', 'wc -l', 'wc -c').chain[1].stdout
	u'24'
	
get partials status 

	:::python
	>>> [e.status for e in run('ls -la', 'wc -l', 'wc -c').chain]
	[0, 0, 0]

Some helper functions to handle output, to help with output lines 

	:::python
	>>> run('ps aux', 'grep emacs').stdout.lines
	[u'user     6986 39.0  0.5 556092 40724 ?        Sl   11:53   0:06 emacs',
	 u'user     6993 78.2  0.5 556148 40820 ?        Sl   11:53   0:06 emacs']

	>>> run('ps aux', 'grep emacs').stdout.qlines
	[[u'seba', u'6986', u'10.3', u'0.5', u'556704', u'41688', u'?', u'Sl', u'11:53', u'0:10', u'emacs'], 
	 [u'seba', u'7013', u'77.8', u'0.5', u'556108', u'40728', u'?', u'Sl', u'11:55', u'0:06', u'emacs']]


I know that this less flexible than subprocess.Popen is, 
I probably will be easy find places where this API will be limited can easily find 
but "simplicity is a feature" should be a goal for standard library. 
I do belive that 90% of cases that users will have won't require to use 

Interesed?
----------

Give it a go. Package is available usual way

	:::bash
	pip install subprocess.run
	
	
The docs for the whole thing are available as well at [http://subprocessrun.xando.org](http://subprocessrun.xando.org) 


and the implementation would be at [https://github.com/xando/subprocess.run](https://github.com/xando/subprocess.run)
