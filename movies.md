---
layout: default
title: Movies
---

<h1>Movies I've Watched</h1>
<p>Films that resonated, provoked thought, or provided a quiet escape.</p>

<div class="item-grid">
  {% for movie in site.movies %}
    <a href="{{ movie.url | relative_url }}" class="item-card-link">
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