# qiskit-ghz-entanglement

GHZ (Greenberger–Horne–Zeilinger) state multi-qubit entanglement using Qiskit.

## What This Shows

A **GHZ state** is a maximally entangled quantum state involving 3 or more qubits. For 3 qubits:

|GHZ⟩ = (|000⟩ + |111⟩) / √2

All qubits are perfectly correlated — measuring one instantly determines the state of all others.

## Circuit

```
q0: ──H──■────────
         │
q1: ─────■──■────
              │
q2: ──────────■──
```

- Hadamard on q0 creates superposition
- CNOT q0→q1 entangles q0 and q1
- CNOT q1→q2 entangles all three

## Files

- `ghz_state.py` — GHZ circuit with statevector simulation and measurement

## Requirements

```bash
pip install qiskit qiskit-aer
```

## Run

```bash
python ghz_state.py
```

## Key Concepts

- **GHZ State**: Maximally entangled multi-qubit state
- **Multi-qubit Entanglement**: Correlations across 3+ qubits
- **Non-locality**: Measurement of one qubit affects all others instantly
- **Quantum Advantage**: GHZ states are used in quantum teleportation, cryptography, and error correction

## Part of

A series of Qiskit learning projects exploring quantum computing fundamentals.
