# deeplab website

You can see our website: https://deeplab-team.github.io/

## How to post a blog

1. create a markdown file following the naming rule of `YYYY-MM-DD-TITLE.md` in `_posts`.

2. write the below prefix.
```
---
layout: post
title: YOUR TITLE
tags: [Projects] //choice: Projects, Seminars, Implementation
permalink: project/YYYY-MM-DD-TITLE //path should be [category / your filename].
---
```

Optionally, you can add 
```
subtitle: YOUR SUBTITLE
cover-img: /assets/img/path.jpg
thumbnail-img: /assets/img/thumb.png
share-img: /assets/img/path.jpg
```

3. You must include "概要", "目的", and "実施期間・日時".

## How to create a category's archive.

1. Please run 'python post2archive.py' that outputs the list of your posts.
