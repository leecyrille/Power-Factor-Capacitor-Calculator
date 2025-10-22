# Current Measurement Guide

## Understanding the Current Calculations

The calculator now provides expected current measurements to help verify capacitor operation during energized testing.

## What Current is Measured Where?

### Single Phase / Per Capacitor
**Line Current** = Current measured on the wire feeding the capacitor

- Formula: `I = V × ω × C`
- This is the total current through the capacitor
- Measurement location: On either supply wire to the capacitor

**Example:**
- 1 kVAR @ 600V, 60Hz
- Capacitance: 7.37 µF
- **Expected current: 1.67 A**

---

### Three Phase Delta (Δ)

**Line Current** = Current measured on L1, L2, or L3 input line to the bank

- Formula: `I_line = √3 × I_capacitor`
- This is what you measure with a clamp meter on the input lines
- Each line current should be approximately equal

**Capacitor Current** = Current through individual capacitor element

- Formula: `I_capacitor = V_LL × ω × C_phase`
- This would only be measured if you opened the bank and metered inside
- Useful for verifying individual cap health if accessible

**Example:**
- 5 kVAR @ 600V, 60Hz Delta
- Per-phase capacitance: 12.28 µF
- **Capacitor current: 2.78 A**
- **Line current: 4.81 A** ← Measure this on input lines

---

### Three Phase Wye (Y)

**Line Current** = Current measured on L1, L2, or L3 input line to the bank

- Formula: `I = V_phase × ω × C_phase` where `V_phase = V_LL / √3`
- In Wye configuration, line current = capacitor current
- Each line current should be approximately equal

**Example:**
- 3 kVAR @ 600V, 60Hz Wye
- Per-phase capacitance: 22.10 µF
- V_phase: 346.41 V
- **Line current: 2.89 A** ← Measure this on input lines

---

## Field Testing Procedure

### Before Energizing:
1. Input nameplate data into calculator
2. Input actual system voltage (measure at the point of connection)
3. Note the expected line current from calculator

### During Energized Test:
1. **Clamp meter on each input line** (L1, L2, L3 for 3-phase, or line wire for single phase)
2. Compare measured current to expected current
3. All three phases should be balanced (within 5-10% of each other)

### What the Current Tells You:

✅ **Current matches expected (within ±10%):** Capacitor is healthy

⚠️ **Current is low:** 
- Capacitor may be degraded/failed
- Check voltage is actually what you think it is
- Verify frequency

⚠️ **Current is high:**
- Could indicate overvoltage condition
- Check actual voltage
- Calculator shows actual kVAR being delivered

⚠️ **Unbalanced currents (3-phase):**
- One or more capacitor elements may be failed
- In Delta: if one cap fails open, you'll see reduced current
- In Wye: if one cap fails, that phase will show very low/no current

---

## Why Actual Voltage Matters

Capacitors are **voltage-sensitive devices**. The current (and thus kVAR) increases with voltage:

- Current: `I ∝ V` (linear with voltage)
- Reactive power: `Q ∝ V²` (proportional to voltage squared)

**Example:**
- Nameplate: 10 kVAR @ 480V
- Operating at 500V (4.2% overvoltage)
- Expected current increases by 4.2%
- **Actual kVAR delivered: 10.85 kVAR** (8.5% increase!)

This is why the calculator asks for both nameplate and actual voltage.

---

## Common Field Scenarios

### Scenario 1: Nameplate matches system
- Nameplate: 5 kVAR @ 600V
- System voltage: 600V
- Expected current: 4.81 A per line (Delta)

### Scenario 2: System runs hot
- Nameplate: 5 kVAR @ 600V  
- System voltage: 625V (4.2% over)
- Expected current: 5.01 A per line
- Delivering 5.43 kVAR (not 5 kVAR!)

### Scenario 3: Degraded capacitor
- Nameplate: 5 kVAR @ 600V
- System voltage: 600V
- Expected current: 4.81 A
- **Measured current: 3.5 A** ← Problem!
- Indicates capacitor has lost ~27% of capacitance

---

## Delta vs Wye Current Characteristics

### Delta Configuration
- Higher individual capacitor current
- Line current = √3 × capacitor current
- More robust to single element failure (bank still works with one cap open)
- Current imbalance indicates internal failure

### Wye Configuration  
- Lower individual capacitor current (each cap sees phase voltage)
- Line current = capacitor current (easier to understand)
- If one cap fails open, that phase shows ~0 current
- Better for unbalanced load conditions

---

## Quick Reference

| Configuration | Where to Measure | Formula | Notes |
|--------------|------------------|---------|-------|
| **Single Phase** | Line wire | I = V × ω × C | Simple, current = capacitor current |
| **Delta** | Input line (L1/L2/L3) | I_line = √3 × V_LL × ω × C | Line current is 73% higher than cap current |
| **Wye** | Input line (L1/L2/L3) | I_line = V_phase × ω × C | Line current = capacitor current |

---

## Troubleshooting with Current Measurements

| Observation | Possible Cause | Action |
|-------------|----------------|--------|
| All currents low equally | Low voltage, wrong frequency | Verify V and f |
| All currents high equally | High voltage | Check if overvoltage condition |
| One phase low (3φ) | Failed capacitor in that phase | Replace capacitor element |
| All currents ~0 | Capacitor not energized | Check breaker, contactors |
| Erratic/fluctuating | Loose connection, blown fuse | Inspect connections |

---

**Remember:** These are expected values based on nameplate ratings. Always measure actual voltage and compare measured current to calculated expected current for accurate diagnostics.
