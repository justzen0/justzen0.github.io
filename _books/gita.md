---
layout: default
title: "Bhagvad gita"
author: "Osho"
quote: "Complete summary of Osho's geeta darshan"
tags: ["Religious Text", "Philosophy", "Hinduism", "Epic Poetry", "Spirituality"]
featured: true
---

<div class="gita-toc-header">
  <h1>The Bhagavad Gita with Osho's commentary</h1>
  <p>An exploration of the divine song of God. Please select a chapter.</p>
</div>
<div class="adhyay-list" style="{margin: 1rem}">
  {% for i in (1..18) %}
    {% assign adhyay_category = "adhyay-" | append: i %}
    {% assign first_shloka = site.gita | where: "categories", adhyay_category | sort: "shloka_num" | first %}
    {% if first_shloka %}
      <a href="/books/gita/{{ adhyay_category }}.html" class="adhyay-list-item">
        <div class="adhyay-number">Chapter {{ i }}</div>
        <div class="adhyay-title">{{ first_shloka.adhyay_title }}</div>
      </a>
    {% endif %}
  {% endfor %}
</div>
<div class="gita-introduction">
  <p>Special thanks to the person(s) who created bhagvad gita verse and translation database.<a href="https://github.com/gita/gita">checkout repository</a> </p>
  <p class="source-note">(Compiled using Gemini)</p>
</div>