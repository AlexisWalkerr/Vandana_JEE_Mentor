"""
====================================================================================
    Part of     : Vandana_JEE_Mentor — Tools Module
    Purpose     : Provide structured JEE syllabus for Physics, Chemistry & Maths

    Team Name   : Anagha_Vandana
------------------------------------------------------------------------------------
    Description : Used by planner agent to build correct topic-oriented study plans.
====================================================================================
"""


def get_jee_syllabus(subject: str) -> str:
    """
    Returns a brief JEE syllabus/topic outline for the given subject.
    subject: 'Physics', 'Chemistry', or 'Maths' / 'Mathematics'.
    """
    s = subject.strip().lower()

    if s == "physics":
        return (
            "JEE Physics Syllabus (high-level):\n"
            "- Units and Measurements\n"
            "- Kinematics\n"
            "- Laws of Motion\n"
            "- Work, Energy and Power\n"
            "- Rotational Motion\n"
            "- Gravitation\n"
            "- Oscillations and Waves\n"
            "- Thermodynamics and Kinetic Theory\n"
            "- Electrostatics, Current Electricity\n"
            "- Magnetism and Electromagnetic Induction\n"
            "- Optics\n"
            "- Modern Physics\n"
        )

    if s == "chemistry":
        return (
            "JEE Chemistry Syllabus (high-level):\n"
            "- Basic Concepts of Chemistry\n"
            "- Atomic Structure\n"
            "- Chemical Bonding and Molecular Structure\n"
            "- States of Matter, Thermodynamics, Equilibrium\n"
            "- Redox Reactions, Electrochemistry, Chemical Kinetics\n"
            "- Surface Chemistry\n"
            "- Classification of Elements and Periodicity\n"
            "- Inorganic Chemistry (s, p, d, f block elements)\n"
            "- Coordination Compounds\n"
            "- Organic Chemistry: Basics, Hydrocarbons, Halides,\n"
            "  Alcohols, Aldehydes, Ketones, Carboxylic Acids,\n"
            "  Amines, Biomolecules, Polymers, Everyday Chemistry\n"
        )

    if s in ("maths", "mathematics"):
        return (
            "JEE Mathematics Syllabus (high-level):\n"
            "- Sets, Relations and Functions\n"
            "- Complex Numbers and Quadratic Equations\n"
            "- Matrices and Determinants\n"
            "- Permutations and Combinations\n"
            "- Mathematical Induction and Binomial Theorem\n"
            "- Sequences and Series\n"
            "- Limits, Continuity and Differentiability\n"
            "- Integral Calculus and its applications\n"
            "- Differential Equations\n"
            "- Coordinate Geometry (2D/3D)\n"
            "- Vector Algebra\n"
            "- Statistics and Probability\n"
            "- Trigonometry\n"
        )

    return (
        "Unknown subject. Please use one of: Physics, Chemistry, Maths."
    )
