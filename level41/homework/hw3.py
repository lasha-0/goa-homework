def find_needle(haystack):
    if "needle" in haystack:
        return f"found the needle at position {haystack.index('needle')}"
    else:
        return "needle not found"