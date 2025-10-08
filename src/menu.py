def flatten_menu(node):
    """
    Return a flat list of item names from a nested menu.
    Node has "type": "category" or "item".
    """
    # If node is not a dictionary or missing type, return empty
    if not isinstance(node, dict) or "type" not in node:
        return []

    # If node is an item, return its name (if exists)
    if node["type"] == "item":
        return [node["name"]] if "name" in node else []

    # If node is a category, flatten all its children recursively
    if node["type"] == "category":
        items = []
        for child in node.get("children", []):
            items.extend(flatten_menu(child))
        return items

    # Unknown node type → ignore
    return []
