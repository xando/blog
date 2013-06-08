from buzzy import render
import buzzy
import markdown

from datetime import datetime
from dateutil import parser
from pygments.formatters import HtmlFormatter


class StaticSite(buzzy.Base):

    PYGMENTS_STYLE = "emacs"
    INCLUDE = ['CNAME', 'libs/', 'img/']
    BUILD_DIR = "build"

    @buzzy.memoized
    def get_posts(self):
        md = markdown.Markdown(extensions=['codehilite', 'meta'])
        results = []
        for post in buzzy.path('posts'):
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

    @buzzy.register
    def pygments(self):
        content = HtmlFormatter(style=self.PYGMENTS_STYLE).get_style_defs()
        yield render.content("pygments.css", content)

    @buzzy.register
    def index(self):
        yield render.template(
            'index.html', "index.html", posts=self.get_posts()
        )

    @buzzy.register
    def posts(self):
        for post in self.get_posts():
            yield render.template(post['name'], 'post.html', post=post)

    @buzzy.register
    def about(self):
        yield render.template('about.html', 'about.html')

    @buzzy.register
    def rss(self):
        yield render.template('rss.xml', 'rss.xml', posts=self.get_posts())

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


if __name__ == "__main__":
    StaticSite()