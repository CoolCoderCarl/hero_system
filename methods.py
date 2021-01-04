### METHODS FOR HERO INFO VIEW
import sys
import json
import parserDescription

### PARSERS
main_parser = parserDescription.createParser()
namespace = main_parser.parse_args(sys.argv[1:])

### HERO FILE
hero_file = 'hero_information.json'

###
### MAIN INFO ABOUT CHARACTER
###
def basicInfo():
    try:
        hfile = open(hero_file)
        hero_json = json.load(hfile)
        if namespace.basic_info:
            print('==================================')
            print('LEVEL: ', end='')
            print(hero_json['level'])
            print('CLASSES: ', end='')
            print(hero_json['class']['first'] + ', ' + hero_json['class']['second'])

        if namespace.param_info:
            print('==================================')
            print('PARAMETERS: ')
            print('----------------------------------')

            print(hero_json['parameters'][0][0], end=': ')
            print(hero_json['parameters'][0][1]['value'])

            print(hero_json['parameters'][1][0], end=': ')
            print(hero_json['parameters'][1][1]['value'])

            print(hero_json['parameters'][2][0], end=': ')
            print(hero_json['parameters'][2][1]['value'])

            print(hero_json['parameters'][3][0], end=': ')
            print(hero_json['parameters'][3][1]['value'])

            print(hero_json['parameters'][4][0], end=': ')
            print(hero_json['parameters'][4][1]['value'])

            print(hero_json['parameters'][5][0], end=': ')
            print(hero_json['parameters'][5][1]['value'])

            print(hero_json['parameters'][6][0], end=': ')
            print(hero_json['parameters'][6][1]['value'])

            print(hero_json['parameters'][7][0], end=': ')
            print(hero_json['parameters'][7][1]['value'])

    except IOError:
        print('Something went wrong')
    finally:
        hfile.close()


###
### SKILL INFO
###
def skillInfo():
    try:
        hfile = open(hero_file)
        hero_json = json.load(hfile)
        if namespace.skill_info:
            print('==================================')
            print('SKILLS')
            print('----------------------------------')

            print(hero_json['skills'][0][0], end='' + ': ')
            print(hero_json['skills'][0][1]['level'])

            print(hero_json['skills'][1][0], end='' + ': ')
            print(hero_json['skills'][1][1]['level'])

            print(hero_json['skills'][2][0], end='' + ': ')
            print(hero_json['skills'][2][1]['level'])

            print(hero_json['skills'][3][0], end='' + ': ')
            print(hero_json['skills'][3][1]['level'])

    except IOError:
        print('Something went wrong')
    finally:
        hfile.close()


###
### FEATURE INFO
###
def featureInfo():
    try:
        hfile = open(hero_file)
        hero_json = json.load(hfile)
        if namespace.features_info:
            print('FEATURES')
            print('----------------------------------')

            print(hero_json['features'][0][0], end='' + ': ')
            print(hero_json['features'][0][1]['level'])

            print(hero_json['features'][1][0], end='' + ': ')
            print(hero_json['features'][1][1]['level'])

            print(hero_json['features'][2][0], end='' + ': ')
            print(hero_json['features'][2][1]['level'])

            print(hero_json['features'][3][0], end='' + ': ')
            print(hero_json['features'][3][1]['level'])

    except IOError:
        print('Something went wrong')
    finally:
        hfile.close()
