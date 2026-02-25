const axios = require("axios");
const fs = require("fs");

const N = 20; // number of trials
const API_URL = "http://localhost:3001/generate"; // adjust if your route is different

const sampleEmail = `
Hi Shreesha,

Thanks for reaching out. We'd love to schedule a quick call to discuss the opportunity further.
Let us know your availability this week.

Best,
Recruiter
`;

async function runBenchmark() {
  const results = [];

  for (let i = 0; i < N; i++) {
    const start = Date.now();


await axios.post(API_URL, {
  emailText: sampleEmail,
  tone: "professional"
});

    const end = Date.now();
    const latency = end - start;
    console.log(`Run ${i + 1}: ${latency} ms`);
    results.push(latency);
  }

  const sorted = [...results].sort((a, b) => a - b);
  const median = sorted[Math.floor(N / 2)];
  const p95 = sorted[Math.floor(N * 0.95)];

  const summary = {
    trials: N,
    median_ms: median,
    p95_ms: p95,
    all_runs: results
  };

  fs.writeFileSync("results/latency.json", JSON.stringify(summary, null, 2));

  console.log("\nBenchmark complete:");
  console.log(summary);
}

runBenchmark();
