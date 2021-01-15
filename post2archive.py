import glob
import re
is_local = True
url = "(http://localhost:4000/" if is_local else "(https://deeplab-team.github.io/"
categories = ["projects", "seminars", "implementation"]

for cat in categories:
    print(cat)
    posts = sorted(glob.glob("_posts/%s/*.md" % cat))
    for post in reversed(posts):
        with open(post, encoding="utf-8_sig") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("title:"):
                    print("[" + line.strip().replace("title: ", "") + "]", end='')
                if line.startswith("permalink:"):
                    print(url + line.strip().replace("permalink: ", "") + ")")
                    print()
    print("")
    