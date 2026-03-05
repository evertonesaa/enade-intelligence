def classify_question(text: str) -> str:

    text = text.lower()

    thermodynamics = [
        "rankine", "brayton", "enthalpy", "entropy",
        "thermodynamic", "turbine", "compressor",
        "boiler", "caldeira", "ciclo", "energia"
    ]

    transport = [
        "reynolds", "drag", "fluid", "flow",
        "viscosity", "pump", "pressure",
        "escoamento", "fluido", "vazão"
    ]

    heat_transfer = [
        "heat transfer", "conduction", "convection",
        "radiation", "heat exchanger",
        "transferência de calor"
    ]

    reaction = [
        "reactor", "reaction", "kinetics",
        "equilibrium", "catalyst", "reação"
    ]

    separations = [
        "distillation", "column", "adsorption",
        "membrane", "separation", "destilação"
    ]

    materials = [
        "hardness", "machining", "lathe",
        "tool wear", "alloy", "usinagem"
    ]

    if any(word in text for word in thermodynamics):
        return "Thermodynamics"

    if any(word in text for word in transport):
        return "Transport Phenomena"

    if any(word in text for word in heat_transfer):
        return "Heat Transfer"

    if any(word in text for word in reaction):
        return "Reaction Engineering"

    if any(word in text for word in separations):
        return "Separation Processes"

    if any(word in text for word in materials):
        return "Materials Engineering"

    return "Unknown"