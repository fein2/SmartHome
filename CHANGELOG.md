changelog = """
# Changelog

All notable changes to this project will be documented in this file.  
This project follows [Semantic Versioning](https://semver.org/).

---

## [v1.2.0] - 2025-08-20
### Added
- **Baseline vs Optimiser Comparison**: Implemented benchmark testing against a baseline scenario to measure cost savings, peak demand reduction, and carbon impact.  
- **Performance Results**:  
  - Cost reduced by **17.5%** compared to baseline.  
  - Evening peak demand (kWh) reduced by **73.9%**, demonstrating load shifting effectiveness.  
  - Carbon emissions tracking extended with more accurate reporting.  
- **Documentation Update**: README updated with results, visuals, and clearer explanation of system behaviour.  

### Changed
- Improved EV charging logic for more efficient scheduling across off-peak and solar generation periods.  
- Refined thermostat and battery coordination logic for better demand response at peak times.  

---

## [v1.1.0] - 2025-08-05
### Added
- **Electric Vehicle (EV) Charger Integration**: Accounts for charging schedules, prioritising off-peak and solar surplus energy.  
- **Carbon Emission Tracking**: Reports emissions associated with energy use, providing clearer environmental insights.  

### Changed
- Optimisation logic improved for better scheduling recommendations and more reliable performance.  

---

## [v1.0.0] - 2025-07-22
### Initial Release
- **Core Smart Home Energy Optimiser** with:  
  - Proactive 24-hour energy price forecast usage.  
  - Battery storage system simulation with charge/discharge logic.  
  - Thermostat with multi-mode settings (default, conserve, pre-cool).  
  - Realistic simulated pricing with peak/off-peak patterns.  

---
"""
