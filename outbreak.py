class Virus:
    def __init__(self, name, infection_rate, mutation_chance, lethality):
        self.name = name
        self.infection_rate = infection_rate  # 0-100
        self.mutation_chance = mutation_chance  # 0-100
        self.lethality = lethality  # 0-100
        self.mutations = []
        
class Mutation:
    def __init__(self, name, effects):
        self.name = name
        self.effects = effects

class Host:
    def __init__(self, name, immunity=50):
        self.name = name
        self.immunity = immunity  # 0-100
        self.infected = False
        self.mutations = []
        self.current_virus = None
        self.health = 100

def create_resident_evil_viruses():
    # Create base viruses
    t_virus = Virus("T-Virus", 85, 70, 90)
    t_virus.mutations = [
        Mutation("Zombie", ["Decreased Intelligence", "Increased Strength"]),
        Mutation("Crimson Head", ["High Speed", "Aggression", "Regeneration"]),
        Mutation("Tyrant", ["Massive Size", "Super Strength", "Regeneration"])
    ]
    
    g_virus = Virus("G-Virus", 95, 100, 95)
    g_virus.mutations = [
        Mutation("G1", ["Enhanced Strength", "Initial Transformation"]),
        Mutation("G2", ["Armored Shell", "Multiple Arms"]),
        Mutation("G3", ["Multiple Eyes", "Enhanced Regeneration"]),
        Mutation("G4", ["Complete Mutation", "Loss of Humanity"])
    ]
    
    return [t_virus, g_virus]

def infect_host(host, virus):
    """Attempt to infect a host with a virus"""
    import random
    
    # Calculate infection chance
    infection_chance = virus.infection_rate - host.immunity
    
    if random.randint(0, 100) < infection_chance:
        host.infected = True
        host.current_virus = virus
        print(f"{host.name} has been infected with {virus.name}")
        return True
    else:
        print(f"{host.name} resisted infection from {virus.name}")
        return False

def mutate_host(host):
    """Attempt to mutate an infected host"""
    import random
    
    if not host.infected or not host.current_virus:
        return False
        
    if random.randint(0, 100) < host.current_virus.mutation_chance:
        # Select random mutation from virus mutations list
        new_mutation = random.choice(host.current_virus.mutations)
        host.mutations.append(new_mutation)
        print(f"{host.name} has mutated: {new_mutation.name}")
        print(f"New effects: {', '.join(new_mutation.effects)}")
        return True
    return False

def simulate_outbreak():
    """Simulate a virus outbreak"""
    viruses = create_resident_evil_viruses()
    hosts = [
        Host("Subject A", immunity=30),
        Host("Subject B", immunity=60),
        Host("Subject C", immunity=45)
    ]
    
    # Simulate infection spread
    for virus in viruses:
        print(f"\nTesting {virus.name}:")
        for host in hosts:
            if not host.infected:
                infect_host(host, virus)
                if host.infected:
                    # Try mutation
                    for _ in range(3):  # Give 3 chances to mutate
                        mutate_host(host)

# Run simulation
if __name__ == "__main__":
    print("=== Resident Evil Virus Simulation ===")
    simulate_outbreak()
