import os
import json
new_module = __import__("accessible_output2.outputs.auto")
ao_output = new_module.outputs.auto.Auto()
ao_output.output("test", True)

cwd = os.getcwd()
interface_path = os.path.join(cwd, "interface.json")
if not (os.path.isfile(interface_path)):
    window = {
        "tag": "CharacterWindow",
        "type": "tabbed_interface",
        "script": "character_window",
        "tabs": [
            {
                "name": "consorts",
                "tag": "consorts",
                "type": "table",
                "categories": [
                    {"name": "Primary Spouse", "tag": "primary"},
                    {"name": "Betrothed", "tag": "betrothed"},
                    {"name": "Spouse", "tag": "spouses"},
                    {"name": "Concubine", "tag": "concubines"}
                    ],
                "rows" : "char",
                "row_title": "name",
                "columns": [{"name": "Gender", "tag": "gender"}, {"name": "Age", "tag": "age"}, {"name": "Health", "tag": "health"}, {"name": "Faith", "tag": "faith"}, {"name": "Religion", "tag": "religion"}, {"name": "Culture", "tag": "culture"}, {"name": "Culture Group", "tag": "culture_group"}, {"name": "Marital Status", "tag": "marital_status"}, {"name": "Relationship to Player", "tag":"player_relation"}, {"name": "Opinion of Player", "tag": "player_opinion"}, {"name": "Opinion of Player breakdown", "tag": "player_opinion_breakdown"}, {"name": "Relationship to Selected Character", "tag": "selected_relation"}, {"name": "Opinion of Selected Character", "tag": "selected_opinion"}, {"name": "Opinion of Selected Character Breakdown", "tag": "selected_opinion_breakdown"}, {"name": "Character ID", "tag": "id"}]
    
                },
            {
                "name": "Heirs",
                "tag": "heirs",
                "type": "table",
                "rows" : "char",
                "row_title": "name",
                "columns": [{"name": "Gender", "tag": "gender"}, {"name": "Age", "tag": "age"}, {"name": "Health", "tag": "health"}, {"name": "Faith", "tag": "faith"}, {"name": "Religion", "tag": "religion"}, {"name": "Culture", "tag": "culture"}, {"name": "Culture Group", "tag": "culture_group"}, {"name": "Marital Status", "tag": "marital_status"}, {"name": "Relationship to Player", "tag":"player_relation"}, {"name": "Opinion of Player", "tag": "player_opinion"}, {"name": "Opinion of Player breakdown", "tag": "player_opinion_breakdown"}, {"name": "Relationship to Selected Character", "tag": "selected_relation"}, {"name": "Opinion of Selected Character", "tag": "selected_opinion"}, {"name": "Opinion of Selected Character Breakdown", "tag": "selected_opinion_breakdown"}, {"name": "Character ID", "tag": "id"}]
                },
            {
                "name": "Lieges",
                "tag": "lieges",
                "type": "table",
                "rows" : "char",
                "row_title": "name",
                "columns": [{"name": "Gender", "tag": "gender"}, {"name": "Age", "tag": "age"}, {"name": "Health", "tag": "health"}, {"name": "Faith", "tag": "faith"}, {"name": "Religion", "tag": "religion"}, {"name": "Culture", "tag": "culture"}, {"name": "Culture Group", "tag": "culture_group"}, {"name": "Marital Status", "tag": "marital_status"}, {"name": "Relationship to Player", "tag":"player_relation"}, {"name": "Opinion of Player", "tag": "player_opinion"}, {"name": "Opinion of Player breakdown", "tag": "player_opinion_breakdown"}, {"name": "Relationship to Selected Character", "tag": "selected_relation"}, {"name": "Opinion of Selected Character", "tag": "selected_opinion"}, {"name": "Opinion of Selected Character Breakdown", "tag": "selected_opinion_breakdown"}, {"name": "Character ID", "tag": "id"}]
                },
            {
                "name": "Close Family",
                "tag": "family",
                "type": "table",
                "rows" : "char",
                "row_title": "name",
                "columns": [{"name": "Gender", "tag": "gender"}, {"name": "Age", "tag": "age"}, {"name": "Health", "tag": "health"}, {"name": "Faith", "tag": "faith"}, {"name": "Religion", "tag": "religion"}, {"name": "Culture", "tag": "culture"}, {"name": "Culture Group", "tag": "culture_group"}, {"name": "Marital Status", "tag": "marital_status"}, {"name": "Relationship to Player", "tag":"player_relation"}, {"name": "Opinion of Player", "tag": "player_opinion"}, {"name": "Opinion of Player breakdown", "tag": "player_opinion_breakdown"}, {"name": "Relationship to Selected Character", "tag": "selected_relation"}, {"name": "Opinion of Selected Character", "tag": "selected_opinion"}, {"name": "Opinion of Selected Character Breakdown", "tag": "selected_opinion_breakdown"}, {"name": "Character ID", "tag": "id"}]
                },
            {
                "name": "Vassals",
                "tag": "vassals",
                "type": "table",
                "rows" : "char",
                "row_title": "name",
                "columns": [{"name": "Gender", "tag": "gender"}, {"name": "Age", "tag": "age"}, {"name": "Health", "tag": "health"}, {"name": "Faith", "tag": "faith"}, {"name": "Religion", "tag": "religion"}, {"name": "Culture", "tag": "culture"}, {"name": "Culture Group", "tag": "culture_group"}, {"name": "Marital Status", "tag": "marital_status"}, {"name": "Relationship to Player", "tag":"player_relation"}, {"name": "Opinion of Player", "tag": "player_opinion"}, {"name": "Opinion of Player breakdown", "tag": "player_opinion_breakdown"}, {"name": "Relationship to Selected Character", "tag": "selected_relation"}, {"name": "Opinion of Selected Character", "tag": "selected_opinion"}, {"name": "Opinion of Selected Character Breakdown", "tag": "selected_opinion_breakdown"}, {"name": "Character ID", "tag": "id"}]
                },
            {
                "name": "Courtiers",
                "tag": "courtiers",
                "type": "table",
                "rows" : "char",
                "row_title": "name",
                "columns": [{"name": "Gender", "tag": "gender"}, {"name": "Age", "tag": "age"}, {"name": "Health", "tag": "health"}, {"name": "Faith", "tag": "faith"}, {"name": "Religion", "tag": "religion"}, {"name": "Culture", "tag": "culture"}, {"name": "Culture Group", "tag": "culture_group"}, {"name": "Marital Status", "tag": "marital_status"}, {"name": "Relationship to Player", "tag":"player_relation"}, {"name": "Opinion of Player", "tag": "player_opinion"}, {"name": "Opinion of Player breakdown", "tag": "player_opinion_breakdown"}, {"name": "Relationship to Selected Character", "tag": "selected_relation"}, {"name": "Opinion of Selected Character", "tag": "selected_opinion"}, {"name": "Opinion of Selected Character Breakdown", "tag": "selected_opinion_breakdown"}, {"name": "Character ID", "tag": "id"}]
                }
            ]
        }
    jlist = [window
        ]
    json_object = json.dumps(jlist, indent=4)
    with open("interface.json", "w") as outfile:
        outfile.write(json_object)
		