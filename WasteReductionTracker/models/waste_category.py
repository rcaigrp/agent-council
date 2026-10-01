class WasteCategory:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"WasteCategory(name='{self.name}', description='{self.description}')"

# Define common waste categories
PLASTIC = WasteCategory("plastic", "Plastic waste items")
PAPER = WasteCategory("paper", "Paper and cardboard waste")
ORGANIC = WasteCategory("organic", "Food scraps and organic waste")
METAL = WasteCategory("metal", "Metal waste items")
OTHER = WasteCategory("other", "Other waste categories")

# All categories list
ALL_CATEGORIES = [PLASTIC, PAPER, ORGANIC, METAL, OTHER]