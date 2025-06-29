---
layout: default
title: All Posts

pagination:
  enabled: true
  collection: posts
  per_page: 5
---

<h1>All Posts</h1>

<input type="text" id="search-input" placeholder="Search posts..." style="width:100%;padding:8px;margin-bottom:20px;">

<div class="post-list" id="post-list">
  {% for post in paginator.posts %}
    <div class="post-item" data-title="{{ post.title | escape }}" data-content="{{ post.content | strip_html | escape }}">
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
      <p>{{ post.excerpt }}</p>
    </div>
  {% endfor %}
</div>

<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path | relative_url }}">&laquo; Previous</a>
  {% endif %}
  <span>Page {{ paginator.page }} of {{ paginator.total_pages }}</span>
  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path | relative_url }}">Next &raquo;</a>
  {% endif %}
</div>
