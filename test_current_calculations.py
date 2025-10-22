"""
Test current calculations for capacitor calculator
"""

import math

def test_current_calculations():
    print("="*80)
    print("CURRENT CALCULATION TESTS")
    print("="*80)
    
    # Test 1: Single Phase
    print("\n" + "-"*80)
    print("TEST 1: Single Phase")
    print("-"*80)
    Q = 1.0  # kVAR
    V_nameplate = 600  # V
    V_actual = 600  # V
    f = 60  # Hz
    
    omega = 2 * math.pi * f
    q_var = Q * 1000
    
    # C = Q / (ω * V²)
    C_uF = (q_var / (omega * V_nameplate * V_nameplate)) * 1e6
    C_F = C_uF * 1e-6
    
    # I = V * ω * C
    I = V_actual * omega * C_F
    
    print(f"Capacitance: {C_uF:.4f} µF")
    print(f"Expected Current @ {V_actual}V: {I:.2f} A")
    print(f"Verification: Q = V × I = {V_actual * I:.2f} VAR (should equal {q_var} VAR)")
    
    # Test 2: Three Phase Delta
    print("\n" + "-"*80)
    print("TEST 2: Three Phase Delta")
    print("-"*80)
    Q = 5.0  # kVAR
    V_nameplate = 600  # V
    V_actual = 600  # V
    f = 60  # Hz
    
    omega = 2 * math.pi * f
    q_var = Q * 1000
    
    # C_phase = Q / (3 * ω * V²)
    C_phase_uF = (q_var / (3 * omega * V_nameplate * V_nameplate)) * 1e6
    C_phase_F = C_phase_uF * 1e-6
    
    # I_capacitor = V_LL * ω * C
    I_cap = V_actual * omega * C_phase_F
    
    # I_line = √3 * I_capacitor
    I_line = math.sqrt(3) * I_cap
    
    print(f"Per-phase Capacitance: {C_phase_uF:.4f} µF")
    print(f"Capacitor Current: {I_cap:.2f} A")
    print(f"Line Current: {I_line:.2f} A")
    print(f"Verification: Q_total = √3 × V_LL × I_line = {math.sqrt(3) * V_actual * I_line:.2f} VAR (should equal {q_var} VAR)")
    
    # Test 3: Three Phase Wye
    print("\n" + "-"*80)
    print("TEST 3: Three Phase Wye")
    print("-"*80)
    Q = 3.0  # kVAR
    V_nameplate = 600  # V
    V_actual = 600  # V
    f = 60  # Hz
    
    omega = 2 * math.pi * f
    q_var = Q * 1000
    V_phase_nameplate = V_nameplate / math.sqrt(3)
    V_phase_actual = V_actual / math.sqrt(3)
    
    # C_phase = Q / (3 * ω * V_phase²)
    C_phase_uF = (q_var / (3 * omega * V_phase_nameplate * V_phase_nameplate)) * 1e6
    C_phase_F = C_phase_uF * 1e-6
    
    # I_line = I_capacitor = V_phase * ω * C
    I_line = V_phase_actual * omega * C_phase_F
    
    print(f"Per-phase Capacitance: {C_phase_uF:.4f} µF")
    print(f"V_phase: {V_phase_actual:.2f} V")
    print(f"Line Current (= Capacitor Current): {I_line:.2f} A")
    print(f"Verification: Q_total = √3 × V_LL × I_line = {math.sqrt(3) * V_actual * I_line:.2f} VAR (should equal {q_var} VAR)")
    
    # Test 4: Different actual voltage
    print("\n" + "-"*80)
    print("TEST 4: Delta with Different Actual Voltage")
    print("-"*80)
    Q = 10.0  # kVAR
    V_nameplate = 480  # V
    V_actual = 500  # V (overvoltage scenario)
    f = 60  # Hz
    
    omega = 2 * math.pi * f
    q_var = Q * 1000
    
    # C_phase = Q / (3 * ω * V_nameplate²) - based on nameplate
    C_phase_uF = (q_var / (3 * omega * V_nameplate * V_nameplate)) * 1e6
    C_phase_F = C_phase_uF * 1e-6
    
    # Current at actual voltage
    I_cap = V_actual * omega * C_phase_F
    I_line = math.sqrt(3) * I_cap
    
    # Actual Q delivered at actual voltage
    Q_actual = math.sqrt(3) * V_actual * I_line
    
    print(f"Nameplate: {Q} kVAR @ {V_nameplate}V")
    print(f"Per-phase Capacitance: {C_phase_uF:.4f} µF")
    print(f"Operating @ {V_actual}V:")
    print(f"  Capacitor Current: {I_cap:.2f} A")
    print(f"  Line Current: {I_line:.2f} A")
    print(f"  Actual kVAR delivered: {Q_actual/1000:.2f} kVAR")
    print(f"  (Note: kVAR increases with voltage squared: {Q * (V_actual/V_nameplate)**2:.2f} kVAR expected)")
    
    print("\n" + "="*80)
    print("ALL CURRENT TESTS COMPLETED")
    print("="*80)

if __name__ == "__main__":
    test_current_calculations()
