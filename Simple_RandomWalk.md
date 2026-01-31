---
layout: default
title: Simple Random Walk
---

<h2>Genetic Drift: Allele Frequency Random Walk</h2>
<div class="controls" style="margin: 20px; padding: 15px; background: white; border-radius: 8px; color: #0b1220;">
  <button onclick="resetSimulation()">Restart Simulation</button>
  <p>Population Size: <span id="popSizeDisplay">50</span></p>
</div>
<div class="canvas-wrap">
  <canvas id="driftCanvas" width="800" height="400"></canvas>
</div>

<style>
  canvas { background: white; border: 1px solid #ccc; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
</style>

<script>
  const canvas = document.getElementById('driftCanvas');
  const ctx = canvas.getContext('2d');
  let populationSize = 50;
  let frequency = 0.5; // Starting at 50% Blue / 50% Red
  let gen = 0;
  let prevX = 0;
  let prevY = 200;

  function drawGrid() {
      ctx.strokeStyle = "#eee";
      for(let i=0; i<=10; i++) {
          let y = i * (canvas.height/10);
          ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
      }
  }

  function step() {
      if (frequency <= 0 || frequency >= 1 || gen > canvas.width) return;

      gen += 2;
      let countA = 0;
      
      // Randomly sample for the next generation
      for (let i = 0; i < populationSize; i++) {
          if (Math.random() < frequency) countA++;
      }
      
      frequency = countA / populationSize;
      
      // Draw the "Step"
      let newX = gen;
      let newY = canvas.height - (frequency * canvas.height);
      
      ctx.strokeStyle = frequency > 0.5 ? "#3498db" : "#e74c3c";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(prevX, prevY);
      ctx.lineTo(newX, newY);
      ctx.stroke();

      prevX = newX; prevY = newY;
      requestAnimationFrame(step);
  }

  function resetSimulation() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      drawGrid();
      frequency = 0.5; gen = 0; prevX = 0; prevY = 200;
      step();
  }

  drawGrid();
  step();
</script>