---
layout: default
title: Movies
---

<h1>Movies I've Watched</h1>
<p>Films that resonated, provoked thought, or provided a quiet escape.</p>

<div class="item-grid">
  {% for movie in site.movies %}
    <a href="{{ movie.url | relative_url }}" class="item-card-link">
      <div class="item-card movie-card" style="background-image: url('{{ movie.poster | relative_url }}');">
        <div class="movie-info">
          <h3>{{ movie.title }}</h3>
          <p class="item-meta">{{ movie.director }} ({{ movie.year }})</p>
        </div>
      </div>
    </a>
  {% endfor %}
</div>