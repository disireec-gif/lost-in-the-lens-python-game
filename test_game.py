from cathersgamemypy import (
    can_move,
    get_next_location,
    has_all_required_gear,
    get_missing_gear,
    REQUIRED_GEAR,
)


def test_valid_move():
    assert can_move("Trailhead", "north") is True


def test_invalid_move():
    assert can_move("Trailhead", "south") is False


def test_next_location():
    assert get_next_location("Trailhead", "north") == "Fern Hollow"


def test_complete_inventory():
    assert has_all_required_gear(REQUIRED_GEAR) is True


def test_incomplete_inventory():
    inventory = {"camera body", "tripod"}
    assert has_all_required_gear(inventory) is False


def test_missing_gear():
    inventory = {"camera body", "tripod"}
    missing = get_missing_gear(inventory)

    assert "wide-angle lens" in missing
    assert "telephoto lens" in missing
