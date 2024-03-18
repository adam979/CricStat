
class ColorScheme:
    # Define the color schemes for each team
    COLOR_SCHEMES = {
        "CSK": {
            "Primary": ["#ffcb05", "#FFCE32", "#f36f21"],
            "Secondary": ["#0066b3", "#1D63FF", "#002349", "#0091ff"],
        },
        "DC": {
            "Primary": ["#17479e", "#113577"],
            "Secondary": ["#d71921", "#fd1d26", "#fb042d"],
        },
        "GG": {"Primary": ["#1d314d", "#1993ff"], "Secondary": ["#dec16d", "#ffe67d"]},
        "KKR": {
            "Primary": ["#53367d", "#704fa1", "#5d3696"],
            "Secondary": ["#f2bf26", "#e3ad3e"],
        },
        "LSG": {"Primary": ["#0257e0", "#1c2c78"], "Secondary": ["#f08800", "#e2250f"]},
        "MI": {
            "Primary": ["#1140be", "#0e3889", "#345ecc", "#0155c8", "#083f88"],
            "Secondary": ["#c19a3c", "#d8ba63", "#dfc667"],
        },
        "PBKS": {
            "Primary": ["#dd1f2d", "#ed1c24"],
            "Secondary": ["#d0aa82", "#f3d6a9"],
        },
        "RR": {
            "Primary": ["#ff4690", "#e50693", "#a00048", "#fe0085"],
            "Secondary": ["#254aa5", "#cba92b", "#0c1679"],
        },
        "RCB": {
            "Primary": ["#fc0e17", "#e00c0b"],
            "Secondary": ["#000000", "#deb04e", "#d4a23d", "#ccba70"],
        },
        "SRH": {"Primary": ["#fe4f34", "#fc642c", "#e27a07"], "Secondary": ["#000000"]},
        # Add color schemes for other teams here...
    }

    @staticmethod
    def get_colors(team):
        """Retrieve the primary and secondary colors for a given team."""
        primary_colors = ColorScheme.COLOR_SCHEMES.get(team, {}).get("Primary", [])
        secondary_colors = ColorScheme.COLOR_SCHEMES.get(team, {}).get("Secondary", [])
        return primary_colors, secondary_colors
