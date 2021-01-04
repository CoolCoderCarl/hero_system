### CREATE, BACKUP AND RESTORE COMMAND
import os
import sys
import json
import shutil
import parserDescription
from pathlib import Path

main_parser = parserDescription.createParser()
commands = main_parser.parse_args(sys.argv[1:])

###
### PATH FOR BACKUP AND RESTORE FILES
###
hero_file = 'hero_information.json'
hero_file_backup = 'hero_information.json.backup'
home_dir = str(Path.home()) + '/'
backup_dir = '/tmp/'
backupIs = (backup_dir + hero_file_backup)

###
### TEMPLATE OF HERO DESCRIBE
###
template_hero_describe = '''
{

  "boolean": true,
  "gender": null,
  "level": null,
  "maxlevel": null,

  "class": {
    "first": null,
    "second": null
  },

  "parameters": [
    ["strength", {
      "value": null,
      "description": "Hard physical",
      "source": null
    }],
    ["endurance", {
      "value": null,
      "description": "Hard physical",
      "source": "The Cooper test"
    }],
    ["dexterity", {
      "value": null,
      "description": "Soft physical",
      "source": null
    }],
    ["speed", {
      "value": null,
      "description": "Soft physical",
      "source": null
    }],
    ["intellect", {
      "value": null,
      "description": "Hard mental",
      "source": "The Eysenck Test"
    }],
    ["memory", {
      "value": null,
      "description": "Hard mental",
      "source": null
    }],
    ["willpower", {
      "value": null,
      "description": "Soft mental",
      "source": null
    }],
    ["charisma",{
      "value": null,
      "description": "Soft mental",
      "source": null
    }]
  ],

  "limitations": [
    null
  ],
  
  "diseases": [
    null
  ],

  "skills": [
    [
    null,
    {
      "description": null,
      "level": null,
      "technologies": {
        "network": null,
        "security": null,
        "data_bases": null,
        "programming": null,
        "operation_systems": null
      }
    }],
    {
      "description": "active"
    }
  ],

  "features": [
    [
    null,
    {
      "description": null,
      "level": null
    }],
    {
      "description": "passive"
    }
  ],
  
  "abilities": {
    "null": {
      "description": "null"
    },
  }
}
'''

def systemCommands():
###
### SHOW DEFAULT TEMPLATES
###
    if commands.show_template:
        print(template_hero_describe)

###
### CREATE FILE IF NOT EXIST
###
    if commands.template:
        if os.path.isfile(hero_file):
            print('FILE EXIST: ' + os.getcwd() + '/' + hero_file)
        elif os.path.isfile(backupIs):
            print('BACKUP EXIST')
            print('RUN personalInfo system --restore COMMAND')
        else:
            print('FILE NOT EXIST')
            print('GOING TO CREATE DEFAULT TEMPLATE...')
            with open(hero_file, 'w') as outfile:
                json.dump(template_hero_describe, outfile)

###
### BACKUP FILE
###
    if commands.backup:
        ### HOME DIRECTORY OF CURRENT USER
        src_dir = home_dir
        ### FILE LOCATED IN CURRENT USER DIRECTORY
        src_file = os.path.join(src_dir + hero_file)
        print('SAVE FILE TO ' + backupIs)
        shutil.copy(src_file, backupIs)

###
### RESTORE FILE
###
    if commands.restore:
        if os.path.isfile(backupIs):
            restore_dir = home_dir
            shutil.copy(backupIs, restore_dir)
            print('SUCCESS')
        else:
            print('BACKUP IS NOT EXIST')
            print('RUN personalInfo system --backup COMMAND')
