---
layout: default
title: Home
---

<!-- 1. The Homepage Art -->
<div class="homepage-art">
  <img src="assets/img/home.png" alt="A calming, minimalist illustration">
</div>

<!-- 2. Section Title -->
<h2 class="section-title">Latest Thoughts</h2>

<!-- 3. The Latest 10 Posts -->
<div class="post-list">
  {% for post in site.posts limit:4 %}
    <div class="post-item">
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
      <p>{{ post.content | strip_html | truncatewords: 50 }}</p>
    </div>
  {% endfor %}
</div>

<!-- 4. Link to the Full Blog Archive -->
<div class="view-all-posts">
  <a href="{{ '/blog.html' | relative_url }}" class="button">View All Posts →</a>
</div>