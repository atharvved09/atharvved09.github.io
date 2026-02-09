---
layout: default
title: Home
---

<style>
/* Custom Portfolio Styles */
.portfolio-header {
  text-align: center;
  margin-bottom: 3rem;
  padding: 2rem 0;
  background: linear-gradient(135deg, #159957, #155799);
  color: white;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.portfolio-header h1 {
  margin: 0;
  font-size: 2.5rem;
  color: white;
}

.portfolio-header p {
  font-size: 1.2rem;
  opacity: 0.9;
  max-width: 600px;
  margin: 1rem auto 0;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.project-card {
  background: white;
  border: 1px solid #e1e4e8;
  border-radius: 8px;
  padding: 1.5rem;
  transition: transform 0.2s, box-shadow 0.2s;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}

.project-title {
  margin-top: 0;
  font-size: 1.4rem;
  color: #159957;
}

.project-title a {
  text-decoration: none;
  color: inherit;
}

.project-desc {
  flex-grow: 1;
  color: #586069;
  font-size: 0.95rem;
  line-height: 1.5;
  margin-bottom: 1rem;
}

.project-meta {
  font-size: 0.85rem;
  color: #6a737d;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
  border-top: 1px solid #eaecef;
  padding-top: 1rem;
}

.project-lang {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.lang-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #f1e05a; /* Default to JS yellow, serves as generic */
}

/* Featured Badge */
.featured-badge {
    background-color: #ffd33d;
    color: #24292e;
    padding: 0.2rem 0.6rem;
    border-radius: 2rem;
    font-size: 0.75rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    display: inline-block;
}

/* Private Badge */
.private-badge {
    background-color: #6a737d;
    color: #ffffff;
    padding: 0.2rem 0.6rem;
    border-radius: 2rem;
    font-size: 0.75rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    display: inline-block;
    margin-right: 0.5rem;
}
</style>

<div class="portfolio-header">
  <h1>Hi, I'm Atharv</h1>
  <p>Exploring the intersection of Computer Science, Bioinformatics, and Algorithms.</p>
</div>

## About Me

I am a passionate developer and researcher with expertise in **Computer Science**, **Bioinformatics**, and **Data Structures**. My work focuses on building efficient algorithms, visualization tools, and exploring genetic technologies.

Here is a collection of my open-source projects and simulations.

<div class="projects-grid">
  {% for project in site.data.projects %}
  <div class="project-card">
    <div>
      {% if project.visibility == 'Private' %}
      <span class="private-badge">Private</span>
      {% endif %}
      {% if project.featured %}
      <span class="featured-badge">Featured</span>
      {% endif %}
      <h3 class="project-title">
        <a href="{{ project.url }}" target="_blank">{{ project.name }}</a>
      </h3>
    </div>
    <p class="project-desc">{{ project.summary }}</p>
    <div class="project-meta">
      <div class="project-lang">
        {% if project.language %}
        <span class="lang-dot" style="background-color: {% cycle '#f1e05a', '#3572A5', '#e34c26', '#89e051' %};"></span>
        {{ project.language }}
        {% else %}
        <span>Code</span>
        {% endif %}
      </div>
      <!--
      {% if project.stars > 0 %}
      <span>★ {{ project.stars }}</span>
      {% endif %}
      -->
    </div>
  </div>
  {% endfor %}
</div>

<br>

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #eee;">
  <h2>Interactive Labs</h2>
  <p>Check out my specific genetic drift simulations:</p>
  <div style="display:flex; justify-content:center; gap:1rem; flex-wrap:wrap; margin-top:1rem;">
      <a class="btn" href="Simple_RandomWalk.html">Simple Random Walk</a>
      <a class="btn" href="Multi_RandomWalk.html">Multi Random Walk</a>
      <a class="btn" href="MonteCarlo_Simulations.html">Monte Carlo</a>
  </div>
</div>
