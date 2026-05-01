SEASONS = {"Season1": "Season 1", "Season2": "Season 2"}
PLATFORM = {
    0: "unknown",
    1: "pc",
    2: "ps4",
    3: "xboxone",
    4: "ps5",
    5: "xboxseries",
    6: "common",
    7: "steam",
}
STATS_PLATFORM = {
    1: "pc",
    3: "xboxone",
    2: "ps4",
    5: "xboxseries",
    4: "ps5",
    6: "common",
    7: "steam",
}
PLATFORM_REVERSE = {
    "unknown": 0,
    "pc": 1,
    "ps4": 2,
    "xboxone": 3,
    "ps5": 4,
    "xboxseries": 5,
    "common": 6,
    "steam": 7,
}
PLATFORM_FESL = {
    0: "pc",
    1: "pc",
    2: "ps4",
    3: "xboxone",
    4: "ps4",
    5: "xboxone",
    6: "pc",
    7: "pc",
}
STATS_PLATFORM_REVERSE = {
    "pc": 1,
    "xboxone": 3,
    "ps4": 2,
    "xboxseries": 5,
    "ps5": 4,
    "xbox": 5,
    "psn": 4,
    "steam": 7,
}
PLATFORM_EA = {"cem_ea_id": "ea", "xbox": "xboxone", "epic": "epic", "steam": "steam"}
PLATFORM_EA_REVERSE = {
    "ea": "cem_ea_id",
    "xboxone": "xbox",
    "epic": "epic",
    "steam": "steam",
}
REGIONS = {
    "aws-hkg": "Asia",
    "aws-icn": "Asia",
    "aws-nrt": "Asia",
    "aws-sin": "Asia",
    "aws-iad": "North America",
    "aws-pdx": "North America",
    "aws-sjc": "North America",
    "aws-brz": "South America",
    "aws-fra": "Europe",
    "aws-lhr": "Europe",
    "aws-syd": "Oceania",
}
REGIONSLIST = {
    "asia": ["aws-hkg", "aws-icn", "aws-nrt", "aws-sin"],
    "nam": ["aws-iad", "aws-pdx", "aws-sjc"],
    "sam": ["aws-brz"],
    "eu": ["aws-fra", "aws-lhr"],
    "oc": ["aws-syd"],
    "all": [
        "aws-iad",
        "aws-pdx",
        "aws-sjc",
        "aws-brz",
        "aws-fra",
        "aws-lhr",
        "aws-hkg",
        "aws-icn",
        "aws-nrt",
        "aws-sin",
        "aws-syd",
    ],
}
SHORT_REGIONS = {
    "aws-hkg": "asia",
    "aws-icn": "asia",
    "aws-nrt": "asia",
    "aws-sin": "asia",
    "aws-iad": "nam",
    "aws-pdx": "nam",
    "aws-sjc": "nam",
    "aws-brz": "sam",
    "aws-fra": "eu",
    "aws-lhr": "eu",
    "aws-syd": "oc",
}
MAPS = {
    "MP_Abbasid": "Siege of Cairo",
    "MP_Aftermath": "Empire State",
    "MP_Badlands": "Blackwell Fields",
    "MP_Battery": "Iberian Offensive",
    "MP_Capstone": "Liberation Peak",
    "MP_Dumbo": "Manhattan Bridge",
    "MP_Eastwood": "Eastwood",
    "MP_FireStorm": "Operation Firestorm",
    "MP_Limestone": "Saints Quarter",
    "MP_Outskirts": "New Sobek City",
    "MP_Tungsten": "Mirak Valley",
    "MP_Portal_Sand": "Portal Sandbox",
    "MP_Contaminated": "Contaminated",
    "MP_Granite": "Fort Lyndon",
    "MP_Granite_MainStreet_Portal": "Downtown",
    "MP_Granite_MilitaryRnD_Portal": "Area 22B",
    "MP_Granite_Marina_Portal": "Marina",
    "MP_Granite_MilitaryStorage_Portal": "Redline Storage",
    "MP_Granite_ClubHouse_Portal": "Club House",
    "MP_Granite_TechCampus_Portal": "Tech Center",
}
TO_GAME_MAPS = {
    "siege of cairo": "MP_Abbasid",
    "empire state": "MP_Aftermath",
    "blackwell fields": "MP_Badlands",
    "iberian offensive": "MP_Battery",
    "liberation peak": "MP_Capstone",
    "manhattan bridge": "MP_Dumbo",
    "eastwood": "MP_Eastwood",
    "operation firestorm": "MP_FireStorm",
    "saints quarter": "MP_Limestone",
    "new sobek city": "MP_Outskirts",
    "mirak valley": "MP_Tungsten",
    "contaminated": "MP_Contaminated",
    "portal sandbox": "MP_Portal_Sand",
    "area 22b": "MP_Granite_MilitaryRnD_Portal",
    "downtown": "MP_Granite_MainStreet_Portal",
    "redline storage": "MP_Granite_MilitaryStorage_Portal",
    "club house": "MP_Granite_ClubHouse_Portal",
    "tech center": "MP_Granite_TechCampus_Portal",
}
MAP_TRANSLATION_IDS = {
    "MP_Abbasid": "ID_MP_LVL_ABBASID_NAME",
    "MP_Aftermath": "ID_MP_LVL_AFTERMATH_NAME",
    "MP_Badlands": "ID_MP_LVL_BADLANDS_NAME",
    "MP_Battery": "ID_MP_LVL_BATTERY_NAME",
    "MP_Capstone": "ID_MP_LVL_CAPSTONE_NAME",
    "MP_Dumbo": "ID_MP_LVL_DUMBO_NAME",
    "MP_Eastwood": "ID_MP_LVL_EASTWOOD_NAME",
    "MP_FireStorm": "ID_MP_LVL_FIRESTORM_NAME",
    "MP_Limestone": "ID_MP_LVL_LIMESTONE_NAME",
    "MP_Outskirts": "ID_MP_LVL_OUTSKIRTS_NAME",
    "MP_Tungsten": "ID_MP_LVL_TUNGSTEN_NAME",
    "MP_Contaminated": "ID_ARRIVAL_MAP_CONTAMINATED",
    "MP_Portal_Sand": "ID_ARRIVAL_MAP_PORTALSANDBOX",
    "MP_Granite": "ID_ARRIVAL_MAP_GRANITE",
    "MP_Granite_MainStreet_Portal": "ID_ARRIVAL_MAP_GRANITE_DOWNTOWN",
    "MP_Granite_MilitaryRnD_Portal": "ID_ARRIVAL_MAP_GRANITE_MILITARY_RND_N",
    "MP_Granite_MilitaryStorage_Portal": "ID_ARRIVAL_MAP_GRANITE_MILITARY_STORAGE_N",
    "MP_Granite_Marina_Portal": "ID_ARRIVAL_MAP_GRANITE_MARINA",
    "MP_Granite_ClubHouse_Portal": "ID_ARRIVAL_MAP_GRANITE_CLUB_HOUSE",
    "MP_Granite_TechCampus_Portal": "ID_ARRIVAL_MAP_GRANITE_TECH_CENTER",
}
MAP_PICTURES = {
    "MP_Abbasid": "https://cdn.gametools.network/maps/bf6/T_UI_Abbasid_Large_OPT-49a3761a.webp",
    "MP_Aftermath": "https://cdn.gametools.network/maps/bf6/T_UI_Aftermath_Large_OPT-bf883df1.webp",
    "MP_Badlands": "https://cdn.gametools.network/maps/bf6/T_UI_Badlands_Large_OPT-6885eb83.webp",
    "MP_Battery": "https://cdn.gametools.network/maps/bf6/T_UI_Battery_Large_OPT-034d4636.webp",
    "MP_Capstone": "https://cdn.gametools.network/maps/bf6/T_UI_Capstone_Large_OPT-2ccae694.webp",
    "MP_Eastwood": "https://cdn.gametools.network/maps/bf6/T_UI_Eastwood_Large_OPT-3bfa6a6f.webp",
    "MP_Dumbo": "https://cdn.gametools.network/maps/bf6/T_UI_Dumbo_Large_OPT-20de031f.webp",
    "MP_FireStorm": "https://cdn.gametools.network/maps/bf6/T_UI_Firestorm_Large_OPT-45d582ad.webp",
    "MP_Limestone": "https://cdn.gametools.network/maps/bf6/T_UI_Limestone_Large_OPT-c9160897.webp",
    "MP_Outskirts": "https://cdn.gametools.network/maps/bf6/T_UI_Outskirts_Large_OPT-bf08f756.webp",
    "MP_Tungsten": "https://cdn.gametools.network/maps/bf6/T_UI_Tungsten_Large_OPT-935da06b.webp",
    "MP_Contaminated": "https://cdn.gametools.network/maps/bf6/T_UI_Contaminated_Large_OPT-da1d04ef.webp",
    "MP_Portal_Sand": "https://cdn.gametools.network/maps/bf6/T_UI_Granite_Portal_07_Thumb_SML-b141ec28.jpg",
    "MP_Granite": "https://cdn.gametools.network/maps/bf6/Fort_Lyndon_BF6_REDSEC.webp",
    "MP_Granite_MainStreet_Portal": "https://cdn.gametools.network/maps/bf6/T_UI_Granite_Portal_01_Thumb_SML-c1924a54.jpg",
    "MP_Granite_Marina_Portal": "https://cdn.gametools.network/maps/bf6/T_UI_Granite_Portal_02_Thumb_SML-bacdb856.jpg",
    "MP_Granite_MilitaryRnD_Portal": "https://cdn.gametools.network/maps/bf6/T_UI_Granite_Portal_03_Thumb_SML-074dbb4f.jpg",
    "MP_Granite_MilitaryStorage_Portal": "https://cdn.gametools.network/maps/bf6/T_UI_Granite_Portal_04_Thumb_SML-e8d5744b.jpg",
    "MP_Granite_ClubHouse_Portal": "https://cdn.gametools.network/maps/bf6/T_UI_Granite_Portal_05_Thumb_SML-74ea7be7.webp",
    "MP_Granite_TechCampus_Portal": "https://cdn.gametools.network/maps/bf6/T_UI_Granite_Portal_06_Thumb_SML-80099ba6.webp",
}
SMALLMODES = {
    "Breakthrough0": "BT",
    "BreakthroughSmall0": "BS",
    "ConquestSmall0": "CQ",
    "ModBuilderCustom0": "CM",
    "Rush0": "RS",
    "Conquest0": "CL",
    "GraniteDuo0": "RD",
    "GraniteSquad0": "RQ",
    "GraniteSolo0": "BRS",
    "GraniteGauntlet0": "RG",
}
MODES = {
    "Breakthrough0": "Breakthrough Large",
    "BreakthroughSmall0": "Breakthrough",
    "ConquestSmall0": "Conquest",
    "ModBuilderCustom0": "Custom",
    "Rush0": "Rush",
    "Conquest0": "Conquest large",
    "GraniteDuo0": "Redsec Duos",
    "GraniteSquad0": "Redsec Quads",
    "GraniteSolo0": "Redsec Solo",
    "GraniteGauntlet0": "Redsec Gauntlet",
}
REDSEC_MODES = {
    "GraniteDuo0": "Duos",
    "GraniteSquad0": "Quads",
    "GraniteSolo0": "Solo",
    "GraniteGauntlet0": "Gauntlet",
}
TO_GAME_MODES = {
    "breakthrough large": "Breakthrough0",
    "breakthrough": "BreakthroughSmall0",
    "conquest": "ConquestSmall0",
    "custom": "ModBuilderCustom0",
    "rush": "Rush0",
    "conquest large": "Conquest0",
    "redsec duos": "GraniteDuo0",
    "redsec quads": "GraniteSquad0",
    "redsec solo": "GraniteSolo0",
    "redsec gauntlet": "GraniteGauntlet0",
}
STAT_MAPS = {
    "lvlmp": {
        "mapName": "All",
        "translationId": "ID_ARRIVAL_MUTATOR_310492599_ENTRY_0",
    },
    "lvlmpabbasid": {
        "mapName": "Siege of Cairo",
        "image": "https://cdn.gametools.network/maps/bf6/T_UI_Abbasid_Large_OPT-49a3761a.webp",
        "translationId": "ID_MP_LVL_ABBASID_NAME",
    },
    "lvlmpaftermath": {
        "mapName": "Empire State",
        "image": "https://cdn.gametools.network/maps/bf6/T_UI_Aftermath_Large_OPT-bf883df1.webp",
        "translationId": "ID_MP_LVL_AFTERMATH_NAME",
    },
    "lvlmpbattery": {
        "mapName": "Iberian Offensive",
        "image": "https://cdn.gametools.network/maps/bf6/T_UI_Battery_Large_OPT-034d4636.webp",
        "translationId": "ID_MP_LVL_BATTERY_NAME",
    },
    "lvlmpcapstone": {
        "mapName": "Liberation Peak",
        "image": "https://cdn.gametools.network/maps/bf6/T_UI_Capstone_Large_OPT-2ccae694.webp",
        "translationId": "ID_MP_LVL_CAPSTONE_NAME",
    },
    "lvlmpdumbo": {
        "mapName": "Manhattan Bridge",
        "image": "https://cdn.gametools.network/maps/bf6/T_UI_Dumbo_Large_OPT-20de031f.webp",
        "translationId": "ID_MP_LVL_DUMBO_NAME",
    },
    "lvlmpfirestorm": {
        "mapName": "Operation Firestorm",
        "image": "https://cdn.gametools.network/maps/bf6/T_UI_Firestorm_Large_OPT-45d582ad.webp",
        "translationId": "ID_MP_LVL_FIRESTORM_NAME",
    },
    "lvlmplimestone": {
        "mapName": "Saints Quarter",
        "image": "https://cdn.gametools.network/maps/bf6/T_UI_Limestone_Large_OPT-c9160897.webp",
        "translationId": "ID_MP_LVL_LIMESTONE_NAME",
    },
    "lvlmpoutskirts": {
        "mapName": "New Sobek City",
        "image": "https://cdn.gametools.network/maps/bf6/T_UI_Outskirts_Large_OPT-bf08f756.webp",
        "translationId": "ID_MP_LVL_OUTSKIRTS_NAME",
    },
    "lvlmptungsten": {
        "mapName": "Mirak Valley",
        "image": "https://cdn.gametools.network/maps/bf6/T_UI_Tungsten_Large_OPT-935da06b.webp",
        "translationId": "ID_MP_LVL_TUNGSTEN_NAME",
    },
    "lvlmpbadlands": {
        "mapName": "Blackwell Fields",
        "image": "https://cdn.gametools.network/maps/bf6/Battlefield_6_Blackwell_Fields.webp",
        "translationId": "ID_MP_LVL_BADLANDS_NAME",
    },
    "lvlftpgranite": {
        "mapName": "REDSEC",
        "image": "https://cdn.gametools.network/maps/bf6/Battlefield_6_Redsec.webp",
        "translationId": "ID_ARRIVAL_REDSEC",
    },
    "lvlmpeastwood": {
        "mapName": "Eastwood",
        "image": "https://cdn.gametools.network/maps/bf6/T_UI_Eastwood_Large_OPT-3bfa6a6f.webp",
        "translationId": "ID_MP_LVL_EASTWOOD_NAME",
    },
    "lvlmpcontaminated": {
        "mapName": "Contaminated",
        "image": "https://cdn.gametools.network/maps/bf6/T_UI_Contaminated_Large_OPT-da1d04ef.webp",
        "translationId": "ID_MP_LVL_CONTAMINATED_NAME",
    },
    "lvlmpsubsurface": {
        "mapName": "Hagental Base",
        "image": "",
        "translationId": "ID_MP_LVL_SUBSURFACE_NAME",
    },
}

STAT_GAMEMODE_SMALL = {
    "gm_esc": {
        "gamemodeName": "Escalation",
        "image": "https://cdn.gametools.network/modes/bf6/escalation.svg",
        "altImage": "",
    },
    "gm_tdm": {
        "gamemodeName": "Team deathmatch",
        "image": "https://cdn.gametools.network/modes/bf6/team_deathmatch.svg",
        "altImage": "",
    },
    "gm_sdm": {
        "gamemodeName": "Squad deathmatch",
        "image": "https://cdn.gametools.network/modes/bf6/squad_deathmatch.svg",
        "altImage": "",
    },
    "gm_dom": {
        "gamemodeName": "Domination",
        "image": "https://cdn.gametools.network/modes/bf6/domination.svg",
        "altImage": "",
    },
    "gm_koth": {
        "gamemodeName": "King of the Hill",
        "image": "https://cdn.gametools.network/modes/bf6/king_of_the_hill.svg",
        "altImage": "",
    },
    "gm_cq": {
        "gamemodeName": "Conquest",
        "image": "https://cdn.gametools.network/modes/bf6/conquest.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/conquest-framed.svg",
    },
    "gm_graniteDuo": {
        "gamemodeName": "Redsec Duo",
        "image": "https://cdn.gametools.network/modes/bf6/battle_royale.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/battle_royale-framed.svg",
    },
    "gm_graniteSolo": {
        "gamemodeName": "Redsec Solo",
        "image": "https://cdn.gametools.network/modes/bf6/battle_royale.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/battle_royale-framed.svg",
    },
    "gm_brsquad": {
        "gamemodeName": "Redsec Squad",
        "image": "https://cdn.gametools.network/modes/bf6/battle_royale.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/battle_royale-framed.svg",
    },
    "gm_rush": {
        "gamemodeName": "Rush",
        "image": "https://cdn.gametools.network/modes/bf6/rush.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/rush-framed.svg",
    },
    "gm_bt": {
        "gamemodeName": "Breakthrough",
        "image": "https://cdn.gametools.network/modes/bf6/breakthrough.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/breakthrough-framed.svg",
    },
    "gm_gntgauntlet": {
        "gamemodeName": "Gauntlet",
        "image": "https://cdn.gametools.network/modes/bf6/gauntlet.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/gauntlet-framed.svg",
    },
    "gm_modbuilder0": {
        "gamemodeName": "Portal",
        "image": "https://cdn.gametools.network/modes/bf6/wrench-hammer.svg",
        "altImage": "",
    },
    "gm_strike": {
        "gamemodeName": "Strikepoint",
        "image": "https://cdn.gametools.network/modes/bf6/strikepoint.svg",
        "altImage": "",
    },
    "gm_official": {"gamemodeName": "Official", "image": "", "altImage": ""},
    "gm_sabotage": {"gamemodeName": "Sabotage", "image": "", "altImage": ""},
}
STAT_GAMEMODE_SMALL_CATEGORY = {
    "gm_all": {"gamemodeName": "All", "image": "", "altImage": ""},
    "gm_mp": {"gamemodeName": "Multiplayer", "image": "", "altImage": ""},
    "gm_modbuilder": {
        "gamemodeName": "Portal",
        "image": "https://cdn.gametools.network/modes/bf6/wrench-hammer.svg",
        "altImage": "",
    },
    "gm_granite": {
        "gamemodeName": "Redsec",
        "image": "https://cdn.gametools.network/modes/bf6/battle_royale.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/battle_royale-framed.svg",
    },
    "gm_granitebr": {
        "gamemodeName": "Battle Royale",
        "image": "https://cdn.gametools.network/modes/bf6/battle_royale.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/battle_royale-framed.svg",
    },
}
STAT_GAMEMODE = {
    "MP_Escalation0": {
        "gamemodeName": "Escalation",
        "image": "https://cdn.gametools.network/modes/bf6/escalation.svg",
        "altImage": "",
    },
    "MP_TeamDM0": {
        "gamemodeName": "Team deathmatch",
        "image": "https://cdn.gametools.network/modes/bf6/team_deathmatch.svg",
        "altImage": "",
    },
    "GraniteGauntlet0": {
        "gamemodeName": "Gauntlet",
        "image": "https://cdn.gametools.network/modes/bf6/gauntlet.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/gauntlet-framed.svg",
    },
    "GraniteSquad0": {
        "gamemodeName": "Redsec Squad",
        "image": "https://cdn.gametools.network/modes/bf6/battle_royale.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/battle_royale-framed.svg",
    },
    "GraniteSolo0": {
        "gamemodeName": "Redsec Solo",
        "image": "https://cdn.gametools.network/modes/bf6/battle_royale.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/battle_royale-framed.svg",
    },
    "MP_KOTH0": {
        "gamemodeName": "King of the Hill",
        "image": "https://cdn.gametools.network/modes/bf6/king_of_the_hill.svg",
        "altImage": "",
    },
    "GraniteDuo0": {
        "gamemodeName": "Redsec Duo",
        "image": "https://cdn.gametools.network/modes/bf6/battle_royale.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/battle_royale-framed.svg",
    },
    "MP_Domination0": {
        "gamemodeName": "Domination",
        "image": "https://cdn.gametools.network/modes/bf6/domination.svg",
        "altImage": "",
    },
    "Conquest0": {
        "gamemodeName": "Conquest",
        "image": "https://cdn.gametools.network/modes/bf6/conquest.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/conquest-framed.svg",
    },
    "MP_SquadDM0": {
        "gamemodeName": "Squad deathmatch",
        "image": "https://cdn.gametools.network/modes/bf6/squad_deathmatch.svg",
        "altImage": "",
    },
    "Breakthrough0": {
        "gamemodeName": "Breakthrough",
        "image": "https://cdn.gametools.network/modes/bf6/breakthrough.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/breakthrough-framed.svg",
    },
    "Rush0": {
        "gamemodeName": "Rush",
        "image": "https://cdn.gametools.network/modes/bf6/rush.svg",
        "altImage": "https://cdn.gametools.network/modes/bf6/rush-framed.svg",
    },
    "ModBuilderCustom0": {
        "gamemodeName": "Portal",
        "image": "https://cdn.gametools.network/modes/bf6/wrench-hammer.svg",
        "altImage": "",
    },
}
CLASSES = {
    "kit": {
        "className": "All",
        "image": "",
        "altImage": "",
        "translationId": "ID_ARRIVAL_MUTATOR_310492599_ENTRY_0",
    },
    "kit_assault": {
        "className": "Assault",
        "image": "https://cdn.gametools.network/classes/bf6/white/Assault.svg",
        "altImage": "https://cdn.gametools.network/classes/bf6/black/Assault.svg",
        "translationId": "ID_ARRIVAL_ASSIGNMENT_CLASS_ASSAULT",
    },
    "kit_engineer": {
        "className": "Engineer",
        "image": "https://cdn.gametools.network/classes/bf6/white/Engineer.svg",
        "altImage": "https://cdn.gametools.network/classes/bf6/black/Engineer.svg",
        "translationId": "ID_ARRIVAL_ASSIGNMENT_CLASS_ENGINEER",
    },
    "kit_support": {
        "className": "Support",
        "image": "https://cdn.gametools.network/classes/bf6/white/Support.svg",
        "altImage": "https://cdn.gametools.network/classes/bf6/black/Support.svg",
        "translationId": "ID_ARRIVAL_ASSIGNMENT_CLASS_SUPPORT",
    },
    "kit_recon": {
        "className": "Recon",
        "image": "https://cdn.gametools.network/classes/bf6/white/Recon.svg",
        "altImage": "https://cdn.gametools.network/classes/bf6/black/Recon.svg",
        "translationId": "ID_ARRIVAL_ASSIGNMENT_CLASS_RECON",
    },
}
VEHICLES = {
    "veh_air_panthera": {
        "type": "Air Combat",
        "vehicleName": "Panthera KHT",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_MDV_Eurocopter_VSD0001-8003028d.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_MDV_Eurocopter_VSD0001-8003028d.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_EUROCOPTER",
    },
    "veh_air_m77efalchio": {
        "type": "Air Combat",
        "vehicleName": "M77E Falchion",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_MDV_AH64E_VSD0001-dd0a7df6.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_MDV_AH64E_VSD0001-dd0a7df6.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_AH64E",
    },
    "veh_sur_leoa4": {
        "type": "Ground Combat",
        "vehicleName": "Leo A4",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_MDV_Leopard_VSD0001-f8da51ee.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_MDV_Leopard_VSD0001-f8da51ee.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_LEOPARD",
    },
    "veh_sur_strf09a4": {
        "type": "Ground Combat",
        "vehicleName": "Strf 09 A4",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_CV90_VSD0001-acd942b6.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_CV90_VSD0001-acd942b6.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_CV90",
    },
    "veh_sur_m1a2sepv3": {
        "type": "Ground Combat",
        "vehicleName": "M1A2 SEPv3",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_MDV_Abrams_VSD0001-5412a78d.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_MDV_Abrams_VSD0001-5412a78d.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_ABRAMS",
    },
    "veh_sur_cheetah1a2": {
        "type": "Ground Combat",
        "vehicleName": "Cheetah 1A2",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_MDV_Gepard_VSD0001-d796732f.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_MDV_Gepard_VSD0001-d796732f.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_GEPARD",
    },
    "veh_sur_glider96": {
        "type": "Ground Combat",
        "vehicleName": "Glider 96",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_MDV_Flyer60_VSD0005-1569869f.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_MDV_Flyer60_VSD0005-1569869f.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_FLYER60",
    },
    "veh_sur_bradley": {
        "type": "Ground Combat",
        "vehicleName": "M3A3 Bradley",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_OB_VEH_Tank_Bradley_VSD0001_Dressing-66f252ca.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_OB_VEH_Tank_Bradley_VSD0001_Dressing-66f252ca.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_BRADLEY",
    },
    "veh_air_su57": {
        "type": "Air Combat",
        "vehicleName": "Su-57",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_MDV_SU57_VSD0001-1b5aa5ee.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_MDV_SU57_VSD0001-1b5aa5ee.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_SU57",
    },
    "veh_air_f61v": {
        "type": "Air Combat",
        "vehicleName": "F-61V",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_MDV_F16_VSD0001-5f951ec9.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_MDV_F16_VSD0001-5f951ec9.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_F16",
    },
    "veh_air_f39e": {
        "type": "Air Combat",
        "vehicleName": "F-39E",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_MDV_JAS39_VSD0001-9313d717.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_MDV_JAS39_VSD0001-9313d717.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_JAS39",
    },
    "veh_air_m77efalchion": {
        "type": "Air Combat",
        "vehicleName": "M77E Falchion",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_MDV_AH64E_VSD0001-dd0a7df6.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_MDV_AH64E_VSD0001-dd0a7df6.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_AH64E",
    },
    "veh_sur_vector": {
        "type": "Ground Transport",
        "vehicleName": "VECTOR",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_MDV_Vector_VSD0002-241efa80.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_MDV_Vector_VSD0002-241efa80.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_CARVECTOR",
    },
    "veh_sur_travmark2": {
        "type": "Ground Transport",
        "vehicleName": "Traverser Mark 2",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_Marauder_VSD0001_Icon_25667539-c29e2338.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_Marauder_VSD0001_Icon_25667539-c29e2338.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_MARAUDER",
    },
    "veh_sur_quadbike": {
        "type": "Ground Transport",
        "vehicleName": "Rugged MV740",
        "image": "https://cdn.gametools.network/vehicles/bf6/U_VEH_Car_QuadBike-f25eae5e.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/U_VEH_Car_QuadBike-f25eae5e.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_QUADBIKE",
    },
    "veh_air_f97kes": {
        "type": "Air Combat",
        "vehicleName": "F-97 Kestrel",
        "image": "https://cdn.gametools.network/vehicles/bf6/T_UI_MDV_F22_VSD0001-218f35cb.webp",
        "altImage": "https://cdn.gametools.network/vehicles/bf6/white/T_UI_MDV_F22_VSD0001-218f35cb.webp",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_F22",
    },
    "veh_air_uh06": {
        "type": "Air Transport",
        "vehicleName": "UH-06",
        "image": "",
        "translationId": None,
    },
    "veh_air_mh47": {
        "type": "Air Transport",
        "vehicleName": "MH47 Chinook",
        "image": "",
        "translationId": None,
    },
    "veh_sur_rhib": {
        "type": "Ground Transport",
        "vehicleName": "7.7m NSW RHIB",
        "image": "",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_VEHICLE_RHIB",
    },
    "veh_sur_ptv": {
        "type": "Ground Transport",
        "vehicleName": "Turfpro PTV Royal",
        "image": "",
        "translationId": None,
    },
    "veh_air_ah6litbird": {
        "type": "Air Combat",
        "vehicleName": "AH-6 Little Bird",
        "image": "",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_AH6M",
    },
    "veh_sur_moto_db01": {
        "type": "Ground Transport",
        "vehicleName": "TM/O 450",
        "image": "",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_DIRTBIKE_02",
    },
    "veh_sur_moto_db02": {
        "type": "Ground Transport",
        "vehicleName": "M1030-M1",
        "image": "",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_DIRTBIKE_01",
    },
    "veh_sur_ltv": {
        "type": "Ground Transport",
        "vehicleName": "LTV",
        "image": "",
        "translationId": None,
    },
}
VEHICLE_GROUPS = {
    "veh": {"groupName": "All"},
    "veh_air": {"groupName": "Air Combat"},
    "veh_sur": {"groupName": "Ground Combat"},
}
VEHICLE_ARCHETYPES = {
    "arch_mbt": {"archetypeName": "Main battle tank"},
    "arch_helitrans": {"archetypeName": "Transport helis"},
    "arch_ifv": {"archetypeName": "Infantry fighting vehicles"},
    "arch_heliattack": {"archetypeName": "Attack helis"},
    "arch_antiair": {"archetypeName": "Anti air tanks"},
    "arch_heliscout": {"archetypeName": "Scout helis"},
    "arch_mastery": {"archetypeName": "Mastery"},
    "arch_fighterplane": {"archetypeName": "Fighter planes"},
    "arch_jetattack": {"archetypeName": "Attack jets"},
    "arch_carapc": {"archetypeName": "Armored personnel carrier"},
    "arch_lighttrans": {"archetypeName": "Light transport vehicles"},
}
MELEE_GROUPS = {
    "melee": {"groupName": "All"},
    "melee_light": {"groupName": "Melee Light"},
    "melee_heavy": {"groupName": "Melee Heavy"},
}
MELEE = {
    "melee_light_combatknife": {
        "type": "Melee Light",
        "meleeName": "KBR Mark II",
        "image": "",  # wrong image
        "translationId": "ID_GADGET_COMBATKNIFE_NAME",
    },
    "melee_light_gekoknife": {
        "type": "Melee Light",
        "meleeName": "Bighorn HK-16",
        "image": "",  # wrong image
        "translationId": "ID_GADGET_GEKOKNIFE_NAME",
    },
    "melee_heavy_sledge": {
        "type": "Melee Heavy",
        "meleeName": "14LB Sledgehammer",
        "image": "",  # wrong image
        "translationId": "ID_ABILITY_SLEDGEHAMMER",
    },
    "melee_light_serratedblade": {
        "type": "Melee Light",
        "meleeName": 'Kapok 14"',
        "image": "",  # wrong image
        "translationId": "ID_GADGET_MACHETE_NAME",
    },
    "melee_light_icecaxe": {
        "type": "Melee Light",
        "meleeName": "Nomad CX-12",
        "image": "",  # wrong image
        "translationId": "ID_GADGET_ICECLIMBINGAXE_NAME",
    },
}
BATTLE_PICKUPS = {
    "btlp": {"battlepickupName": "All"},
    "btlp_minigun": {"battlepickupName": "Minigun"},
    "btlp_railgun": {"battlepickupName": "Railgun"},
}
WEAPONS = {
    "wp_mg_l110": {
        "type": "Machine Guns",
        "weaponName": "L110",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_Minimi_PKG_Factory_MED-0e29fce7.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_Minimi_PKG_Factory_MED-0e29fce7.webp",
        "translationId": "ID_ABILITY_MINIMI",
    },
    "wp_smg_pw5a3": {
        "type": "SMG-PDWs",
        "weaponName": "PW5A3",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_MP5MLI_PKG_Factory_MED-2d1944b7.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_MP5MLI_PKG_Factory_MED-2d1944b7.webp",
        "translationId": "ID_ABILITY_MP5",
    },
    "wp_ar_m433": {
        "type": "Assault Rifles",
        "weaponName": "M433",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_HK433_PKG_Factory_MED-b06f02f7.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_HK433_PKG_Factory_MED-b06f02f7.webp",
        "translationId": "ID_ABILITY_HK433",
    },
    "wp_mg_rpkm": {
        "type": "Machine Guns",
        "weaponName": "RPKM",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_RPKM_PKG_Factory_MED-755b785f.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_RPKM_PKG_Factory_MED-755b785f.webp",
        "translationId": "ID_ABILITY_RPKM",
    },
    "wp_sg_m87a1": {
        "type": "Shotguns",
        "weaponName": "M87A1",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_590A1_PKG_Factory_MED-4b387330.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_590A1_PKG_Factory_MED-4b387330.webp",
        "translationId": "ID_ABILITY_590A1",
    },
    "wp_pst_p18": {
        "type": "Pistols",
        "weaponName": "P18",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_M18_PKG_Factory_MED-88261bf8.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_M18_PKG_Factory_MED-88261bf8.webp",
        "translationId": "ID_ABILITY_M18",
    },
    "wp_crb_x277": {
        "type": "Carbines",
        "weaponName": "M277",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_XM7_PKG_Factory_MED-26271094.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_XM7_PKG_Factory_MED-26271094.webp",
        "translationId": "ID_ABILITY_XM7",
    },
    "wp_ar_b36a4": {
        "type": "Assault Rifles",
        "weaponName": "B36A4",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_G36_PKG_Factory_MED-fb5466ec.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_G36_PKG_Factory_MED-fb5466ec.webp",
        "translationId": "ID_ABILITY_G36",
    },
    "wp_ar_l85a3": {
        "type": "Assault Rifles",
        "weaponName": "L85A3",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_L85A3_PKG_Factory_MED-9bd0deaa.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_L85A3_PKG_Factory_MED-9bd0deaa.webp",
        "translationId": "ID_ABILITY_L85A3",
    },
    "wp_snp_m2010": {
        "type": "Rifles",
        "weaponName": "M2010 ESR",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_M2010ESR_PKG_Factory_MED-f94fdae6.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_M2010ESR_PKG_Factory_MED-f94fdae6.webp",
        "translationId": "ID_ABILITY_M2010ESR",
    },
    "wp_sg_m1014": {
        "type": "Shotguns",
        "weaponName": "M1014",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_M1014_PKG_Factory_MED-e011854a.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_M1014_PKG_Factory_MED-e011854a.webp",
        "translationId": "ID_ABILITY_M1014",
    },
    "wp_crb_ak205": {
        "type": "Carbines",
        "weaponName": "AK-205",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_AK205_PKG_Factory_MED-6d376081.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_AK205_PKG_Factory_MED-6d376081.webp",
        "translationId": "ID_ABILITY_AK205",
    },
    "wp_dmr_svk86": {
        "type": "DMRs",
        "weaponName": "SVK-8.6",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_SVCh_PKG_Factory_MED-bb06d385.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_SVCh_PKG_Factory_MED-bb06d385.webp",
        "translationId": "ID_ABILITY_SVCH",
    },
    "wp_smg_sgx": {
        "type": "SMG-PDWs",
        "weaponName": "SGX",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_MPX_PKG_Factory_MED-e822f017.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_MPX_PKG_Factory_MED-e822f017.webp",
        "translationId": "ID_ABILITY_MPX",
    },
    "wp_dmr_lmr27": {
        "type": "DMRs",
        "weaponName": "LMR27",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_ARADMR_PKG_Factory_MED-dfe224de.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_ARADMR_PKG_Factory_MED-dfe224de.webp",
        "translationId": "ID_ABILITY_ARADMR",
    },
    "wp_crb_qbz192": {
        "type": "Carbines",
        "weaponName": "QBZ-192",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_QBZ192_PKG_Factory_MED-dc0a546b.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_QBZ192_PKG_Factory_MED-dc0a546b.webp",
        "translationId": "ID_ABILITY_QBZ192",
    },
    "wp_crb_m417a2": {
        "type": "Carbines",
        "weaponName": "M417 A2",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_HK417A2_PKG_Factory_MED-494ffe6e.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_HK417A2_PKG_Factory_MED-494ffe6e.webp",
        "translationId": "ID_ABILITY_HK417A2",
    },
    "wp_mg_drsiar": {
        "type": "Machine Guns",
        "weaponName": "DRS-IAR",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_M27IAR_PKG_Factory_MED-ae6675cd.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_M27IAR_PKG_Factory_MED-ae6675cd.webp",
        "translationId": "ID_ABILITY_M27IAR",
    },
    "wp_ar_kord6p67": {
        "type": "Assault Rifles",
        "weaponName": "KORD 6P67",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_6P67_PKG_Factory_MED-827b9414.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_6P67_PKG_Factory_MED-827b9414.webp",
        "translationId": "ID_ABILITY_6P67",
    },
    "wp_smg_usg90": {
        "type": "SMG-PDWs",
        "weaponName": "USG-90",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_P90_PKG_Factory_MED-2ab1db64.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_P90_PKG_Factory_MED-2ab1db64.webp",
        "translationId": "ID_ABILITY_P90",
    },
    "wp_crb_m4a1": {
        "type": "Carbines",
        "weaponName": "M4A1",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_M4A1_PKG_Factory_MED-34529a82.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_M4A1_PKG_Factory_MED-34529a82.webp",
        "translationId": "ID_ABILITY_M4A1",
    },
    "wp_mg_kts100mk8": {
        "type": "Machine Guns",
        "weaponName": "KTS100 MK8",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_Ultimax_PKG_Factory_MED-a8ebb482.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_Ultimax_PKG_Factory_MED-a8ebb482.webp",
        "translationId": "ID_ABILITY_ULTIMAX",
    },
    "wp_pst_m45a1": {
        "type": "Pistols",
        "weaponName": "M45A1",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_M45A1_PKG_Factory_MED-8c41691b.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_M45A1_PKG_Factory_MED-8c41691b.webp",
        "translationId": "ID_ABILITY_M45A1",
    },
    "wp_smg_kv9": {
        "type": "SMG-PDWs",
        "weaponName": "KV9",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_Vector_PKG_Factory_MED-b5631ed7.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_Vector_PKG_Factory_MED-b5631ed7.webp",
        "translationId": "ID_ABILITY_VECTOR",
    },
    "wp_ar_sor556mk2": {
        "type": "Assault Rifles",
        "weaponName": "SOR-556 Mk2",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_SCARL_PKG_Factory_MED-b44467bb.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_SCARL_PKG_Factory_MED-b44467bb.webp",
        "translationId": "ID_ABILITY_SCARL",
    },
    "wp_smg_pw7a2": {
        "type": "SMG-PDWs",
        "weaponName": "PW7A2",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_MP7A2_PKG_Factory_MED-406bc965.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_MP7A2_PKG_Factory_MED-406bc965.webp",
        "translationId": "ID_ABILITY_MP7A2",
    },
    "wp_mg_m123k": {
        "type": "Machine Guns",
        "weaponName": "M123K",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_MG4K_PKG_Factory_MED-cc064690.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_MG4K_PKG_Factory_MED-cc064690.webp",
        "translationId": "ID_ABILITY_MG4K",
    },
    "wp_pst_m44": {
        "type": "Pistols",
        "weaponName": "M44",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_RagingHunter_PKG_Factory_MED-f9773307.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_RagingHunter_PKG_Factory_MED-f9773307.webp",
        "translationId": "ID_ABILITY_RH44",
    },
    "wp_mg_xm250": {
        "type": "Machine Guns",
        "weaponName": "M250",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_M250_PKG_Factory_MED-6e230a71.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_M250_PKG_Factory_MED-6e230a71.webp",
        "translationId": "ID_ABILITY_M250",
    },
    "wp_smg_umg40": {
        "type": "SMG-PDWs",
        "weaponName": "UMG-40",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_UMP40_PKG_Factory_MED-22afa646.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_UMP40_PKG_Factory_MED-22afa646.webp",
        "translationId": "ID_ABILITY_UMP40",
    },
    "wp_ar_tr7": {
        "type": "Assault Rifles",
        "weaponName": "TR-7",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_Tavor7_PKG_Factory_MED-e682f267.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_Tavor7_PKG_Factory_MED-e682f267.webp",
        "translationId": "ID_ABILITY_TAVOR7",
    },
    "wp_smg_sl9": {
        "type": "SMG-PDWs",
        "weaponName": "SL9",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_APDW_PKG_Factory_MED-c4d1b829.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_APDW_PKG_Factory_MED-c4d1b829.webp",
        "translationId": "ID_ABILITY_APDW",
    },
    "wp_mg_m240l": {
        "type": "Machine Guns",
        "weaponName": "M240L",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_M240L_PKG_Factory_MED-1fa18e0c.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_M240L_PKG_Factory_MED-1fa18e0c.webp",
        "translationId": "ID_ABILITY_M240L",
    },
    "wp_smg_scw10": {
        "type": "SMG-PDWs",
        "weaponName": "SCW-10",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_APC10_PKG_Factory_MED-716a97fb.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_APC10_PKG_Factory_MED-716a97fb.webp",
        "translationId": "ID_ABILITY_APC10",
    },
    "wp_ar_nvo228e": {
        "type": "Assault Rifles",
        "weaponName": "NVO-228E",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_ACE32_PKG_Factory_MED-39a97220.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_ACE32_PKG_Factory_MED-39a97220.webp",
        "translationId": "ID_ABILITY_ACE32",
    },
    "wp_mg_m60": {
        "type": "Machine Guns",
        "weaponName": "M/60",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_M60E6_PKG_Factory_MED-e600bb28.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_M60E6_PKG_Factory_MED-e600bb28.webp",
        "translationId": "ID_ABILITY_M60E6",
    },
    "wp_snp_psr": {
        "type": "Rifles",
        "weaponName": "PSR",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_MRAD_PKG_Factory_MED-5035ce99.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_MRAD_PKG_Factory_MED-5035ce99.webp",
        "translationId": "ID_ABILITY_MRAD",
    },
    "wp_dmr_svdm": {
        "type": "DMRs",
        "weaponName": "SVDM",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_SVDM_PKG_Factory_MED-b6c9aa50.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_SVDM_PKG_Factory_MED-b6c9aa50.webp",
        "translationId": "ID_ABILITY_SVDM",
    },
    "wp_ar_ak4d": {
        "type": "Assault Rifles",
        "weaponName": "AK4D",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_G3A4_PKG_Factory_MED-0575cf00.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_G3A4_PKG_Factory_MED-0575cf00.webp",
        "translationId": "ID_ABILITY_G3A4",
    },
    "wp_crb_sor300sc": {
        "type": "Carbines",
        "weaponName": "SOR-300SC",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_SCARSC_PKG_Factory_MED-7a6a50ff.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_SCARSC_PKG_Factory_MED-7a6a50ff.webp",
        "translationId": "ID_ABILITY_SCARSC",
    },
    "wp_crb_sg553r": {
        "type": "Carbines",
        "weaponName": "SG 553R",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_SIG553R_PKG_Factory_MED-afc2dfa8.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_SIG553R_PKG_Factory_MED-afc2dfa8.webp",
        "translationId": "ID_ABILITY_SIG553R",
    },
    "wp_crb_grtbc": {
        "type": "Carbines",
        "weaponName": "GRT-BC",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_MSBSGROTB_PKG_Factory_MED-25acf006.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_MSBSGROTB_PKG_Factory_MED-25acf006.webp",
        "translationId": "ID_ABILITY_MSBSGROT",
    },
    "wp_sg_185ksk": {
        "type": "Shotguns",
        "weaponName": "18.5KS-K",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_185KSK_PKG_Factory_MED-432c353f.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_MSBSGROTB_PKG_Factory_MED-25acf006.webp",
        "translationId": "ID_ABILITY_185KSK",
    },
    "wp_pst_es57": {
        "type": "Pistols",
        "weaponName": "ES 5.7",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_FiveSeven_PKG_Factory_MED-c540cde7.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_FiveSeven_PKG_Factory_MED-c540cde7.webp",
        "translationId": "ID_ABILITY_FIVESEVEN",
    },
    "wp_dmr_m39emr": {
        "type": "DMRs",
        "weaponName": "M39 EMR",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_M39EMR_PKG_Factory_MED-e17b5963.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_M39EMR_PKG_Factory_MED-e17b5963.webp",
        "translationId": "ID_ABILITY_M39EMR",
    },
    "wp_snp_sv98": {
        "type": "Rifles",
        "weaponName": "SV-98",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_SV98M_PKG_Factory_MED-c38f085a.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_SV98M_PKG_Factory_MED-c38f085a.webp",
        "translationId": "ID_ABILITY_SV98M",
    },
    "wp_pst_m357trait": {
        "type": "Pistols",
        "weaponName": "M357 Trait",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_TRR8_PKG_Factory_MED-815434c3.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_TRR8_PKG_Factory_MED-815434c3.webp",
        "translationId": "ID_ABILITY_TRR8",
    },
    "wp_pst_ggh22": {
        "type": "Pistols",
        "weaponName": "GGH-22",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_G22_PKG_Factory_MED-0faaf1e3.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_G22_PKG_Factory_MED-0faaf1e3.webp",
        "translationId": "ID_ABILITY_G22",
    },
    "wp_snp_miniscout": {
        "type": "Rifles",
        "weaponName": "Mini Scout",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_MiniFix_PKG_Factory_MED-c8bab5ff.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_MiniFix_PKG_Factory_MED-c8bab5ff.webp",
        "translationId": "ID_ABILITY_MINIFIX",
    },
    "wp_sg_db12": {
        "type": "Shotguns",
        "weaponName": "DB-12",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_DP12_PKG_Factory_MED-0335554d.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_DP12_PKG_Factory_MED-0335554d.webp",
        "translationId": "ID_ABILITY_DP12",
    },
    "wp_ar_vhsk2": {
        "type": "Assault Rifles",
        "weaponName": "VCR-2",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_VHS2_Factory_Icon-a82fc1f9.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_VHS2_Factory_Icon-a82fc1f9.webp",
        "translationId": "ID_ABILITY_VHS2",
    },
    "wp_dmr_msbsgrotc": {
        "type": "DMRs",
        "weaponName": "GRT-CPS",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_MSBSGROTCPS_Factory_Icon-096caf67.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_MSBSGROTCPS_Factory_Icon-096caf67.webp",
        "translationId": "ID_ABILITY_GROTC",
    },
    "wp_pst_vz61": {
        "type": "Pistols",
        "weaponName": "vz. 61",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_Skorpion_Factory_Icon-a6d915ec.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_Skorpion_Factory_Icon-a6d915ec.webp",
        "translationId": "ID_ABILITY_SKORPION",
    },
    "wp_smg_cz3a1": {
        "type": "SMG-PDWs",
        "weaponName": "CZ3A1",
        "image": "https://cdn.gametools.network/weapons/bf6/T_UI_ScorpionEvo3_Factory_Icon-5391cf9f.webp",
        "altImage": "https://cdn.gametools.network/weapons/bf6/white/T_UI_ScorpionEvo3_Factory_Icon-5391cf9f.webp",
        "translationId": "ID_ABILITY_SCORPIONEVO3",
    },
    "wp_mg_mg525btk": {
        "type": "Machine Guns",
        "weaponName": "M121 A2",
        "image": "",
        "translationId": "ID_ABILITY_MG5",
    },
}
WEAPON_GROUPS = {
    "wp_temp": {
        "groupName": "All",
        "translationId": "ID_ARRIVAL_MUTATOR_310492599_ENTRY_0",
    },
    "wp_snp": {
        "groupName": "Rifles",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_RIFLE",
    },
    "wp_crb": {
        "groupName": "Carbines",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_CARBINE",
    },
    "wp_mg": {
        "groupName": "Machine Guns",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_MACHINEGUN",
    },
    "wp_sg": {
        "groupName": "Shotguns",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_SHOTGUN",
    },
    "wp_ar": {
        "groupName": "Assault Rifles",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_ASSAULTRIFLE",
    },
    "wp_smg": {
        "groupName": "SMG-PDWs",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_SMGPDW",
    },
    "wp_dmr": {
        "groupName": "DMRs",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_DMR",
    },
    "wp_pst_temp": {
        "groupName": "Pistols",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_PISTOL",
    },
}
GADGETS = {
    "gad_callin_airstrike": {
        "type": "Strike Packages",
        "gadgetName": "Air Strike",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_CALLINS_Airstrike_Thumb-638b4ee1.png",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_GRANITEAIRSTRIKE",
    },
    "gad_mpaps": {
        "type": "Deployable Gadgets",
        "gadgetName": "MP-APS",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_MPAPS_Icon-b735994d.png",
        "translationId": "ID_GADGET_MPAPS_NAME",
    },
    "gad_gpdis": {
        "type": "Deployable Gadgets",
        "gadgetName": "GPDIS",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_EIDOS_Icon-2273a3ee.png",
        "translationId": "ID_GADGET_EIDOS_NAME",
    },
    "gad_c4": {
        "type": "Explosives",
        "gadgetName": "C-4 Explosives",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_C4_Icon-330d6ee2.png",
        "translationId": "ID_GADGET_C4_NAME",
    },
    "gad_gl_he": {
        "type": "Grenade Launchers",
        "gadgetName": "M320A1 HE",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_M320_HE_Icon-83b61ed0.png",
        "translationId": "ID_GADGET_M320HE_NAME",
    },
    "gad_rl_ungui": {
        "type": "Launchers",
        "gadgetName": "RPG-7V2",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_RPG7v2_Icon-ce5453fd.png",
        "translationId": "ID_GADGET_RPG7V2_NAME",
    },
    "gad_rl_aimgui": {
        "type": "Launchers",
        "gadgetName": "M136 AT",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_AT4_Icon-beadb575.png",
        "translationId": "ID_GADGET_AT4_NAME",
    },
    "gad_mine_press": {
        "type": "Explosives",
        "gadgetName": "M15",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_AT_Mine_Icon-2288ec8e.png",
        "translationId": "ID_GADGET_ATMINE_NAME",
    },
    "gad_gl_tb": {
        "type": "Grenade Launchers",
        "gadgetName": "M320A1 THRM",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_M320_Thermobaric_Icon-3f13c762.png",
        "translationId": "ID_GADGET_M320THERMOBARIC_NAME",
    },
    "gad_rl_longra": {
        "type": "Launchers",
        "gadgetName": "MAS 148 Glaive",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_Javelin_Icon-a0ce2091.png",
        "translationId": "ID_GADGET_JAVELIN_NAME",
    },
    "gad_mine_ap": {
        "type": "Explosives",
        "gadgetName": "M18A1",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_Claymore_Icon-5c7f1590.png",
        "translationId": "ID_GADGET_CLAYMORE_NAME",
    },
    "gad_mine_tws": {
        "type": "Explosives",
        "gadgetName": "M4A1 SLAM",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_M4_SLAM_Icon-541f624c.png",
        "translationId": "M4A1 SLAM",
    },
    "gad_gl_breach": {
        "type": "Grenade Launchers",
        "gadgetName": "X95 BRE",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_Drill_Launcher_Icon-1e1481d9.png",
        "translationId": "ID_GADGET_DRILLLAUNCHER_NAME",
    },
    "gad_mine_mosen": {
        "type": "Explosives",
        "gadgetName": "PTKM-1R",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_PTKM_1R_Icon-ceb07fc0.png",
        "translationId": "ID_GADGET_PTKM1R_NAME",
    },
    "gad_rl_surtoair": {
        "type": "Launchers",
        "gadgetName": "SLM-93A",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_Stinger_Icon-d4590623.png",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_STINGER",
    },
    "gad_il_airburst": {
        "type": "Grenade Launchers",
        "gadgetName": "Sich G1 WP",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_Airburst_Incendiary_Launcher_Icon-da8af82a.png",
        "translationId": "ID_GADGET_AIRBURSTINCENDIARYLAUNCHER_NAME",
    },
    "gad_deploymortar": {
        "type": "Class Gadgets",
        "gadgetName": "LWCMS",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_Deployable_Mortar_Icon-97b13652.png",
        "translationId": "ID_GADGET_DEPLOYABLEMORTAR_NAME",
    },
    "gad_deploybeacon": {
        "type": "Deployable Gadgets",
        "gadgetName": "QLink 6",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_Spawn_Beacon_Icon-b6e67f1c.png",
        "translationId": "ID_GADGET_SPAWNBEACON_NAME",
    },
    "gad_gl_smoke": {
        "type": "Grenade Launchers",
        "gadgetName": "M320A1 SMK",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_M320_Smoke_Icon-dfa762d9.png",
        "translationId": "ID_GADGET_M320SMOKE_NAME",
    },
    "gad_callin_wpdrop": {
        "type": "Strike Packages",
        "gadgetName": "Weapon Drop",
        "image": "https://cdn.gametools.network/gadgets/bf6/U_Gadget_WeaponDrop_Granite-2c6c3b16.webp",
        "translationId": "ID_GADGET_CALLINWEAPONDROP_NAME",
    },
    "gad_callin_uav": {
        "type": "Strike Packages",
        "gadgetName": "UAV Overwatch",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_CALLINS_Uav_Thumb-fdf9a78e.png",
        "translationId": "ID_GRANITE_CALLIN_UAV",
    },
    "gad_callin_antiveh": {
        "type": "Strike Packages",
        "gadgetName": "Anti-Vehicle Drop",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_CALLINS_SupAnti_Thumb-84fc98fc.png",
        "translationId": "ID_GRANITE_CALLIN_ANTIVEHICLEDROP",
    },
    "gad_callin_smoke": {
        "type": "Strike Packages",
        "gadgetName": "Smoke Screen",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_CALLINS_Smoke_Thumb-5d515d26.png",
        "translationId": "ID_GADGET_CALLINSMOKESCREEN_NAME",
    },
    "gad_callin_artstrike": {
        "type": "Strike Packages",
        "gadgetName": "Artillery Strike",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_CALLINS_Artillery_Thumb-126cad71.png",
        "translationId": "ID_GADGET_CALLINARTILLERYSTRIKE_NAME",
    },
    "gad_gren_av": {
        "type": "Throwables",
        "gadgetName": "SCG-24",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_AntiTank_Grenade_Icon-82f8def3.png",
        "translationId": "ID_GADGET_ANTITANKGRENADE_NAME",
    },
    "gad_ubsg_incen": {
        "type": "Misc. Equipment",
        "gadgetName": "SS26",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_M26_Mass_Dragonsbreath_Icon-f7daa1ac.png",
        "translationId": "ID_GADGET_M26MASSDRAGONSBREATH_NAME",
    },
    "gad_eodbot": {
        "type": "Deployable Gadgets",
        "gadgetName": "CSB IV",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_EOD_Bot_Icon-6f474b0e.png",
        "translationId": "ID_GADGET_EODBOT_NAME",
    },
    "gad_tugs": {
        "type": "Class Gadgets",
        "gadgetName": "T-UGS",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_T_UGS_Icon-5b910fc6.png",
        "translationId": "ID_GADGET_TUGS_NAME",
    },
    "gad_ladder": {
        "type": "Deployable Gadgets",
        "gadgetName": "Tarantula ALX",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_Assault_Ladder_Icon-3700a067.png",
        "translationId": "ID_GADGET_ASSAULTLADDER_NAME",
    },
    "gad_sup_pouch": {
        "type": "Misc. Equipment",
        "gadgetName": "Goliath Compact",
        "image": "https://cdn.gametools.network/gadgets/bf6/T_UI_Supply_Pouch_Icon-40691f80.png",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_SUPPLYPOUCH",
    },
    "gad_lancet": {
        "type": "Misc. Equipment",
        "gadgetName": "DGMK4",
        "image": "",
        "translationId": "ID_GADGET_LANCET_NAME",
    },
    "gad_callin_armor": {
        "type": "",
        "gadgetName": "ARMOR DROP",
        "image": "",
        "translationId": "ID_GRANITE_CALLIN_ARMOR",
    },
    "gad_rl_igla": {
        "type": "Class Gadgets",
        "gadgetName": "9K38 Igla",
        "image": "",
        "translationId": "ID_GADGET_IGLA_NAME",
    },
    "gad_gren_mfrag": {
        "type": "",
        "gadgetName": "Mini Grenade",
        "image": "",
        "translationId": None,
    },
    "gad_gren_frag": {
        "type": "Grenade",
        "gadgetName": "Frag Grenade",
        "image": "",
        "translationId": None,
    },
    "gad_repair": {
        "type": "",
        "gadgetName": "Repair Tool",
        "image": "",
        "translationId": None,
    },
    "gad_gren_inc": {
        "type": "Grenade",
        "gadgetName": "Incendiary Grenade",
        "image": "",
        "translationId": None,
    },
    "gad_sup_bag": {
        "type": "",
        "gadgetName": "Supply Bag",
        "image": "",
        "translationId": None,
    },
    "gad_deplocover": {
        "type": "",
        "gadgetName": "Deployable Cover",
        "image": "",
        "translationId": None,
    },
    "gad_gren_stun": {
        "type": "",
        "gadgetName": "Stun Grenade",
        "image": "",
        "translationId": None,
    },
    "gad_gren_smoke": {
        "type": "",
        "gadgetName": "Smoke Grenade",
        "image": "",
        "translationId": None,
    },
    "gad_gren_flash": {
        "type": "",
        "gadgetName": "Flash Grenade",
        "image": "",
        "translationId": None,
    },
    "gad_recondrone": {
        "type": "",
        "gadgetName": "Recon Drone",
        "image": "",
        "translationId": None,
    },
    "gad_laserdes": {
        "type": "",
        "gadgetName": "Laser Designator",
        "image": "",
        "translationId": None,
    },
    "gad_adren": {
        "type": "",
        "gadgetName": "Adrenaline Injector",
        "image": "",
        "translationId": None,
    },
    "gad_vehsupcra": {
        "type": "",
        "gadgetName": "Supply Crate",
        "image": "",
        "translationId": None,
    },
    "gad_tknife": {
        "type": "",
        "gadgetName": "Throwing Knife",
        "image": "",
        "translationId": None,
    },
    "gad_msensor": {
        "type": "",
        "gadgetName": "Proximity Detector",
        "image": "",
        "translationId": None,
    },
    "gad_deployable": {
        "type": "",
        "gadgetName": "Deployable Cover",
        "image": "",
        "translationId": None,
    },
    "gad_decoy": {
        "type": "",
        "gadgetName": "Sniper Decoy",
        "image": "",
        "translationId": None,
    },
    "gad_callin_resupply": {
        "type": "Strike Packages",
        "gadgetName": "",
        "image": "",
        "translationId": None,
    },
    "gad_gasmask": {
        "type": "",
        "gadgetName": "Gas mask",
        "image": "",
        "translationId": None,
    },
    "gad_callin_mobresp": {
        "type": "",
        "gadgetName": "Mobile respawn",
        "image": "",
        "translationId": None,
    },
    "gad_defib": {
        "type": "",
        "gadgetName": "Defibrillator",
        "image": "",
        "translationId": None,
    },
    "gad_tdart": {
        "type": "",
        "gadgetName": "Tracer Dart",
        "image": "",
        "translationId": None,
    },
}

GADGET_GROUPS = {
    "gad_temp": {
        "groupName": "All",
        "translationId": "ID_ARRIVAL_MUTATOR_310492599_ENTRY_0",
    },
    "gad_gl": {
        "groupName": "Grenade Launchers",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_GRENADE_LAUNCHERS",
    },
    "gad_mine": {
        "groupName": "Explosives",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_EQUIPMENTEXPLOSIVE",
    },
    "gad_grenades": {"groupName": "Grenades", "translationId": None},
    "gad_rl": {
        "groupName": "Launchers",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_LAUNCHER",
    },
    "gad_il": {
        "groupName": "Grenade Launchers",
        "translationId": "ID_ARRIVAL_CATEGORIZATIONTAG_NAME_GRENADE_LAUNCHERS",
    },
    "gad_callins": {"groupName": "Call-ins", "translationId": None},
}

RANK_IMAGES = {
    1: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_001_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_001_lg.png",
    },
    2: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_002_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_002_lg.png",
    },
    3: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_003_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_003_lg.png",
    },
    4: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_004_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_004_lg.png",
    },
    5: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_005_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_005_lg.png",
    },
    6: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_006_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_006_lg.png",
    },
    7: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_007_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_007_lg.png",
    },
    8: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_008_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_008_lg.png",
    },
    9: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_009_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_009_lg.png",
    },
    10: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_010_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_010_lg.png",
    },
    11: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_011_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_011_lg.png",
    },
    12: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_012_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_012_lg.png",
    },
    13: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_013_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_013_lg.png",
    },
    14: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_014_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_014_lg.png",
    },
    15: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_015_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_015_lg.png",
    },
    16: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_016_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_016_lg.png",
    },
    17: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_017_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_017_lg.png",
    },
    18: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_018_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_018_lg.png",
    },
    19: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_019_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_019_lg.png",
    },
    20: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_020_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_020_lg.png",
    },
    21: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_021_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_021_lg.png",
    },
    22: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_022_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_022_lg.png",
    },
    23: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_023_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_023_lg.png",
    },
    24: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_024_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_024_lg.png",
    },
    25: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_025_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_025_lg.png",
    },
    26: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_026_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_026_lg.png",
    },
    27: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_027_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_027_lg.png",
    },
    28: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_028_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_028_lg.png",
    },
    29: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_029_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_029_lg.png",
    },
    30: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_030_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_030_lg.png",
    },
    31: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_031_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_031_lg.png",
    },
    32: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_032_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_032_lg.png",
    },
    33: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_033_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_033_lg.png",
    },
    34: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_034_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_034_lg.png",
    },
    35: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_035_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_035_lg.png",
    },
    36: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_036_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_036_lg.png",
    },
    37: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_037_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_037_lg.png",
    },
    38: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_038_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_038_lg.png",
    },
    39: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_039_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_039_lg.png",
    },
    40: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_040_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_040_lg.png",
    },
    41: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_041_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_041_lg.png",
    },
    42: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_042_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_042_lg.png",
    },
    43: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_043_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_043_lg.png",
    },
    44: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_044_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_044_lg.png",
    },
    45: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_045_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_045_lg.png",
    },
    46: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_046_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_046_lg.png",
    },
    47: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_047_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_047_lg.png",
    },
    48: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_048_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_048_lg.png",
    },
    49: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_049_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_049_lg.png",
    },
    50: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_050_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_050_lg.png",
    },
    55: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_055_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_055_lg.png",
    },
    60: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_060_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_060_lg.png",
    },
    65: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_065_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_065_lg.png",
    },
    70: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_070_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_070_lg.png",
    },
    75: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_075_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_075_lg.png",
    },
    80: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_080_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_080_lg.png",
    },
    85: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_085_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_085_lg.png",
    },
    90: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_090_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_090_lg.png",
    },
    95: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_095_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_095_lg.png",
    },
    100: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_100_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_100_lg.png",
    },
    110: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_110_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_110_lg.png",
    },
    120: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_120_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_120_lg.png",
    },
    130: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_130_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_130_lg.png",
    },
    140: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_140_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_140_lg.png",
    },
    150: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_150_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_150_lg.png",
    },
    160: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_160_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_160_lg.png",
    },
    170: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_170_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_170_lg.png",
    },
    180: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_180_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_180_lg.png",
    },
    190: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_190_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_190_lg.png",
    },
    200: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_200_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_200_lg.png",
    },
    210: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_210_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_210_lg.png",
    },
    220: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_220_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_220_lg.png",
    },
    230: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_230_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_230_lg.png",
    },
    240: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_240_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_240_lg.png",
    },
    250: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_250_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_250_lg.png",
    },
    260: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_260_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_260_lg.png",
    },
    270: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_270_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_270_lg.png",
    },
    280: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_280_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_280_lg.png",
    },
    290: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_290_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_290_lg.png",
    },
    300: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_300_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_300_lg.png",
    },
    310: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_310_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_310_lg.png",
    },
    320: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_320_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_320_lg.png",
    },
    330: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_330_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_330_lg.png",
    },
    340: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_340_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_340_lg.png",
    },
    350: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_350_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_350_lg.png",
    },
    360: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_360_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_360_lg.png",
    },
    370: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_370_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_370_lg.png",
    },
    380: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_380_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_380_lg.png",
    },
    390: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_390_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_390_lg.png",
    },
    400: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_400_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_400_lg.png",
    },
    410: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_410_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_410_lg.png",
    },
    420: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_420_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_420_lg.png",
    },
    430: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_430_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_430_lg.png",
    },
    440: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_440_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_440_lg.png",
    },
    450: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_450_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_450_lg.png",
    },
    460: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_460_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_460_lg.png",
    },
    470: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_470_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_470_lg.png",
    },
    480: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_480_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_480_lg.png",
    },
    490: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_490_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_490_lg.png",
    },
    500: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_500_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_500_lg.png",
    },
    1000: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_1000_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_1000_lg.png",
    },
    1500: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_1500_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_1500_lg.png",
    },
    2000: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_2000_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_2000_lg.png",
    },
    2500: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_2500_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_2500_lg.png",
    },
    3000: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_3000_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_3000_lg.png",
    },
    3500: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_3500_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_3500_lg.png",
    },
    4000: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_4000_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_4000_lg.png",
    },
    4500: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_4500_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_4500_lg.png",
    },
    5000: {
        "small": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_5000_sm.png",
        "large": "https://cdn.gametools.network/ranks/bf6/t_ui_rank_5000_lg.png",
    },
}
