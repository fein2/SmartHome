# Smart Home Energy Optimiser

A Python project that simulates an advanced energy management system for a smart home. This optimiser makes proactive decisions based on a simulated 24-hour energy price forecast and a home battery storage system.

## Features

* **Proactive Optimisation:** The script uses a simulated 24-hour forecast to make proactive decisions, rather than simply reacting to a real-time price. This showcases a more sophisticated approach to energy management.

* **Battery Storage Logic:** The optimiser includes logic to charge a home battery during low-price periods and discharge it to power devices during high-price periods, which is crucial for grid stability.

* **Multi-Setting Device Control:** The simulated thermostat can be set to different modes (`default`, `conserve`, `pre-cool`) based on the forecasted price, allowing for more nuanced control than a simple on/off switch.

* **Simulated Real-World Pricing:** The project's pricing data is not random but is patterned to realistically mimic peak and off-peak periods, providing a more authentic demonstration of the optimiser's capabilities.

## How to Run

1. Ensure you have Python installed.

2. Run the script from your terminal: `python optimiser_advanced.py`

## Next Steps

This project provides a robust foundation for a full-scale application. Further improvements could include:

* **Interactive Dashboard:** Create a simple web interface to visualise the forecast and the optimiser's decisions.

* **Simulated Weather Data:** Add another simulated data source for outside temperature to make the optimiser's decisions more realistic.

* **Multiple Devices:** Expand the optimiser to manage multiple devices like a hot water system or a pool pump.