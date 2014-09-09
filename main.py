import os
import buzzy
import subprocess

from datetime import datetime
from pygments.formatters import HtmlFormatter


class StaticSite(buzzy.Base):

    PYGMENTS_STYLE = "emacs"
    INCLUDE = ['CNAME', 'libs/', 'img/', 'cv/']

    @buzzy.register
    def blog(self):
        BLOG_DIR = os.path.join(self.BASE_DIR, "posts")
        BLOG_DATE_FORMAT = "%d-%m-%Y"

        posts = []
        for post in os.listdir(BLOG_DIR):
            post_path = os.path.join(BLOG_DIR, post)
            if post_path.endswith('md'):
                posts.append(
                    buzzy.render.markdown(post_path, post.replace('.md','.html'))
                )

        posts.sort(
            key=lambda x: datetime.strptime(x.meta['date'], BLOG_DATE_FORMAT),
            reverse=True
        )

        yield buzzy.render.template('index.html', "index.html", posts=posts)

        for post in posts:
            yield buzzy.render.template(
                "post.html",
                os.path.join("blog", post.name),
                post=post
            )

    @buzzy.register
    def pygments(self):
        content = HtmlFormatter(style=self.PYGMENTS_STYLE).get_style_defs()
        yield buzzy.render.content("pygments.css", content)

    @buzzy.register
    def about(self):
        yield buzzy.render.template('about.html', 'about.html')

    @buzzy.register
    def about(self):
        yield buzzy.render.template('cv.html', 'cv.html')

    @buzzy.command
    def deploy(self, args):
        self.build(args)

        git_thing = [
            "git init",
            "git remote add origin git@github.com:xando/xando.github.com.git",
            "git add .",
            "git commit -m 'page generated'",
            "git push --force -u origin master "
        ]

        for each in git_thing:
            print subprocess.check_output(each, shell=True, cwd=self.BUILD_DIR)

        self.logger.info("Deployed")


if __name__ == "__main__":
    StaticSite()
