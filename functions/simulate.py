import random

# You can add your own or let the user provide a custom list
AI_NAMES = [
    "Rico Blaze", "Sasha Torque", "Max Velocity", "Luna Drift", "Zane Nitro",
    "Carmen Veloce", "Ace Thunder", "Niko Shift", "Ryder Apex", "Jade Burn",
    "Taro Flash", "Mira Zoom", "Dash Steel", "Lexi Storm", "Finn Traction"
]

FORZA_POINTS = [25, 20, 18, 15, 12, 10, 8, 6, 4, 2, 1]  # Top 11 get points

def simulate_ai_results(user_time, user_position, total_racers=16):
    results = []

    # Indexes for placement
    user_index = user_position - 1  # 0-based
    racer_count = total_racers - 1

    # Generate times for AI based on user's position and time
    for pos in range(total_racers):
        if pos == user_index:
            continue  # Skip user's position, reserved for user

        time_offset = 0

        if pos < user_index:
            # AI ahead of user — slightly faster
            time_offset = -random.uniform(0.1, 5.0)
        elif pos > user_index:
            # AI behind user — slightly slower
            time_offset = random.uniform(0.1, 5.0)
        else:
            # Adjacent to user (shouldn't hit this case but safe fallback)
            time_offset = random.uniform(-0.2, 0.2)

        ai_time = round(user_time + time_offset, 3)
        results.append((pos, ai_time))

    # Sort by time to assign final positions
    results.sort(key=lambda x: x[1])
    final_results = []
    used_names = set()

    for idx, (original_pos, ai_time) in enumerate(results):
        name = random.choice([n for n in AI_NAMES if n not in used_names])
        used_names.add(name)

        finish_position = idx + 1 if idx < user_index else idx + 2  # Skip user's slot
        points = FORZA_POINTS[finish_position - 1] if finish_position <= len(FORZA_POINTS) else 0

        final_results.append({
            'name': name,
            'finish_time': ai_time,
            'position': finish_position,
            'points': points
        })

    return final_results
