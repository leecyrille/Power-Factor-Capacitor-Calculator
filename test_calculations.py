"""
Test calculations for capacitor calculator
Verifying math for all combinations
"""

import math

def test_calculation(phase_type, kvar, voltage, frequency, connection_type):
    print("\n" + "="*80)
    print(f"Test: {phase_type.upper()} Phase, {connection_type.upper()}, {kvar} kVAR, {voltage}V, {frequency}Hz")
    print("="*80)
    
    omega = 2 * math.pi * frequency
    q_var = kvar * 1000
    
    print(f"ω (angular frequency) = 2π × {frequency} = {omega:.4f} rad/s")
    print(f"Q (reactive power) = {kvar} × 1000 = {q_var} VAR")
    
    capacitance_microfarads = 0
    single_cap_microfarads = 0
    delta_equivalent_microfarads = 0
    
    if phase_type == 'single':
        # Single phase: C = Q / (ω * V²)
        capacitance_microfarads = (q_var / (omega * voltage * voltage)) * 1e6
        
        print(f"\nFormula: C = Q / (ω × V²)")
        print(f"C = {q_var} / ({omega:.4f} × {voltage}²)")
        print(f"C = {q_var} / ({omega:.4f} × {voltage * voltage})")
        print(f"C = {(q_var / (omega * voltage * voltage)):.6e} F")
        print(f"C = {capacitance_microfarads:.2f} µF")
        
        # Verify: Q = ω * C * V²
        verify_q = omega * (capacitance_microfarads * 1e-6) * voltage * voltage
        print(f"\nVerification: Q = ω × C × V²")
        print(f"Q = {omega:.4f} × {(capacitance_microfarads * 1e-6):.6e} × {voltage}²")
        print(f"Q = {verify_q:.2f} VAR (should equal {q_var} VAR)")
        print(f"Error: {abs(verify_q - q_var):.6f} VAR ({(abs(verify_q - q_var) / q_var * 100):.8f}%)")
        
    elif connection_type == 'delta':
        # For delta: Each capacitor sees line voltage
        # Total Q = 3 * ω * C * V²
        single_cap_microfarads = (q_var / (3 * omega * voltage * voltage)) * 1e6
        delta_equivalent_microfarads = (3 * single_cap_microfarads) / 2
        capacitance_microfarads = single_cap_microfarads
        
        print(f"\nFormula (Delta): C_per_phase = Q / (3 × ω × V_line²)")
        print(f"C = {q_var} / (3 × {omega:.4f} × {voltage}²)")
        print(f"C = {q_var} / (3 × {omega:.4f} × {voltage * voltage})")
        print(f"C = {q_var} / {(3 * omega * voltage * voltage):.2f}")
        print(f"C_single = {single_cap_microfarads:.2f} µF (per phase)")
        print(f"C_delta_measured = {delta_equivalent_microfarads:.2f} µF (line-to-line measurement)")
        
        # Verify: Q = 3 * ω * C * V²
        verify_q = 3 * omega * (single_cap_microfarads * 1e-6) * voltage * voltage
        print(f"\nVerification: Q = 3 × ω × C × V_line²")
        print(f"Q = 3 × {omega:.4f} × {(single_cap_microfarads * 1e-6):.6e} × {voltage}²")
        print(f"Q = {verify_q:.2f} VAR (should equal {q_var} VAR)")
        print(f"Error: {abs(verify_q - q_var):.6f} VAR ({(abs(verify_q - q_var) / q_var * 100):.8f}%)")
        
        print(f"\nDelta configuration notes:")
        print(f"- Each capacitor is rated for line voltage ({voltage}V)")
        print(f"- When measuring L1-L2: Two caps in series (C/2) || one cap (C) = 3C/2")
        print(f"- Expected multimeter reading: {delta_equivalent_microfarads:.2f} µF")
        
    else:  # wye
        phase_voltage = voltage / math.sqrt(3)
        capacitance_microfarads = (q_var / (3 * omega * phase_voltage * phase_voltage)) * 1e6
        
        print(f"\nFormula (Wye): C_per_phase = Q / (3 × ω × V_phase²)")
        print(f"V_phase = V_line / √3 = {voltage} / {math.sqrt(3):.4f} = {phase_voltage:.4f} V")
        print(f"C = {q_var} / (3 × {omega:.4f} × {phase_voltage:.4f}²)")
        print(f"C = {q_var} / (3 × {omega:.4f} × {(phase_voltage * phase_voltage):.2f})")
        print(f"C = {q_var} / {(3 * omega * phase_voltage * phase_voltage):.2f}")
        print(f"C = {capacitance_microfarads:.2f} µF (per phase)")
        
        # Verify: Q = 3 * ω * C * Vph²
        verify_q = 3 * omega * (capacitance_microfarads * 1e-6) * phase_voltage * phase_voltage
        print(f"\nVerification: Q = 3 × ω × C × V_phase²")
        print(f"Q = 3 × {omega:.4f} × {(capacitance_microfarads * 1e-6):.6e} × {phase_voltage:.4f}²")
        print(f"Q = {verify_q:.2f} VAR (should equal {q_var} VAR)")
        print(f"Error: {abs(verify_q - q_var):.6f} VAR ({(abs(verify_q - q_var) / q_var * 100):.8f}%)")
        
        print(f"\nWye configuration notes:")
        print(f"- Each capacitor is rated for phase voltage ({phase_voltage:.2f}V)")
        print(f"- Capacitors are connected line-to-neutral")
    
    # Calculate discharge resistance
    target_voltage = 50
    time_seconds = 300
    capacitance_farads = capacitance_microfarads * 1e-6
    
    if voltage > target_voltage:
        discharge_resistance = -time_seconds / (capacitance_farads * math.log(target_voltage / voltage))
        
        print(f"\n{'='*40}")
        print(f"DISCHARGE RESISTANCE CALCULATION")
        print(f"{'='*40}")
        print(f"Formula: V(t) = V₀ × e^(-t/RC)")
        print(f"Solving for R: R = -t / (C × ln(V_target/V₀))")
        print(f"\nGiven:")
        print(f"  V₀ = {voltage} V (initial voltage)")
        print(f"  V_target = {target_voltage} V (target voltage)")
        print(f"  t = {time_seconds} s (5 minutes)")
        print(f"  C = {(capacitance_farads * 1e6):.2f} µF = {capacitance_farads:.6e} F")
        print(f"\nCalculation:")
        print(f"  ln({target_voltage}/{voltage}) = {math.log(target_voltage / voltage):.6f}")
        print(f"  R = -{time_seconds} / ({capacitance_farads:.6e} × {math.log(target_voltage / voltage):.6f})")
        print(f"  R = {discharge_resistance:.2f} Ω")
        
        if discharge_resistance >= 1e6:
            print(f"  R = {(discharge_resistance / 1e6):.2f} MΩ")
        elif discharge_resistance >= 1e3:
            print(f"  R = {(discharge_resistance / 1e3):.2f} kΩ")
        
        # Verify discharge
        verify_voltage = voltage * math.exp(-time_seconds / (discharge_resistance * capacitance_farads))
        print(f"\nVerification: V({time_seconds}s) = {voltage} × e^(-{time_seconds}/({discharge_resistance:.2f} × {capacitance_farads:.6e}))")
        print(f"V({time_seconds}s) = {verify_voltage:.2f} V (should equal {target_voltage} V)")
        print(f"Error: {abs(verify_voltage - target_voltage):.6f} V")


if __name__ == "__main__":
    print("\n" + "="*80)
    print("CAPACITOR CALCULATOR - MATH VERIFICATION")
    print("="*80)
    
    # Test cases
    print("\n\nTEST CASE 1: Default Values (Single Phase)")
    test_calculation('single', 1, 690, 60, 'delta')
    
    print("\n\nTEST CASE 2: Three Phase Delta")
    test_calculation('three', 1, 690, 60, 'delta')
    
    print("\n\nTEST CASE 3: Three Phase Wye")
    test_calculation('three', 1, 690, 60, 'wye')
    
    print("\n\nTEST CASE 4: Single Phase - Higher kVAR")
    test_calculation('single', 10, 480, 60, 'delta')
    
    print("\n\nTEST CASE 5: Three Phase Delta - 50Hz European")
    test_calculation('three', 5, 400, 50, 'delta')
    
    print("\n\nTEST CASE 6: Three Phase Wye - 50Hz European")
    test_calculation('three', 5, 400, 50, 'wye')
    
    print("\n\nTEST CASE 7: Single Phase - Low Voltage")
    test_calculation('single', 2, 240, 60, 'delta')
    
    print("\n\nTEST CASE 8: Three Phase Delta - High Power")
    test_calculation('three', 25, 480, 60, 'delta')
    
    print("\n\n" + "="*80)
    print("ALL TESTS COMPLETED")
    print("="*80)
