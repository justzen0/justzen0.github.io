---
layout: default
title: Books
---

<h1>Books I've Read</h1>
<p>A collection of books that have offered perspective or pause.</p>

<!-- ====================================================== -->
<!-- 1. NEW FEATURED BOOKS SECTION -->
<!-- ====================================================== -->
<div class="featured-books-section">
  <h2 class="section-title">Featured Reads</h2>
  <div class="item-grid featured-grid">
    {% assign featured_books = site.books | where: "featured", true %}
    {% for book in featured_books %}
      <a href="{{ book.url | relative_url }}" 
         class="item-card-link" 
         data-tags="{% for tag in book.tags %}{{ tag | slugify }} {% endfor %}">
        <div class="item-card book-card">
          <h3>{{ book.title }}</h3>
          <p class="item-meta">by {{ book.author }}</p>
          <blockquote class="item-quote">"{{ book.quote }}"</blockquote>
        </div>
      </a>
    {% endfor %}
  </div>
</div>


<!-- START: NEW Filter Dropdown Section -->
{% assign all_tags = site.books | map: 'tags' | join: ',' | split: ',' | uniq | sort %}
<div class="filter-container">
  <span class="filter-label">Filter by genre:</span>
  <div class="filter-dropdown-wrapper">
    <select id="tag-filter-dropdown">
      <option value="all">All Genres</option>
      {% for tag in all_tags %}
        {% assign clean_tag = tag | strip %}
        <option value="{{ clean_tag | slugify }}">{{ clean_tag }}</option>
      {% endfor %}
    </select>
  </div>
</div>
<!-- END: NEW Filter Dropdown Section -->

<div class="item-grid all-books-grid">
  {% for book in site.books %}
    <a href="{{ book.url | relative_url }}" class="item-card-link" data-tags="{% for tag in book.tags %}{{ tag | slugify }} {% endfor %}">
      <div class="item-card book-card">
        <h3>{{ book.title }}</h3>
        <p class="item-meta">by {{ book.author }}</p>
        <blockquote class="item-quote">"{{ book.quote }}"</blockquote>
      </div>
    </a>
  {% endfor %}
</div>