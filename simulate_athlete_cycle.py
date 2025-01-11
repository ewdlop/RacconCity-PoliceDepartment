import random
from datetime import datetime, timedelta

class Substance:
    def __init__(self, name, detection_window_days, performance_boost, risk_level):
        self.name = name
        self.detection_window = detection_window_days
        self.performance_boost = performance_boost  # 1-100
        self.risk_level = risk_level  # 1-100
        self.side_effects = []

class Athlete:
    def __init__(self, name, base_performance):
        self.name = name
        self.base_performance = base_performance  # 1-100
        self.current_performance = base_performance
        self.substances = []
        self.side_effects = []
        self.last_usage = None
        self.health = 100

def create_substance_database():
    substances = {
        "Testosterone_Propionate": Substance("Testosterone Propionate", 90, 30, 40),
        "Dianabol": Substance("Dianabol", 45, 40, 60),
        "Trenbolone": Substance("Trenbolone", 120, 50, 75),
        "Winstrol": Substance("Winstrol", 30, 35, 45)
    }
    
    # Add side effects
    substances["Testosterone_Propionate"].side_effects = [
        "Reduced natural testosterone",
        "Acne",
        "Hair loss"
    ]
    substances["Dianabol"].side_effects = [
        "Liver strain",
        "Water retention",
        "High blood pressure"
    ]
    substances["Trenbolone"].side_effects = [
        "Insomnia",
        "Increased aggression",
        "Night sweats"
    ]
    substances["Winstrol"].side_effects = [
        "Joint pain",
        "Tendon issues",
        "HDL reduction"
    ]
    
    return substances

def simulate_drug_test(athlete, test_date):
    """Simulate a drug test for an athlete"""
    if not athlete.last_usage or not athlete.substances:
        return "Clean"
    
    days_since_usage = (test_date - athlete.last_usage).days
    
    for substance in athlete.substances:
        if days_since_usage < substance.detection_window:
            return f"Positive for {substance.name}"
    
    return "Clean"

def calculate_performance_impact(athlete):
    """Calculate total performance impact of substances"""
    total_boost = 0
    health_impact = 0
    
    for substance in athlete.substances:
        total_boost += substance.performance_boost
        health_impact += substance.risk_level
        
        # Random chance of developing side effects
        if random.random() < 0.3:  # 30% chance
            new_effect = random.choice(substance.side_effects)
            if new_effect not in athlete.side_effects:
                athlete.side_effects.append(new_effect)
                athlete.health -= random.randint(5, 15)
    
    athlete.current_performance = min(100, athlete.base_performance + total_boost)
    athlete.health = max(0, athlete.health - (health_impact * 0.1))
    
    return total_boost

def simulate_athlete_cycle(athlete, substance, cycle_length_days):
    """Simulate an athlete's performance cycle with a substance"""
    print(f"\nSimulating {cycle_length_days} day cycle for {athlete.name} with {substance.name}")
    
    athlete.substances.append(substance)
    athlete.last_usage = datetime.now()
    
    # Initial impact
    performance_boost = calculate_performance_impact(athlete)
    
    print(f"\nInitial Statistics:")
    print(f"Base Performance: {athlete.base_performance}")
    print(f"Performance Boost: +{performance_boost}")
    print(f"Current Performance: {athlete.current_performance}")
    print(f"Health Level: {athlete.health}")
    
    # Simulate cycle
    for day in range(cycle_length_days):
        if day % 30 == 0:  # Monthly check
            test_result = simulate_drug_test(athlete, athlete.last_usage + timedelta(days=day))
            print(f"\nDay {day} Status:")
            print(f"Drug Test Result: {test_result}")
            print(f"Current Side Effects: {', '.join(athlete.side_effects)}")
            print(f"Health Level: {athlete.health}")

def analyze_risk_reward(athlete):
    """Analyze risk vs reward for current protocol"""
    performance_gain = athlete.current_performance - athlete.base_performance
    health_loss = 100 - athlete.health
    risk_ratio = health_loss / performance_gain if performance_gain > 0 else float('inf')
    
    print("\nRisk/Reward Analysis:")
    print(f"Performance Gain: {performance_gain:.1f}%")
    print(f"Health Impact: -{health_loss:.1f}%")
    print(f"Risk Ratio: {risk_ratio:.2f}")
    
    if risk_ratio < 1:
        return "High reward relative to risk"
    elif risk_ratio < 2:
        return "Moderate risk/reward balance"
    else:
        return "High risk relative to reward"

# Example usage
if __name__ == "__main__":
    # Create substance database
    substances = create_substance_database()
    
    # Create athlete
    athlete = Athlete("Test Athlete", 75)
    
    # Select substance for simulation
    test_substance = substances["Testosterone_Propionate"]
    
    # Run simulation
    simulate_athlete_cycle(athlete, test_substance, 90)
    
    # Analyze results
    result = analyze_risk_reward(athlete)
    print(f"\nFinal Analysis: {result}")
