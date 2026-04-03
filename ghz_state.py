"""
ghz_state.py
============
Demonstrates a 3-qubit GHZ (Greenberger–Horne–Zeilinger) state using Qiskit.

GHZ State: |GHZ⟩ = (|000⟩ + |111⟩) / √2

All 3 qubits are maximally entangled — measuring one instantly determines
the state of all others (either all 0 or all 1).

Circuit:
  q0: ──H──■────────
           │
  q1: ─────■──■────
                │
  q2: ──────────■──

Requirements:
  pip install qiskit qiskit-aer
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

# ── 1. Build the GHZ circuit ──────────────────────────────────────────────
qc = QuantumCircuit(3, 3)

# Step 1: Hadamard on q0 → creates superposition |0⟩ + |1⟩
qc.h(0)

# Step 2: CNOT q0 → q1  → entangles q0 and q1
qc.cx(0, 1)

# Step 3: CNOT q1 → q2  → entangles all three
qc.cx(1, 2)

print("=" * 55)
print("GHZ State Circuit")
print("=" * 55)
print(qc.draw(output="text"))

# ── 2. Statevector simulation (exact amplitudes) ───────────────────────────
sv = Statevector(qc)

print("\n" + "=" * 55)
print("Statevector (non-zero amplitudes)")
print("=" * 55)
for i, amp in enumerate(sv):
    if abs(amp) > 1e-10:
        label = format(i, "03b")
        print(f"  |{label}⟩  amplitude = {amp:.4f}  prob = {abs(amp)**2:.4f}")

# ── 3. Measurement simulation (shot-based) ───────────────────────────────
qc_meas = qc.copy()
qc_meas.measure([0, 1, 2], [0, 1, 2])

simulator = AerSimulator()
job = simulator.run(qc_meas, shots=1024)
counts = job.result().get_counts()

print("\n" + "=" * 55)
print("Measurement results (1024 shots)")
print("=" * 55)
for state, count in sorted(counts.items()):
    bar = "█" * (count // 20)
    print(f"  |{state}⟩  {count:4d} shots  {bar}")

print("\nKey insight: Only |000⟩ and |111⟩ appear — ")
print("all qubits are always measured in the same state.")
