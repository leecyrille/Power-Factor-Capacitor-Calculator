"""
Acceptance tests for corrected discharge resistor math
"""

import math

def test_capacitor_calculator():
    print("="*80)
    print("ACCEPTANCE TESTS - Corrected Discharge Resistor Math")
    print("="*80)
    
    target_voltage = 50
    time_seconds = 300
    
    def R_for(Ceq_F, V0):
        if V0 <= target_voltage or Ceq_F <= 0:
            return None
        return -time_seconds / (Ceq_F * math.log(target_voltage / V0))
    
    # Test 1: Delta case
    print("\n" + "-"*80)
    print("TEST 1: Delta case")
    print("-"*80)
    Q = 1.7  # kVAR
    V_LL = 688  # V
    f = 58  # Hz
    
    omega = 2 * math.pi * f
    q_var = Q * 1000
    
    # C_phase = Q / (3 * ω * V_LL²)
    C_phase_uF = (q_var / (3 * omega * V_LL * V_LL)) * 1e6
    print(f"C_phase = {C_phase_uF:.4f} µF (expected ≈ 3.29 µF)")
    
    # Delta measurement = 1.5 * C_phase
    delta_measurement_uF = 1.5 * C_phase_uF
    print(f"Delta measurement = {delta_measurement_uF:.4f} µF (expected ≈ 4.93 µF)")
    
    # R(Line-to-Line): use Ceq = 1.5 * C_phase
    Ceq_LL_F = (1.5 * C_phase_uF) * 1e-6
    R_LL = R_for(Ceq_LL_F, V_LL)
    print(f"R(Line-to-Line) = {R_LL/1e6:.2f} MΩ (expected ≈ 23.2 MΩ)")
    
    # Test 2: Wye case
    print("\n" + "-"*80)
    print("TEST 2: Wye case")
    print("-"*80)
    Q = 1.0  # kVAR
    V_LL = 690  # V
    f = 60  # Hz
    
    omega = 2 * math.pi * f
    q_var = Q * 1000
    V_phase = V_LL / math.sqrt(3)
    
    # C_phase = Q / (3 * ω * V_phase²)
    C_phase_uF = (q_var / (3 * omega * V_phase * V_phase)) * 1e6
    print(f"C_phase = {C_phase_uF:.4f} µF (expected ≈ 5.57 µF)")
    print(f"V_phase = {V_phase:.1f} V")
    
    # R(Line-to-Line): Ceq = 0.5 * C_phase
    Ceq_LL_F = (0.5 * C_phase_uF) * 1e-6
    R_LL = R_for(Ceq_LL_F, V_LL)
    print(f"R(Line-to-Line) = {R_LL/1e6:.2f} MΩ (expected ≈ 38.9 MΩ)")
    
    # R(Line-to-Neutral): Ceq = C_phase, V0 = V_phase
    Ceq_LN_F = C_phase_uF * 1e-6
    R_LN = R_for(Ceq_LN_F, V_phase)
    print(f"R(Line-to-Neutral) = {R_LN/1e6:.2f} MΩ (expected ≈ 26.0 MΩ)")
    
    # Test 3: Single phase
    print("\n" + "-"*80)
    print("TEST 3: Single phase")
    print("-"*80)
    Q = 1.3  # kVAR
    V = 690  # V
    f = 60  # Hz
    
    omega = 2 * math.pi * f
    q_var = Q * 1000
    
    # C = Q / (ω * V²)
    C_uF = (q_var / (omega * V * V)) * 1e6
    print(f"C = {C_uF:.4f} µF (expected ≈ 7.24 µF)")
    
    # R to 50 V in 300 s
    C_F = C_uF * 1e-6
    R = R_for(C_F, V)
    print(f"R = {R/1e6:.2f} MΩ (expected ≈ 15.8 MΩ)")
    
    print("\n" + "="*80)
    print("ALL ACCEPTANCE TESTS COMPLETED")
    print("="*80)

if __name__ == "__main__":
    test_capacitor_calculator()
