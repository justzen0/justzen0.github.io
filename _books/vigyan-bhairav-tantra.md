---
layout: default
title: Vigyan Bhairav Tantra
permalink: /books/vigyan-bhairav-tantra/
author: Osho
quote: "A book that will help you explore the depths of consiousness."
---

<div class="vbt-header">
  <h1>Vigyan Bhairav Tantra</h1>
  <p class="subtitle">The 112 Meditations for Attaining Oneness</p>
</div>

<div class="vbt-introduction">
  <p>Below is a comprehensive summary of the 112 meditations found within the Vigyan Bhairav Tantra, drawn from Osho's masterwork, "The Book of Secrets."</p>
  <p>This is an exhaustive collection of every meditation technique possible. So as long as humans exist, no novel method can be developed beyond what is listed here—only new combinations can be discovered.</p>
  <p>The path is simple:
Choose one technique. Follow it for three months. Experience the change within.</p>
  <p class="source-note">(Compiled using NotebookLM)</p>
</div>

<div class="meditation-list">
  {% assign meditations = site.vigyan_bhairav_tantra | sort: 'n' %}

  {% for meditation in meditations %}
    <a href="{{ meditation.url | relative_url }}" class="meditation-list-item">
      <div class="meditation-title-block">
        <span class="meditation-number">Meditation {{ meditation.n }}</span>
        <span class="meditation-method">{{ meditation.title }}</span>
      </div>
      <span class="arrow">→</span>
    </a>
  {% endfor %}
</div>