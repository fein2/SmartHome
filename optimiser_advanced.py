import time
import random
import datetime

# --- Simulating a Smart Device with Multiple Settings ---
thermostat = {
    "status": "on",
    "setting": "default",
    "temperature_default": 22,
    "temperature_conserve": 25,
    "temperature_pre_cool": 20
}

# --- Simulating a Home Battery Storage System ---
battery = {
    "capacity_kwh": 10,
    "current_charge_kwh": 5,
    "charge_rate_kw": 2,
    "discharge_rate_kw": 3
}

def get_24_hour_forecast():
    """
    Simulates a 24-hour energy price forecast.
    This replaces a real predictive model, demonstrating the concept.
    The prices are patterned to mimic real-world peak/off-peak pricing.
    """
    forecast = []
    for hour in range(24):
        # Peak prices between 4 PM and 9 PM
        if 16 <= hour < 21:
            base_price = 0.45
            variation = random.uniform(-0.05, 0.05)
        # Off-peak prices between 10 PM and 7 AM
        elif 22 <= hour or hour < 7:
            base_price = 0.15
            variation = random.uniform(-0.02, 0.02)
        # Standard prices during the day
        else:
            base_price = 0.25
            variation = random.uniform(-0.03, 0.03)
        
        forecast.append(round(base_price + variation, 2))
    return forecast

def optimise_energy_usage(forecast):
    """
    Main function to optimise energy usage based on a 24-hour forecast
    and the status of a home battery. This logic is proactive and prioritises
    charging the battery during low-price periods.
    """
    print("Starting smart home optimiser with a 24-hour forecast and battery storage...")
    
    # This loop runs once every hour to simulate the daily optimisation
    for hour, forecasted_price in enumerate(forecast):
        print(f"\n--- Optimising for hour {hour}:00 ---")
        print(f"Forecasted price: ${forecasted_price:.2f} per kWh")
        print(f"Battery charge: {battery['current_charge_kwh']:.2f} kWh / {battery['capacity_kwh']} kWh")

        # --- Advanced Optimisation Logic with Battery ---
        
        if forecasted_price < 0.20 and battery["current_charge_kwh"] < battery["capacity_kwh"]:
            battery["current_charge_kwh"] += battery["charge_rate_kw"]
            # Ensure the charge doesn't exceed capacity
            battery["current_charge_kwh"] = min(battery["current_charge_kwh"], battery["capacity_kwh"])
            print("Price is low. Charging the home battery.")
        
        if forecasted_price > 0.40:
            # If the price is very high, use the battery or turn off
            if battery["current_charge_kwh"] > 0:
                print("Price is very high. Thermostat will run from battery.")
                thermostat["status"] = "on"
                thermostat["setting"] = "conserve"
                battery["current_charge_kwh"] -= battery["discharge_rate_kw"]
                # Ensure the charge doesn't go below zero
                battery["current_charge_kwh"] = max(battery["current_charge_kwh"], 0)
            else:
                if thermostat["setting"] != "off":
                    thermostat["status"] = "off"
                    thermostat["setting"] = "off"
                    print("Price is very high and battery is empty. Thermostat is turned off to save energy.")
        
        # If the price is high, use the 'conserve' setting and run from battery if available
        elif forecasted_price > 0.30:
            if battery["current_charge_kwh"] > 0 and thermostat["setting"] != "conserve":
                thermostat["status"] = "on"
                thermostat["setting"] = "conserve"
                print(f"Price is high. Thermostat set to conserve mode ({thermostat['temperature_conserve']}°C), running from battery.")
                battery["current_charge_kwh"] -= battery["discharge_rate_kw"]
                battery["current_charge_kwh"] = max(battery["current_charge_kwh"], 0)
            elif thermostat["setting"] != "conserve":
                thermostat["status"] = "on"
                thermostat["setting"] = "conserve"
                print(f"Price is high. Thermostat set to conserve mode ({thermostat['temperature_conserve']}°C), running from grid.")

        # If the price is low, use the 'pre-cool' setting and charge battery
        elif forecasted_price < 0.20:
            next_hour_price = forecast[(hour + 1) % 24]
            if next_hour_price > 0.30 and thermostat["setting"] != "pre-cool":
                thermostat["status"] = "on"
                thermostat["setting"] = "pre-cool"
                print(f"Price is low, and a peak is coming. Thermostat set to pre-cool ({thermostat['temperature_pre_cool']}°C).")
            elif thermostat["setting"] != "default":
                thermostat["status"] = "on"
                thermostat["setting"] = "default"
                print(f"Price is low. Thermostat set to default mode ({thermostat['temperature_default']}°C).")

        # Otherwise, use the default setting
        else:
            if thermostat["setting"] != "default":
                thermostat["status"] = "on"
                thermostat["setting"] = "default"
                print(f"Price is normal. Thermostat set to default mode ({thermostat['temperature_default']}°C).")
                
        time.sleep(3) # Wait 3 seconds per simulated hour

if __name__ == "__main__":
    daily_forecast = get_24_hour_forecast()
    optimise_energy_usage(daily_forecast)
