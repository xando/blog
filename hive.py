import buzzy
import markdown

from dateutil import parser
from pygments.formatters import HtmlFormatter


class StaticSite(buzzy.Base):

    PYGMENTS_STYLE = "emacs"

    @buzzy.memoized
    def get_posts(self, posts, index):
        md = markdown.Markdown(extensions=['codehilite', 'meta'])
        results = []
        for post in posts:
            results.append({
                "name": post.replace('md','html'),
                "content": index.content % md.convert(post.content),
                "title": md.Meta['title'][0],
                "date": md.Meta['date'][0],
                "date-object": parser.parse(md.Meta['date'][0])
            })

        results.sort(key=lambda x:x['date-object'])
        return results

    @buzzy.render
    def pygments(self):
        return {
            "name": "pygments.css",
            "content": HtmlFormatter(style=self.PYGMENTS_STYLE).get_style_defs()
        }

    @buzzy.render('index.html', 'posts')
    def index(self, index, posts):

        content = "".join([
            '<a href="%(name)s"><h1>%(title)s</h1></a><div class="break">...</div>' % e
            for e in self.get_posts(posts, index)
        ])

        return {"name": index.basename, "content": index.content % content}

    @buzzy.render('posts', 'index.html')
    def posts(self, posts, index):
        return self.get_posts(posts, index)
