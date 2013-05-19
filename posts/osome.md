Title:   Let's fix few things in python os module, ... osome
Date:    May 05, 2013


# Let's fix few things in python std lib, ... osome

So as there are things that are a bit annoying in **os** module
inside Python standard library. First thing that really annoys me is
**os.path** and path handling in it. Python as objected oriented
language has this really cool idea that everything is an object even
class and function are objects as well. Well path is a object as well
in Python but string object not path object and by design path (file,
directory) has something to say about itself. Path could be a well defined object. 

## the thing

Python is often compared with Ruby let's have a look how things are
done there
[Pathname](http://www.ruby-doc.org/stdlib-1.9.3/libdoc/pathname/rdoc/Pathname.html)
Well despite the fact that if you Ruby or now, we have to say that **Pathname** API is pretty
good.


*********

	:::python
	from osome import path
	
	print path('~').ls()
	[u'./.git',
	u'./build',
	u'./img',
	u'./libs',
	u'./posts',
	u'./.gitignore',
	u'./CNAME',
	u'./hive.py',
	u'./hive.pyc',
	u'./index.html',
	u'./rss.xml']

*********

	:::python
	from osome import path
	
	print [p for p in path('.')]
	[u'./.git',
	u'./build',
	u'./img',
	u'./libs',
	u'./posts',
	u'./.gitignore',
	u'./CNAME',
	u'./hive.py',
	u'./hive.pyc',
	u'./index.html',
	u'./rss.xml']



The **osome.path** API is not finall but probably won't change
dramatically at least that one idea will stay for sure path should be
an object.

## the other thing


The second thing that is really weird and can imagine hard to get for
people new to Python is **os.subprocess**.  So you want to capture
stdin from your python script? So you have probably two options.

	:::python
	from osome import path
