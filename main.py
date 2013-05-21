import buzzy
import markdown

from datetime import datetime
from dateutil import parser
from pygments.formatters import HtmlFormatter


class StaticSite(buzzy.Base):

    PYGMENTS_STYLE = "emacs"

    @buzzy.memoized
    def get_posts(self, posts):
        md = markdown.Markdown(extensions=['codehilite', 'meta'])
        results = []
        for post in posts:
            content = md.convert(post.content)
            if md.Meta.get('publish', [False])[0]:

                results.append({
                    "name": post.replace('md','html'),
                    "source": post.content,
                    "content": content,
                    "title": md.Meta['title'][0],
                    "date": md.Meta['date'][0],
                    "dateobject": parser.parse(md.Meta['date'][0])
                })

        results.sort(key=lambda x:x['dateobject'], reverse=True)
        return results

    @buzzy.render
    def pygments(self):
        return "pygments.css", HtmlFormatter(style=self.PYGMENTS_STYLE).get_style_defs()

    @buzzy.render
    def index(self):
        posts = self.get_posts(buzzy.path('posts'))
        return 'index.html', self.render_template('index.html', posts=posts)

    @buzzy.render
    def posts(self):
        posts = self.get_posts(buzzy.path('posts'))
        return [(p['name'], self.render_template('post.html', post=p)) for p in posts]

    @buzzy.render
    def about(self):
        return 'about.html', self.render_template('about.html')

    @buzzy.render
    def rss(self):
        posts = self.get_posts(buzzy.path('posts'))
        return 'rss.xml', self.render_template('rss.xml', posts=posts)

    @buzzy.command
    def publish(self, args):
        self._build()

        with buzzy.path(self.BUILD_DIR) as p:
            p.run('git init')
            p.run('git remote add origin git@github.com:xando/xando.github.com.git')
            p.run('git add -A')
            p.run('git commit -m "published"')
            p.run('git push --force')
        print "Published %s" % datetime.now()

