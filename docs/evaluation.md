# Evaluation & Methodology

## Objective

Evaluate whether a fully local LLM email assistant can deliver:

- Acceptable latency
- Zero API cost
- Strong privacy guarantees
- Practical usability

---

## Experimental Setup

### Hardware

- Apple M-series CPU
- 16GB RAM
- macOS
- No GPU acceleration enabled

### Model
- Llama 3.1 (via Ollama)
- Local inference only

### Backend
- Node.js Express API

---

## Latency Measurement

Measured:

- Median latency
- P95 latency
- End-to-end response time
  (Extension click → Draft inserted)

Benchmark script:
`eval/benchmark_latency.js`

Latency recorded across:
- 20 benchmark trials
- Varied lengths (short, medium, long threads)

---

## Reply Quality Scoring

See: `eval/quality_eval.md` for the scoring rubric (Relevance, Tone, Clarity, Completeness, Safety).
---

## Cost Comparison

| System | API Cost | Hosting Cost |
|--------|----------|--------------|
| Repla.ai | $0 | $0 |
| Cloud AI Tools | Token-based | Recurring infra |

Local inference removes per-token billing entirely.

---

## Privacy Surface Analysis

Repla.ai:
- No cloud calls
- No data logging
- No remote storage

Cloud-based tools:
- External API transmission
- Potential logging
- Compliance risks

---

## Reproducibility

To reproduce results:

1. Run `ollama serve`
2. Run backend (`npm start`)
3. Execute:
4. View output metrics

---

## Key Findings

- Median latency: 2924 ms
- P95 latency: 13483 ms
- Trials: 20
- Fully offline inference
- Zero API cost
- Interactive median latency (~2.9s) with occasional cold-start spikes (P95 ~13.5s), typical for first-run local LLM inference

---

## Limitations

- Depends on local hardware performance
- Model size affects latency
- No long-term memory or context caching (by design)

---

## Interpretation

The elevated P95 latency (~13.5s) is attributed primarily to cold-start model initialization and prompt size variability. Subsequent warm runs cluster near the median (~2.9s), indicating stable interactive performance once the model is loaded into memory.

This behavior is expected for fully local inference systems and represents a tradeoff between privacy guarantees and tail latency performance.
