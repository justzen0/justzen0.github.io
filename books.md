---
layout: default
title: Books
---

<h1>Books I've Read</h1>
<p>A collection of books that have offered perspective or pause.</p>

<div class="item-grid">
  {% for book in site.books %}
    <a href="{{ book.url | relative_url }}" class="item-card-link">
      <div class="item-card book-card">
        <h3>{{ book.title }}</h3>
        <p class="item-meta">by {{ book.author }}</p>
        <blockquote class="item-quote">"{{ book.quote }}"</blockquote>
      </div>
    </a>
  {% endfor %}
</div>