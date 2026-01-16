# Crops database containing the base temperature (Tbase), upper temperature
# (Tupper), and phenology stage thresholds based on cumulative Growing
# Degree Days (GDD).
#
# The phenological stages follow the FAO56 framework:
#   - initial
#   - development
#   - mid-season
#   - harvest (end of late season)
#
# All temperature thresholds (Tbase, Tupper) and cumulative GDD values for
# each growth stage are derived from:
#
# Paredes, P., López-Urrea, R., Martínez-Romero, Á., Petry, M., Cameira, M.R.,
# Montoya, F., Salman, M., & Pereira, L.S. (2025).
# "Estimating the lengths of crop growth stages to define the crop coefficient
# curves using growing degree days (GDD): Application of the revised FAO56
# guidelines." Agricultural Water Management, 319, 109758.
#
# Source tables:
#   - Tbase and Tupper: Tables 1–2
#   - Cumulative GDD for phenological stages: Table 5
#
# These values are applicable under non-limiting water and nutrient conditions
# and are intended for temperature-based phenology estimation consistent with
# FAO56rev guidelines.

crops = {

    # ROOTS, TUBERS, BULBS

    "carrot_common": {
        "t_base": 6,
        "t_upper": 30,
        "stages": {
            "initial": 320,
            "development": 785,      # 320 + 465
            "mid_season": 1285,      # 320 + 465 + 500
            "harvest": 1575,         # total
        },
    },

    "garlic_short": {
        "t_base": 4,
        "t_upper": 30,
        "stages": {
            "initial": 150,
            "development": 490,
            "mid_season": 825,
            "harvest": 1140,
        },
    },

    "garlic_long": {
        "t_base": 4,
        "t_upper": 30,
        "stages": {
            "initial": 580,
            "development": 1195,
            "mid_season": 1510,
            "harvest": 1750,
        },
    },

    "onion_common": {
        "t_base": 4.5,
        "t_upper": 35,
        "stages": {
            "initial": 460,
            "development": 930,
            "mid_season": 1810,
            "harvest": 2290,
        },
    },

    "potato_short": {
        "t_base": 2,
        "t_upper": 30,
        "stages": {
            "initial": 260,
            "development": 750,
            "mid_season": 1275,
            "harvest": 1600,
        },
    },

    "potato_long": {
        "t_base": 2,
        "t_upper": 30,
        "stages": {
            "initial": 405,
            "development": 935,
            "mid_season": 1425,
            "harvest": 2260,
        },
    },


    # LEAVES AND FLOWERS

    "broccoli_short": {
        "t_base": 4.5,
        "t_upper": 30,
        "stages": {
            "initial": 195,
            "development": 445,
            "mid_season": 655,
            "harvest": 755,
        },
    },

    "broccoli_long": {
        "t_base": 4.5,
        "t_upper": 30,
        "stages": {
            "initial": 295,
            "development": 645,
            "mid_season": 1170,
            "harvest": 1280,
        },
    },

    "lettuce_short": {
        "t_base": 4,
        "t_upper": 28,
        "stages": {
            "initial": 365,
            "development": 750,
            "mid_season": 965,
            "harvest": 985,
        },
    },

    "lettuce_long": {
        "t_base": 4,
        "t_upper": 28,
        "stages": {
            "initial": 360,
            "development": 815,
            "mid_season": 1270,
            "harvest": 1290,
        },
    },

    # FRUIT VEGETABLES

    "bell_pepper_common": {
        "t_base": 10,
        "t_upper": 35,
        "stages": {
            "initial": 445,
            "development": 1625,
            "mid_season": 2370,
            "harvest": 2415,
        },
    },

    "melon_short": {
        "t_base": 10,
        "t_upper": 38,
        "stages": {
            "initial": 185,
            "development": 705,
            "mid_season": 1020,
            "harvest": 1175,
        },
    },

    "melon_long": {
        "t_base": 10,
        "t_upper": 38,
        "stages": {
            "initial": 140,
            "development": 685,
            "mid_season": 1145,
            "harvest": 1600,
        },
    },

    "tomato_industry": {
        "t_base": 7,
        "t_upper": 28,
        "stages": {
            "initial": 280,
            "development": 800,
            "mid_season": 1680,
            "harvest": 1900,
        },
    },

    "tomato_market": {
        "t_base": 7,
        "t_upper": 28,
        "stages": {
            "initial": 325,
            "development": 985,
            "mid_season": 1865,
            "harvest": 2065,
        },
    },


    # FIELD CROPS – CEREALS


    "barley_short": {
        "t_base": 0,
        "t_upper": 30,
        "stages": {
            "initial": 290,
            "development": 745,
            "mid_season": 1090,
            "harvest": 1450,
        },
    },

    "barley_long": {
        "t_base": 0,
        "t_upper": 30,
        "stages": {
            "initial": 300,
            "development": 975,
            "mid_season": 1665,
            "harvest": 2330,
        },
    },

    "maize_grain_short": {
        "t_base": 10,
        "t_upper": 32,
        "stages": {
            "initial": 200,
            "development": 580,
            "mid_season": 1080,
            "harvest": 1540,
        },
    },

    "maize_grain_long": {
        "t_base": 10,
        "t_upper": 32,
        "stages": {
            "initial": 295,
            "development": 715,
            "mid_season": 1490,
            "harvest": 1955,
        },
    },
}