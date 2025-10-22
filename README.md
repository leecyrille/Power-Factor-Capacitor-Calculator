# Nominal Test Capacitance Calculator

A professional web-based calculator for determining capacitor values and discharge resistances in power system applications.

## Features

- **Single Phase & Three Phase Calculations**
  - Single phase / per capacitor calculations
  - Three phase bank calculations (Delta and Wye configurations)

- **Accurate Capacitance Calculations**
  - Per-phase capacitor values
  - Delta configuration multimeter measurements
  - Wye configuration values

- **Discharge Resistance Calculations**
  - Line-to-line discharge resistance
  - Line-to-neutral discharge resistance (for Wye)
  - Calculated to discharge from operating voltage to under 50V in 5 minutes

- **Real-Time Updates**
  - Automatic calculation on input change
  - No button clicks needed

- **Professional Design**
  - Pace Technologies branding
  - Responsive layout for mobile and desktop
  - Accessible interface with ARIA support

## Usage

Simply open `index.html` in any modern web browser. The calculator will:

1. Default to 3-phase Delta configuration at 600V, 60Hz, 1 kVAR
2. Update results automatically as you change any input
3. Display capacitance values with 4 decimal precision
4. Show appropriate discharge resistance values based on configuration

## Input Parameters

- **System Type**: Single Phase/Per Capacitor or Three Phase Bank
- **Reactive Power (kVAR)**: Total bank reactive power for 3-phase, individual capacitor power for single phase
- **Voltage (V)**: Line-to-line voltage for 3-phase, applied voltage for single phase
- **Frequency (Hz)**: System frequency (typically 50 or 60 Hz)
- **Connection Type**: Delta (Δ) or Wye (Y) - only applicable for three phase banks

## Formulas Used

### Capacitance Calculations

**Single Phase:**
```
C = Q / (ω × V²)
```

**Three Phase Delta (per phase):**
```
C = Q / (3 × ω × V_LL²)
Delta measurement = 1.5 × C (for multimeter testing)
```

**Three Phase Wye (per phase):**
```
C = Q / (3 × ω × V_phase²)
where V_phase = V_LL / √3
```

### Discharge Resistance Calculations

**Equivalent Capacitance:**
- Single phase: `C_eq = C`
- Delta (L-L): `C_eq = 1.5 × C_phase`
- Wye (L-L): `C_eq = 0.5 × C_phase`
- Wye (L-N): `C_eq = C_phase`

**Resistance:**
```
R = -t / (C_eq × ln(V_target / V_0))
where t = 300s, V_target = 50V
```

## Technical Details

- Pure HTML/CSS/JavaScript - no dependencies
- Works offline
- Client-side calculations only
- Mathematical precision validated with test cases

## Credits

© 2025 Lee Maskell - Pace Technologies Inc.

## License

Proprietary - Pace Technologies Inc.
