---
layout: default
title: yoga sutra 
permalink: /books/yoga-sutra/
author: Patanjali
quote: "Yoga is not a philosophy but a discipline, to take you from where you are and realise what you can totally be."
tags: ["Spirituality"]
featured: true
---

<div class="vbt-header">
  <h1>Patanjali Yoga Sutras</h1>
  <!-- <p class="subtitle">aa</p> -->
</div>


<div class="meditation-list">
  {% assign sutras = site.yoga_sutra | sort: 'sutra' %}

  {% for s in sutras %}
    <a href="{{ s.url | relative_url }}" class="meditation-list-item">
      <div class="meditation-title-block">
        <span class="meditation-number">Sutra {{ s.sutra }}</span>
        <span class="meditation-method">{{ s.title }}</span>
      </div>
      <span class="arrow">→</span>
    </a>
  {% endfor %}
</div>