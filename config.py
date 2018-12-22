# -*- coding: utf-8 -*-
"""
说明:   1.默认情况，以第一个字段为key, 有且只有一个key, 不需要在此配置表添加
		2.不需要key的情况，keytype为0
		3.需要指定非第一个地段为key或者多个key的情况，keytype为1, 并且需要填写指定的key对应的字段名
		4.支持一表多sheet, 每个sheet配置情况同1,2,3
		5.默认屏蔽以字符 "_" 开头为sheet名称的sheet
"""

CONFIG = {
	'AvatarConf.xlsx' : {
		'ExtraExp' : {'key' : ['Level', 'activity'], 'keytype' : 1}
	},
	'JobValueConf.xlsx' : { 
		'JobValue' : {'key' : ['occupationId', 'base_attr'], 'keytype' : 1}
	},

	'MapInfoConf.xlsx' : { 
		'AreaMap'				: {'key' : ['AreaMapID', 'WildMapID'], 'keytype' : 1},
		'WildMapMonsterGourpID' : {'key' : ['WildMapMonsterGourpID', 'WildMapMonsterID'], 'keytype' : 1},
		'WildMapEventGourpID'   : {'key' : ['WildMapEventGourpID', 'WildMapEventID'], 'keytype' : 1}
	},
	'Map3D.xlsx' : {
		'Map'	: {'key' : ['mapType', 'objectType'], 'keytype' : 1}
	},
	
	'GuideConf.xlsx' : {
		'Guide' : {'key' : ['groupid', 'guideid'], 'keytype' : 1}
	},
	
	'JobValueConf.xlsx' : {
		'JobValue'	: {'key' : ['occupationId', 'base_attr'], 'keytype' : 1}
	},
	'FishPointConf.xlsx' : {
		'fish_point_id'	: {'key' : ['fish_point_id','index_id'], 'keytype' : 1},
        'fish_pond_id':   {'key':['fish_pond_id','index_id'],'keytype': 1},
        'fishfeel_pond_id': {'key':['fishfeel_pond_id','index_id'],'keytype':1},
		'FishPoints': {'key':['map_id','fish_point_id'],'keytype':1}
	},
	'EquipConfig.xlsx' : {
		'refine_library' : {'key' : ['refine_library_id','property_type'], 'keytype' : 1},
		'effect_library' : {'key' : ['effect_library','effect_id'], 'keytype' : 1}
	},
        'EquipStrengthen.xlsx' : {
		'strengthen' : {'key' : ['equip_id','equipstrengthen_lv'], 'keytype' : 1}
	},
	'MinePointConf.xlsx' : {
		'ore_pond'	: {'key' : ['ore_pond_id','ore_type'], 'keytype' : 1},
		'MinePoints': {'key':['map_id','mine_point_id'],'keytype':1}
	},
	'CookConf.xlsx' : {
        'cook_pond':   {'key':['cook_pond_id','food_id'],'keytype': 1}
    },
	'SkillConfig.xlsx' : {
		'level'	: {'key':['effect_id', 'level'], 'keytype' : 1},
		'molecule' : {'key':['skillid', 'molecule_id'], 'keytype' : 1}
	},
	'MonsterConf.xlsx' : {
		'Monster_Grown': {'key':['grown_id', 'level_min'], 'keytype' : 1},
		'Monster_Group2d': {'key':['monster_groupid', 'monster_id'], 'keytype' : 1},
		'Monster_Group3d': {'key':['monster_groupid'], 'keytype' : 1}
	},
	'NpcConf.xlsx' : {
		'NpcConf' : {'key':['npcId'], 'keytype' : 1}
	},
	'MapConf.xlsx' : {
		'Map_Monster_Point': {'key':['mapId', 'monster_point'], 'keytype' : 1},
		'Map_First_Point' : {'key' : ['mapId', 'map_location'], 'keytype' : 1}
	},
	'DropConf.xlsx' : {
		'DropConf' : {'key':['drop_id', 'index_id'], 'keytype': 1},
		'DropChildConf' : {'key':['drop_child_id', 'index_id'], 'keytype': 1},
		'DropLevel' : {'key':['drop_level_id', 'level_min'], 'keytype': 1}
	},
	'PetConf.xlsx' : {
		'Pet_Qualification' : {'key':['pet_id', 'qualification_type'], 'keytype' : 1},
		'Pet_Qualification_Value' : {'key':['Level', 'qualification_type'], 'keytype' : 1},
		'Skill_Cover' : {'key':['pet_sub_type', 'skill_quality'], 'keytype' : 1},
		'Pet_Value' : {'key':['pet_sub_type', 'base_attr'], 'keytype' : 1},
		'Mark' : {'key':['pet_sub_type', 'pet_index'], 'keytype' : 1}
	},
	'PetEquipConf.xlsx' : {
		'learning_library' : {'key':['learning_id', 'skill_id'], 'keytype' : 1},
		'attribute_library' : {'key':['attribute_library', 'attribute_id'], 'keytype' : 1}
	},
	'Questionbank.xlsx' : {
		'Question' : {'key':['question_library', 'question_id'], 'keytype' : 1},
		'DailyQA'  : {'key':['question_id', 'question_sub_id'], 'keytype' : 1},
		'QAquest_Con'  : {'key':['act_type', 'act_name'], 'keytype' : 1}
	},
	'TaskConfig.xlsx' : {
		'Task_Library' : {'key':['task_libraryid', 'task_index'], 'keytype' : 1}
	},
	'RideConf.xlsx' : {
		'Ride_step' : {'key':['ride_type', 'level'], 'keytype' : 1},
		'Passive_library' : {'key':['passive_library', 'index_id'], 'keytype' : 1}
	},
	"PVPConf.xlsx" : {
		'reward' : {'key' : ['id', 'level'], 'keytype' : 1},
		'matchtime': {'key' : ['id', 'grade'], 'keytype' : 1},
		'text' : {'key' : ['pvp_type', 'index'], 'keytype' : 1}
	},
	'FactionsConf.xlsx' : {
		'reward' : {'key': ['id', 'level'], 'keytype': 1},
		'correct' : {'key': ['correct_id', 'correct_type'], 'keytype': 1}
	},
	'Advanced.xlsx' : {
		'Refresh' : {'key': ['type', 'id'], 'keytype': 1},
		'condition' : {'key': ['type', 'Action'], 'keytype': 1},
		'switch' : {'key': ['quality', 'index_id'], 'keytype': 1},
		'fishfeel' : {'key': ['type', 'quality'], 'keytype': 1},
		'point' : {'key': ['type', 'point_id'], 'keytype': 1},
		'level' : {'key': ['type', 'level'], 'keytype': 1},
		'instrument' : {'key': ['type', 'prop_id'], 'keytype': 1},
		'mineralConf' : {'key': ['type', 'NuggetID'], 'keytype': 1},
		'qualityconf' : {'key': ['type', 'Action'], 'keytype': 1}
	},
	'ClickLive.xlsx' : {
		'Refresh' : {'key': ['type', 'id'], 'keytype': 1},
		'Site' : {'key': ['type', 'point_id'], 'keytype': 1},
		'DropId' : {'key': ['type', 'id'], 'keytype': 1},
		'CookicLevel' : {'key': ['level', 'id'], 'keytype': 1},
		'CookicProp' : {'key': ['cookic_site', 'prop_id'], 'keytype': 1}
	},
	'SpeakConf.xlsx' : {
		'speak_pool' : {'key': ['speak_pool_id', 'speak_words_id'], 'keytype': 1}
	},
	"SociatyConf.xlsx" : {
		'level' : {'key' : ['type_id', 'level'], 'keytype' : 1},
		'donate' : {'key' : ['type', 'multiple'], 'keytype' : 1},
		'Monster' : {'key' : ['heat', 'sequence'], 'keytype' : 1}
	},
	"FishChampion.xlsx" : {
		'Refresh' : {'key': ['type', 'id'], 'keytype': 1},
		'condition' : {'key': ['type', 'Action'], 'keytype': 1},
		'switch' : {'key': ['quality', 'index_id'], 'keytype': 1},
		'fishfeel' : {'key': ['type', 'quality'], 'keytype': 1},
		'point' : {'key': ['type', 'point_id'], 'keytype': 1},
		'level' : {'key': ['type', 'level'], 'keytype': 1},
		'instrument' : {'key': ['type', 'prop_id'], 'keytype': 1},
		'mineralConf' : {'key': ['type', 'NuggetID'], 'keytype': 1},
		'qualityconf' : {'key': ['type', 'Action'], 'keytype': 1}
	},
	"HuntingMonster.xlsx" : {
		'HuntingMonster' : {'key':['mapid', 'index_id'], 'keytype': 1},
		'MonsterPoint': {'key':['mapId', 'monster_point'], 'keytype': 1}
	},
	"LifeSkillConf.xlsx" : {
		'LifeSkillLevel' : {'key':['type', 'level'], 'keytype': 1},
		'Prop' : {'key':['type', 'quality'], 'keytype': 1}
	},
   "Study.xlsx" : {
        'person_study' : {'key':['Study_id', 'Study_level'], 'keytype': 1},
        'partner_study' : {'key':['Study_id', 'Study_level'], 'keytype': 1},
        'pet_study' : {'key':['Study_id', 'Study_level'], 'keytype': 1},
        'Study_level_limit' : {'key':['Limit_id', 'Study_level'], 'keytype': 1}

   },
	"TimingFighting.xlsx" : {
		'MapPoint' : {'key':['mapid', 'index_id'], 'keytype': 1},
		'Evil_mappoint' : {'key':['mapid', 'index_id'], 'keytype': 1}
	},
	"StoryCopy.xlsx" : {
		'StoryCopy' : {'key':['level', 'missionid'], 'keytype': 1}
	},
	"Auction.xlsx" : {
		'auction_item' : {'key':['auction_award', 'auction_index'], 'keytype': 1},
		"auction_act" : {'key':['actId', 'index'], 'keytype': 1}
	},
	"MapTransfer.xlsx" : {
		'transfer' : {'key':['mapId', 'desMapId'], 'keytype': 1}
	},
	"Formation.xlsx" : {
		'formationlevel' : {'key':['id', 'level'], 'keytype': 1}
	},
	"GemConf.xlsx" : {
		'gem' : {'key':['gem_type', 'gem_id'], 'keytype': 1}
	},
	"SkillLevelup.xlsx" : {
		'skill_awake' : {'key':['Skill_id', 'Skill_level'], 'keytype': 1}
	},
	"Awards.xlsx" : {
		'Daily_Gift' : {'key':['week', 'gift_type'], 'keytype': 1},
		'Signin_awards' : {'key':['month', 'date'], 'keytype': 1}
	},
	"Citytrade.xlsx" : {
		'Props_Detail' : {'key': ['Props_Group_id', 'Prop_index'], 'keytype': 1}
	},
	"Soulbrand.xlsx" : {
		'soulbrand' : {'key' : ['nature', 'id'], 'keytype': 1},
		'library' : {'key' : ['skill_library', 'index_id'], 'keytype': 1}
	},
	"Box.xlsx" : {
		'BoxPoints' : {'key' : ['map_id', 'mine_point_id'], 'keytype': 1}
	},
	"Wingconf.xlsx" : {
		'colors' : {'key' : ["wingid", "colors"], 'keytype': 1},
		'skilllibrary' : {'key' : ['skilllibrary', 'index'], 'keytype': 1}
	},
	"DungeonConfig.xlsx" : {
		'drop_grade' : {'key' : ['act_id', 'grade_id'], 'keytype': 1}
	},
	"Conversion.xlsx" : {
		'propid' : {'key' : ['type', 'prop_name'], 'keytype': 1}
	},
	"Manufacture.xlsx" : {
		'level' : {'key' : ['skill_type', 'level_index'], 'keytype': 1}
	},
	"Trade.xlsx" : {
		'coin_auto_put' : {'key' : ['trade_type1', 'trade_type2','trade_type3'], 'keytype': 1},
		'gold_auto_put' : {'key' : ['trade_type1', 'trade_type2','trade_type3'], 'keytype': 1}
	},

	"GuideConf.xlsx" : {
		'Group' : {'key' : ['groupid'], 'keytype' : 1}
	},
	"Rankings.xlsx" : {
		'award' : {'key' : ['id', 'floor'], 'keytype' : 1}
	},
	"ZodiacConf.xlsx" : {
		'zodiac_monster' : {'key':['date', 'map_id'], 'keytype': 1},
        'zodiac_boss' : {'key':['award_type', 'award_level'], 'keytype': 1}
	},
	"NewServerParty.xlsx" : {
		'NewServerParty' : {'key':['day_group', 'index'], 'keytype': 1}
	},
	"FashionEquip.xlsx" : {
		'Fashion_effect' : {'key' : ['effect_id', 'effect_type'], 'keytype': 1}
	},
	"HuntingList.xlsx" : {
		'HuntingTaskWeight' : {'key' : ['task_group', 'task_level'], 'keytype': 1}
	}
}
