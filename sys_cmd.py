### CREATE, BACKUP AND RESTORE COMMAND
import os
import sys
import json
import shutil
import parserDescription
from pathlib import Path

main_parser = parserDescription.createParser()
namespace = main_parser.parse_args(sys.argv[1:])

###
### PATH FOR BACKUP AND RESTORE
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
      "value": null
    }],
    ["dexterity", {
      "value": null
    }],
    ["speed", {
      "value": null
    }],
    ["vitality", {
    "value": null
    }],
    ["intellect", {
      "value": null
    }],
    ["willpower", {
      "value": null
    }],
    ["charisma",{
      "value": null
    }]
  ],

  "limitations": [
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
      "description": null
    }
  ],
  
  "abilities": {
    "null": {
      "description": "null"
    },
  }
}
'''
###
### CREATE FILE IF NOT EXIST
###
def createFromTemplate():
    if namespace.template:
        if os.path.isfile(hero_file):
            print('FILE EXIST')
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
def backUpFile():
    if namespace.backup:
        src_dir = home_dir
        src_file = os.path.join(src_dir + hero_file)
        print('SAVE FILE TO ' + backupIs)
        shutil.copy(src_file, backupIs)

###
### RESTORE FILE
###
def restoreBackFile():
    if namespace.restore:
        if os.path.isfile(backupIs):
            restore_dir = home_dir
            shutil.copy(backupIs, restore_dir)
            print('SUCCESS')
        else:
            print('BACKUP IS NOT EXIST')
