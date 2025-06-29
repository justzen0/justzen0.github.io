---
layout: default
title: All Posts
---

<h1>All Posts</h1>

<div class="post-list">
  {% for post in site.posts %}
    <div class="post-item">
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
      <p>{{ post.excerpt }}</p>
    </div>
  {% endfor %}
</div>