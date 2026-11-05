"""Lost in the Lens - a text-based wilderness photography adventure."""


LOCATIONS = {
    "Trailhead": {
        "description": "A rain-soaked trail marker points deeper into Cascade Peak National Park.",
        "exits": {"north": "Fern Hollow", "east": "River Crossing"},
        "item": None,
    },
    "Fern Hollow": {
        "description": "Ferns crowd a quiet hollow. Something metallic glints beneath a log.",
        "exits": {"south": "Trailhead", "east": "Cedar Grove"},
        "item": "tripod",
    },
    "River Crossing": {
        "description": "A slick footbridge spans a rushing, glacial river.",
        "exits": {"west": "Trailhead", "north": "Cedar Grove", "east": "Granite Pass"},
        "item": "camera body",
    },
    "Cedar Grove": {
        "description": "Towering cedars shelter a small clearing from the storm.",
        "exits": {"west": "Fern Hollow", "south": "River Crossing", "north": "Wildflower Meadow"},
        "item": "wide-angle lens",
    },
    "Granite Pass": {
        "description": "Wind whistles through a narrow pass between granite walls.",
        "exits": {"west": "River Crossing", "north": "Wildflower Meadow", "east": "Eagle Ridge"},
        "item": "telephoto lens",
    },
    "Wildflower Meadow": {
        "description": "Storm clouds part over a meadow bright with alpine flowers.",
        "exits": {"south": "Cedar Grove", "east": "Eagle Ridge"},
        "item": "memory card",
    },
    "Eagle Ridge": {
        "description": "The ridge gives you a dramatic view of the summit above.",
        "exits": {"west": "Granite Pass", "east": "Summit Overlook"},
        "item": "weather cover",
    },
    "Summit Overlook": {
        "description": "Rogue Ranger Rex waits beside the overlook, arms folded.",
        "exits": {"west": "Eagle Ridge"},
        "item": None,
    },
}

REQUIRED_GEAR = {
    "camera body",
    "wide-angle lens",
    "telephoto lens",
    "tripod",
    "memory card",
    "weather cover",
}

def can_move(location, direction):
    """Return True when the player can move in the chosen direction."""
    return direction in LOCATIONS[location]["exits"]


def get_next_location(location, direction):
    """Return the destination for a valid movement direction."""
    return LOCATIONS[location]["exits"].get(direction)


def has_all_required_gear(inventory):
    """Return True when all required photography gear is collected."""
    return set(inventory) == REQUIRED_GEAR


def get_missing_gear(inventory):
    """Return the required gear that has not been collected."""
    return REQUIRED_GEAR - set(inventory)



def  show_location(location):
    """Print the current location, available exits, and any gear present."""
    data = LOCATIONS[location]
    print(f"\n== {location} ==")
    print(data["description"])
    print("Exits:", ", ".join(data["exits"]))
    if data["item"]:
        print(f"You spot: {data['item']}")


def show_help():
    print("\nCommands:")
    print("  go [north|south|east|west]  Move to a connected zone")
    print("  get [item]                  Pick up gear in this zone")
    print("  look                        Describe your current zone")
    print("  inventory                   Show collected gear")
    print("  help                        Show these commands")
    print("  quit                        Leave the game")


def play():
    location = "Trailhead"
    inventory = set()

    print("=" * 58)
    print("LOST IN THE LENS: A Wilderness Photography Adventure")
    print("=" * 58)
    print("A storm scattered your six essential photography items across")
    print("Cascade Peak National Park. Recover every item, then reach")
    print("Summit Overlook before Rogue Ranger Rex sends you home.")
    print("Type 'help' to see the commands.")

    while True:
        show_location(location)
        command = input("\nWhat will you do? ").strip().lower()
        if not command:
            continue

        verb, *words = command.split()
        target = " ".join(words)

        if verb in {"quit", "exit"}:
            print("You pack up and head safely back down the trail.")
            return
        if verb == "help":
            show_help()
            continue
        if verb in {"look", "l"}:
            continue
        if verb in {"inventory", "i"}:
            print("\nYour camera bag contains:")
            if inventory:
                for item in sorted(inventory):
                    print(f"- {item}")
            else:
                print("- Nothing yet")
            print(f"{len(inventory)}/{len(REQUIRED_GEAR)} essential items collected.")
            continue
        if verb in {"get", "take"}:
            item = LOCATIONS[location]["item"]
            if not item:
                print("There is no photography gear here to collect.")
            elif target != item:
                print(f"You can collect '{item}'. Try: get {item}")
            else:
                inventory.add(item)
                LOCATIONS[location]["item"] = None
                print(f"You carefully pack the {item}.")
            continue
        if verb in {"go", "move"}:
            if target not in LOCATIONS[location]["exits"]:
                print("You cannot go that way from here.")
                continue
            location = LOCATIONS[location]["exits"][target]
            if location == "Summit Overlook":
                if inventory == REQUIRED_GEAR:
                    print("\nRex checks your complete kit, then steps aside.")
                    print("Golden light floods the valley. You capture the career-defining shot!")
                    print("You win!")
                else:
                    missing = ", ".join(sorted(REQUIRED_GEAR - inventory))
                    print("\nRex sees your incomplete camera bag and confiscates your gear.")
                    print(f"Missing: {missing}")
                    print("Game over.")
                return
            continue

        print("I don't understand that command. Type 'help' for assistance.")


if __name__ == "__main__":
    play()

}


def show_location(location):
    """Print the current location, available exits, and any gear present."""
    data = LOCATIONS[location]
    print(f"\n== {location} ==")
    print(data["description"])
    print("Exits:", ", ".join(data["exits"]))
    if data["item"]:
        print(f"You spot: {data['item']}")


def show_help():
    print("\nCommands:")
    print("  go [north|south|east|west]  Move to a connected zone")
    print("  get [item]                  Pick up gear in this zone")
    print("  look                        Describe your current zone")
    print("  inventory                   Show collected gear")
    print("  help                        Show these commands")
    print("  quit                        Leave the game")


def play():
    location = "Trailhead"
    inventory = set()

    print("=" * 58)
    print("LOST IN THE LENS: A Wilderness Photography Adventure")
    print("=" * 58)
    print("A storm scattered your six essential photography items across")
    print("Cascade Peak National Park. Recover every item, then reach")
    print("Summit Overlook before Rogue Ranger Rex sends you home.")
    print("Type 'help' to see the commands.")

    while True:
        show_location(location)
        command = input("\nWhat will you do? ").strip().lower()
        if not command:
            continue

        verb, *words = command.split()
        target = " ".join(words)

        if verb in {"quit", "exit"}:
            print("You pack up and head safely back down the trail.")
            return
        if verb == "help":
            show_help()
            continue
        if verb in {"look", "l"}:
            continue
        if verb in {"inventory", "i"}:
            print("\nYour camera bag contains:")
            if inventory:
                for item in sorted(inventory):
                    print(f"- {item}")
            else:
                print("- Nothing yet")
            print(f"{len(inventory)}/{len(REQUIRED_GEAR)} essential items collected.")
            continue
        if verb in {"get", "take"}:
            item = LOCATIONS[location]["item"]
            if not item:
                print("There is no photography gear here to collect.")
            elif target != item:
                print(f"You can collect '{item}'. Try: get {item}")
            else:
                inventory.add(item)
                LOCATIONS[location]["item"] = None
                print(f"You carefully pack the {item}.")
            continue
        if verb in {"go", "move"}:
            if target not in LOCATIONS[location]["exits"]:
                print("You cannot go that way from here.")
                continue
            location = LOCATIONS[location]["exits"][target]
            if location == "Summit Overlook":
                if inventory == REQUIRED_GEAR:
                    print("\nRex checks your complete kit, then steps aside.")
                    print("Golden light floods the valley. You capture the career-defining shot!")
                    print("You win!")
                else:
                    missing = ", ".join(sorted(REQUIRED_GEAR - inventory))
                    print("\nRex sees your incomplete camera bag and confiscates your gear.")
                    print(f"Missing: {missing}")
                    print("Game over.")
                return
            continue

        print("I don't understand that command. Type 'help' for assistance.")


if __name__ == "__main__":
    play()
