---
layout: default
title: Movies
---

<h1>Movies I've Watched</h1>
<p>Films that resonated, provoked thought, or provided a quiet escape.</p>

<!-- START: NEW Filter Dropdown Section -->
{% assign all_tags = site.movies | map: 'tags' | join: ',' | split: ',' | uniq | sort %}
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
  {% for movie in site.movies %}
    <a href="{{ movie.url | relative_url }}" class="item-card-link" data-tags="{% for tag in movie.tags %}{{ tag | slugify }} {% endfor %}">
      <div class="item-card movie-card">
        <img 
          loading="lazy" 
          src="{{ movie.poster | relative_url }}" 
          alt="Poster for {{ movie.title }}" 
          class="movie-poster">
        <div class="card-gradient-overlay"></div>
        <div class="movie-info">
          <h3>{{ movie.title }}</h3>
          <p class="item-meta">{{ movie.director }} ({{ movie.year }})</p>
        </div>
      </div>
    </a>
  {% endfor %}
</div>