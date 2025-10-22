// Test calculations for capacitor calculator
// Verifying math for all combinations

console.log("=".repeat(80));
console.log("CAPACITOR CALCULATOR - MATH VERIFICATION");
console.log("=".repeat(80));

function testCalculation(phaseType, kvar, voltage, frequency, connectionType) {
    console.log("\n" + "-".repeat(80));
    console.log(`Test: ${phaseType.toUpperCase()} Phase, ${connectionType.toUpperCase()}, ${kvar} kVAR, ${voltage}V, ${frequency}Hz`);
    console.log("-".repeat(80));
    
    const omega = 2 * Math.PI * frequency;
    const qVar = kvar * 1000;
    
    console.log(`ω (angular frequency) = 2π × ${frequency} = ${omega.toFixed(4)} rad/s`);
    console.log(`Q (reactive power) = ${kvar} × 1000 = ${qVar} VAR`);
    
    let capacitanceMicrofarads;
    let singleCapMicrofarads;
    let deltaEquivalentMicrofarads;
    
    if (phaseType === 'single') {
        // Single phase: C = Q / (ω * V²)
        capacitanceMicrofarads = (qVar / (omega * voltage * voltage)) * 1e6;
        
        console.log(`\nFormula: C = Q / (ω × V²)`);
        console.log(`C = ${qVar} / (${omega.toFixed(4)} × ${voltage}²)`);
        console.log(`C = ${qVar} / (${omega.toFixed(4)} × ${voltage * voltage})`);
        console.log(`C = ${(qVar / (omega * voltage * voltage)).toExponential(6)} F`);
        console.log(`C = ${capacitanceMicrofarads.toFixed(2)} µF`);
        
        // Verify: Q = ω * C * V²
        const verifyQ = omega * (capacitanceMicrofarads * 1e-6) * voltage * voltage;
        console.log(`\nVerification: Q = ω × C × V²`);
        console.log(`Q = ${omega.toFixed(4)} × ${(capacitanceMicrofarads * 1e-6).toExponential(6)} × ${voltage}²`);
        console.log(`Q = ${verifyQ.toFixed(2)} VAR (should equal ${qVar} VAR)`);
        console.log(`Error: ${Math.abs(verifyQ - qVar).toFixed(6)} VAR (${((Math.abs(verifyQ - qVar) / qVar) * 100).toFixed(8)}%)`);
        
    } else if (connectionType === 'delta') {
        // For delta: Each capacitor sees line voltage
        // Total Q = 3 * ω * C * V²
        singleCapMicrofarads = (qVar / (3 * omega * voltage * voltage)) * 1e6;
        deltaEquivalentMicrofarads = (3 * singleCapMicrofarads) / 2;
        capacitanceMicrofarads = singleCapMicrofarads;
        
        console.log(`\nFormula (Delta): C_per_phase = Q / (3 × ω × V_line²)`);
        console.log(`C = ${qVar} / (3 × ${omega.toFixed(4)} × ${voltage}²)`);
        console.log(`C = ${qVar} / (3 × ${omega.toFixed(4)} × ${voltage * voltage})`);
        console.log(`C = ${qVar} / ${(3 * omega * voltage * voltage).toFixed(2)}`);
        console.log(`C_single = ${singleCapMicrofarads.toFixed(2)} µF (per phase)`);
        console.log(`C_delta_measured = ${deltaEquivalentMicrofarads.toFixed(2)} µF (line-to-line measurement)`);
        
        // Verify: Q = 3 * ω * C * V²
        const verifyQ = 3 * omega * (singleCapMicrofarads * 1e-6) * voltage * voltage;
        console.log(`\nVerification: Q = 3 × ω × C × V_line²`);
        console.log(`Q = 3 × ${omega.toFixed(4)} × ${(singleCapMicrofarads * 1e-6).toExponential(6)} × ${voltage}²`);
        console.log(`Q = ${verifyQ.toFixed(2)} VAR (should equal ${qVar} VAR)`);
        console.log(`Error: ${Math.abs(verifyQ - qVar).toFixed(6)} VAR (${((Math.abs(verifyQ - qVar) / qVar) * 100).toFixed(8)}%)`);
        
        console.log(`\nDelta configuration notes:`);
        console.log(`- Each capacitor is rated for line voltage (${voltage}V)`);
        console.log(`- When measuring L1-L2: Two caps in series (C/2) || one cap (C) = 3C/2`);
        console.log(`- Expected multimeter reading: ${deltaEquivalentMicrofarads.toFixed(2)} µF`);
        
    } else { // wye
        const phaseVoltage = voltage / Math.sqrt(3);
        capacitanceMicrofarads = (qVar / (3 * omega * phaseVoltage * phaseVoltage)) * 1e6;
        
        console.log(`\nFormula (Wye): C_per_phase = Q / (3 × ω × V_phase²)`);
        console.log(`V_phase = V_line / √3 = ${voltage} / ${Math.sqrt(3).toFixed(4)} = ${phaseVoltage.toFixed(4)} V`);
        console.log(`C = ${qVar} / (3 × ${omega.toFixed(4)} × ${phaseVoltage.toFixed(4)}²)`);
        console.log(`C = ${qVar} / (3 × ${omega.toFixed(4)} × ${(phaseVoltage * phaseVoltage).toFixed(2)})`);
        console.log(`C = ${qVar} / ${(3 * omega * phaseVoltage * phaseVoltage).toFixed(2)}`);
        console.log(`C = ${capacitanceMicrofarads.toFixed(2)} µF (per phase)`);
        
        // Verify: Q = 3 * ω * C * Vph²
        const verifyQ = 3 * omega * (capacitanceMicrofarads * 1e-6) * phaseVoltage * phaseVoltage;
        console.log(`\nVerification: Q = 3 × ω × C × V_phase²`);
        console.log(`Q = 3 × ${omega.toFixed(4)} × ${(capacitanceMicrofarads * 1e-6).toExponential(6)} × ${phaseVoltage.toFixed(4)}²`);
        console.log(`Q = ${verifyQ.toFixed(2)} VAR (should equal ${qVar} VAR)`);
        console.log(`Error: ${Math.abs(verifyQ - qVar).toFixed(6)} VAR (${((Math.abs(verifyQ - qVar) / qVar) * 100).toFixed(8)}%)`);
        
        console.log(`\nWye configuration notes:`);
        console.log(`- Each capacitor is rated for phase voltage (${phaseVoltage.toFixed(2)}V)`);
        console.log(`- Capacitors are connected line-to-neutral`);
    }
    
    // Calculate discharge resistance
    const targetVoltage = 50;
    const timeSeconds = 300;
    const capacitanceFarads = capacitanceMicrofarads * 1e-6;
    let dischargeResistance = 0;
    
    if (voltage > targetVoltage) {
        dischargeResistance = -timeSeconds / (capacitanceFarads * Math.log(targetVoltage / voltage));
        
        console.log(`\n${"=".repeat(40)}`);
        console.log(`DISCHARGE RESISTANCE CALCULATION`);
        console.log(`${"=".repeat(40)}`);
        console.log(`Formula: V(t) = V₀ × e^(-t/RC)`);
        console.log(`Solving for R: R = -t / (C × ln(V_target/V₀))`);
        console.log(`\nGiven:`);
        console.log(`  V₀ = ${voltage} V (initial voltage)`);
        console.log(`  V_target = ${targetVoltage} V (target voltage)`);
        console.log(`  t = ${timeSeconds} s (5 minutes)`);
        console.log(`  C = ${(capacitanceFarads * 1e6).toFixed(2)} µF = ${capacitanceFarads.toExponential(6)} F`);
        console.log(`\nCalculation:`);
        console.log(`  ln(${targetVoltage}/${voltage}) = ${Math.log(targetVoltage / voltage).toFixed(6)}`);
        console.log(`  R = -${timeSeconds} / (${capacitanceFarads.toExponential(6)} × ${Math.log(targetVoltage / voltage).toFixed(6)})`);
        console.log(`  R = ${dischargeResistance.toFixed(2)} Ω`);
        
        if (dischargeResistance >= 1e6) {
            console.log(`  R = ${(dischargeResistance / 1e6).toFixed(2)} MΩ`);
        } else if (dischargeResistance >= 1e3) {
            console.log(`  R = ${(dischargeResistance / 1e3).toFixed(2)} kΩ`);
        }
        
        // Verify discharge
        const verifyVoltage = voltage * Math.exp(-timeSeconds / (dischargeResistance * capacitanceFarads));
        console.log(`\nVerification: V(${timeSeconds}s) = ${voltage} × e^(-${timeSeconds}/(${dischargeResistance.toFixed(2)} × ${capacitanceFarads.toExponential(6)}))`);
        console.log(`V(${timeSeconds}s) = ${verifyVoltage.toFixed(2)} V (should equal ${targetVoltage} V)`);
        console.log(`Error: ${Math.abs(verifyVoltage - targetVoltage).toFixed(6)} V`);
    }
}

// Test cases
console.log("\n\n");
console.log("TEST CASE 1: Default Values");
testCalculation('single', 1, 690, 60, 'delta');

console.log("\n\n");
console.log("TEST CASE 2: Three Phase Delta");
testCalculation('three', 1, 690, 60, 'delta');

console.log("\n\n");
console.log("TEST CASE 3: Three Phase Wye");
testCalculation('three', 1, 690, 60, 'wye');

console.log("\n\n");
console.log("TEST CASE 4: Single Phase - Higher kVAR");
testCalculation('single', 10, 480, 60, 'delta');

console.log("\n\n");
console.log("TEST CASE 5: Three Phase Delta - 50Hz European");
testCalculation('three', 5, 400, 50, 'delta');

console.log("\n\n");
console.log("TEST CASE 6: Three Phase Wye - 50Hz European");
testCalculation('three', 5, 400, 50, 'wye');

console.log("\n\n");
console.log("TEST CASE 7: Single Phase - Low Voltage");
testCalculation('single', 2, 240, 60, 'delta');

console.log("\n\n");
console.log("TEST CASE 8: Three Phase Delta - High Power");
testCalculation('three', 25, 480, 60, 'delta');

console.log("\n\n");
console.log("=".repeat(80));
console.log("ALL TESTS COMPLETED");
console.log("=".repeat(80));
