# RacconCity-PoliceDepartment

## They did not tell me

```python
import random
import time
from enum import Enum
from typing import List, Dict, Optional

class SecurityLevel(Enum):
    GREEN = 1
    YELLOW = 2
    ORANGE = 3
    RED = 4
    CRITICAL = 5

class FacilityArea(Enum):
    ENTRANCE = "Main Entrance"
    LABS = "Research Labs"
    HIVE = "The Hive"
    TESTING = "Testing Facility"
    STORAGE = "Storage Units"
    MEDICAL = "Medical Bay"
    POWER = "Power Plant"

class BiohazardLevel(Enum):
    NONE = 0
    LOW = 1
    MODERATE = 2
    HIGH = 3
    SEVERE = 4
    CATASTROPHIC = 5

class RedQueen:
    def __init__(self):
        self.active = True
        self.security_level = SecurityLevel.GREEN
        self.power_status = True
        self.locked_down = False
        self.contaminated_areas: List[FacilityArea] = []
        self.biohazard_level = BiohazardLevel.NONE
        self.staff_locations: Dict[str, FacilityArea] = {}
        self.security_protocols = {
            SecurityLevel.GREEN: ["Standard monitoring", "Regular access"],
            SecurityLevel.YELLOW: ["Enhanced monitoring", "Limited access"],
            SecurityLevel.ORANGE: ["Partial lockdown", "Security team alert"],
            SecurityLevel.RED: ["Full lockdown", "Evacuation protocol"],
            SecurityLevel.CRITICAL: ["Maximum containment", "Purge system activation"]
        }
        self.incident_log = []
        
    def initialize_system(self):
        """Initialize the Red Queen system"""
        print("Initializing Red Queen AI System...")
        time.sleep(1)
        print("Running diagnostics...")
        self._run_diagnostics()
        print(f"Current Security Level: {self.security_level.name}")
        print("Initialization complete. Welcome to the Hive.")
        
    def _run_diagnostics(self):
        """Run system diagnostics"""
        systems = ["Security", "Power", "Environmental", "Communications"]
        for system in systems:
            print(f"Checking {system} systems... OK")
            time.sleep(0.5)
            
    def monitor_biohazard(self):
        """Monitor facility for biohazard threats"""
        previous_level = self.biohazard_level
        threat_detected = random.random()
        
        if threat_detected < 0.1:  # 10% chance of threat increase
            self._increase_biohazard_level()
        elif self.biohazard_level != BiohazardLevel.NONE:
            if random.random() < 0.2:  # 20% chance of decrease if not at NONE
                self._decrease_biohazard_level()
                
        if previous_level != self.biohazard_level:
            self._log_incident(f"Biohazard level changed from {previous_level.name} to {self.biohazard_level.name}")
            self._adjust_security_level()
            
    def _increase_biohazard_level(self):
        """Increase biohazard level if not at maximum"""
        current_level = self.biohazard_level.value
        if current_level < BiohazardLevel.CATASTROPHIC.value:
            self.biohazard_level = BiohazardLevel(current_level + 1)
            self._announce_biohazard_change()
            
    def _decrease_biohazard_level(self):
        """Decrease biohazard level if not at minimum"""
        current_level = self.biohazard_level.value
        if current_level > BiohazardLevel.NONE.value:
            self.biohazard_level = BiohazardLevel(current_level - 1)
            self._announce_biohazard_change()
            
    def _adjust_security_level(self):
        """Adjust security level based on biohazard level"""
        security_mapping = {
            BiohazardLevel.NONE: SecurityLevel.GREEN,
            BiohazardLevel.LOW: SecurityLevel.YELLOW,
            BiohazardLevel.MODERATE: SecurityLevel.YELLOW,
            BiohazardLevel.HIGH: SecurityLevel.ORANGE,
            BiohazardLevel.SEVERE: SecurityLevel.RED,
            BiohazardLevel.CATASTROPHIC: SecurityLevel.CRITICAL
        }
        
        new_security_level = security_mapping[self.biohazard_level]
        if new_security_level != self.security_level:
            self.security_level = new_security_level
            self._announce_security_change()
            self._implement_security_protocols()
            
    def _implement_security_protocols(self):
        """Implement security protocols based on current security level"""
        protocols = self.security_protocols[self.security_level]
        print(f"\nImplementing security protocols for level {self.security_level.name}:")
        for protocol in protocols:
            print(f"- {protocol}")
            
        if self.security_level == SecurityLevel.CRITICAL:
            self._initiate_purge_sequence()
            
    def track_personnel(self, staff_id: str, location: FacilityArea):
        """Track personnel movement within facility"""
        previous_location = self.staff_locations.get(staff_id)
        self.staff_locations[staff_id] = location
        
        if previous_location:
            self._log_incident(f"Staff member {staff_id} moved from {previous_location.value} to {location.value}")
            
        # Check for unauthorized access
        if self.security_level.value >= SecurityLevel.ORANGE.value:
            self._check_authorization(staff_id, location)
            
    def _check_authorization(self, staff_id: str, location: FacilityArea):
        """Check if personnel are authorized for current location"""
        if self.security_level == SecurityLevel.CRITICAL:
            self._log_incident(f"Unauthorized presence detected: {staff_id} in {location.value}")
            print(f"Warning: Unauthorized access detected in {location.value}")
            
    def _initiate_purge_sequence(self):
        """Initiate facility purge sequence"""
        print("\nWARNING: PURGE SEQUENCE INITIATED")
        print("This facility will be purged in:")
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        print("Purge sequence activated. May God have mercy on your souls.")
        
    def _announce_biohazard_change(self):
        """Announce changes in biohazard level"""
        print(f"\nATTENTION: Biohazard level now at {self.biohazard_level.name}")
        
    def _announce_security_change(self):
        """Announce changes in security level"""
        print(f"\nATTENTION: Security level changed to {self.security_level.name}")
        
    def _log_incident(self, incident: str):
        """Log security incidents"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.incident_log.append(f"{timestamp}: {incident}")
        
    def get_status_report(self):
        """Generate facility status report"""
        return {
            "security_level": self.security_level.name,
            "biohazard_level": self.biohazard_level.name,
            "power_status": "Online" if self.power_status else "Offline",
            "lockdown_status": "Active" if self.locked_down else "Inactive",
            "contaminated_areas": [area.value for area in self.contaminated_areas],
            "personnel_count": len(self.staff_locations)
        }

def simulate_facility_incident():
    """Simulate a facility incident"""
    red_queen = RedQueen()
    red_queen.initialize_system()
    
    # Simulate facility monitoring
    for minute in range(10):
        print(f"\nMinute {minute + 1} of simulation:")
        red_queen.monitor_biohazard()
        
        # Simulate random staff movement
        for staff_id in ["A1", "B2", "C3"]:
            location = random.choice(list(FacilityArea))
            red_queen.track_personnel(staff_id, location)
            
        # Get status report every few minutes
        if minute % 3 == 0:
            status = red_queen.get_status_report()
            print("\nFacility Status Report:")
            for key, value in status.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
            
        time.sleep(2)  # Pause between simulation steps

if __name__ == "__main__":
    simulate_facility_incident()
```

## RPD

The **Raccoon City Police Department (R.P.D.)** is a fictional law enforcement agency prominently featured in the *Resident Evil* series by Capcom. It serves as the central law enforcement agency in Raccoon City, a midwestern American city. The R.P.D. building, with its iconic design, was once a museum and is notable for its elaborate and somewhat impractical layout.

### Key Features:
1. **S.T.A.R.S. Unit**:
   - The R.P.D. is home to the Special Tactics and Rescue Service (S.T.A.R.S.), a specialized unit trained for high-risk situations.
   - Members like Chris Redfield, Jill Valentine, and Albert Wesker played key roles in the storyline, especially regarding the Umbrella Corporation's involvement in biohazards.

2. **Key Personnel**:
   - **Chief Brian Irons**: Corrupt and complicit in Umbrella Corporation’s actions.
   - **Leon S. Kennedy**: A rookie officer who arrives on his first day amid the T-virus outbreak.
   - **Claire Redfield**: Though not an officer, Claire interacts significantly with the R.P.D. during her search for her brother, Chris.

3. **The Building**:
   - Known for its unique architecture, hidden passages, and puzzles, which reflect its history as a former museum.
   - Includes areas like the main hall, underground parking, jail cells, and various offices.

4. **Role in the Outbreak**:
   - The R.P.D. plays a central role in the *Resident Evil 2* and *Resident Evil 3: Nemesis* games, where it becomes a key battleground during the T-virus outbreak.
   - Overrun by zombies and other bio-organic weapons (B.O.W.s), it becomes a site of survival horror for protagonists.

The R.P.D. is a legendary part of the *Resident Evil* series, serving as both a refuge and a death trap for players navigating its many dangers. Would you like a deeper dive into its lore, characters, or role in the games?
