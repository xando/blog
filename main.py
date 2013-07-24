import buzzy
from buzzy import render

from datetime import datetime
from dateutil import parser
from pygments.formatters import HtmlFormatter

from buzzy.packages import run

class StaticSite(buzzy.Base):

    PYGMENTS_STYLE = "emacs"
    INCLUDE = ['CNAME', 'libs/', 'img/']

    @buzzy.memoized
    def get_posts(self):
        results = [
            render.markdown(post.replace('md','html'), post) for post in
            buzzy.path('posts')
        ]
        results = [
            post for post in results if post.meta.get('status') == "publish"
        ]
        results.sort(
            key=lambda x:parser.parse(x.meta['date']), reverse=True
        )
        return results

    @buzzy.register
    def preview_post(self):
        for post_file in buzzy.path('posts'):
            target = post_file\
                .replace('md','html')\
                .replace('posts/', 'posts/preview/')
            post = render.markdown(target, post_file)
            yield render.template(post.name, "post.html", post=post)

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
            yield render.template(post.name, "post.html", post=post)

    @buzzy.register
    def about(self):
        yield render.template('about.html', 'about.html')

    @buzzy.register
    def rss(self):
        yield render.template('rss.xml', 'rss.xml', posts=self.get_posts())

    @buzzy.command
    def publish(self, args):
        self._build()

        p = buzzy.path(self.BUILD_DIR)

        run('git init')
        run('git remote add origin git@github.com:xando/xando.github.com.git')
        run('git add -A')
        run('git commit -m "published"')
        run('git push --force')
        print "Published %s" % datetime.now()


if __name__ == "__main__":
    StaticSite()