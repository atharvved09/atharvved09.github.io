---
layout: default
title: Multi Random Walk
---

<h2>Evolutionary Random Walk Simulator</h2>

<div class="panel" style="background:#111;padding:20px;border-radius:12px;margin-bottom:20px;display:flex;gap:20px;align-items:center;color:#e6eef6;">
    <div>
        <label>Pop. Size:</label>
        <input type="number" id="popInput" value="50">
    </div>
    <div>
        <label>Simulations:</label>
        <input type="number" id="simInput" value="10">
    </div>
    <button class="run-btn" onclick="runSimulations()">Run Simulations</button>
    <button class="clear-btn" onclick="clearCanvas()">Clear Board</button>
</div>

<div class="canvas-wrap">
  <canvas id="driftCanvas" width="900" height="500" style="background:#222;border-radius:8px;border:2px solid #444;"></canvas>
</div>

<style>
  input { padding: 8px; border-radius: 4px; border: none; width: 60px; }
  button { padding: 10px 20px; cursor: pointer; border-radius: 6px; border: none; font-weight: bold; }
  .run-btn { background: #2ecc71; color: white; }
  .clear-btn { background: #e74c3c; color: white; }
</style>

<script>
  const canvas = document.getElementById('driftCanvas');
  const ctx = canvas.getContext('2d');

  function clearCanvas() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      drawGrid();
  }

  function drawGrid() {
      ctx.strokeStyle = "#333";
      ctx.lineWidth = 1;
      for(let i=0; i<=10; i++) {
          let y = i * (canvas.height/10);
          ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
          // Add percentage labels
          ctx.fillStyle = "#555";
          ctx.fillText((100 - i*10) + "%", 5, y - 5);
      }
  }

  async function runSimulations() {
      const popSize = parseInt(document.getElementById('popInput').value);
      const numSims = parseInt(document.getElementById('simInput').value);
      
      for(let i = 0; i < numSims; i++) {
          // Generate a random bright color for each walk
          const color = `hsl(${Math.random() * 360}, 70%, 60%)`;
          simulateWalk(popSize, color);
      }
  }

  function simulateWalk(popSize, color) {
      let frequency = 0.5;
      let gen = 0;
      let prevX = 0;
      let prevY = canvas.height / 2;
      const stepWidth = 3;

      function drawStep() {
          if (frequency <= 0 || frequency >= 1 || gen > canvas.width) return;

          gen += stepWidth;
          let countA = 0;
          
          // The Biological Random Walk (Binomial Sampling)
          for (let i = 0; i < popSize; i++) {
              if (Math.random() < frequency) countA++;
          }
          
          frequency = countA / popSize;
          
          let newX = gen;
          let newY = canvas.height - (frequency * canvas.height);
          
          ctx.strokeStyle = color;
          ctx.globalAlpha = 0.6; // Slight transparency to see overlapping lines
          ctx.lineWidth = 1.5;
          ctx.beginPath();
          ctx.moveTo(prevX, prevY);
          ctx.lineTo(newX, newY);
          ctx.stroke();

          prevX = newX;
          prevY = newY;

          // Using requestAnimationFrame to make it "race" across the screen
          requestAnimationFrame(drawStep);
      }
      drawStep();
  }

  drawGrid();
</script>