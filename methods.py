import json
import sys
import parserDescription

main_parser = parserDescription.createParser()
namespace = main_parser.parse_args(sys.argv[1:])

###
### MAIN INFO ABOUT CHARACTER
###
def basicInfo():
  if namespace.basic_info:
    with open('test.json') as data_json:
        datest = json.load(data_json)
        print('==================================')
        print('LEVEL: ', end='')
        print(datest['level'])
        print('==================================')
###
### SKILL INFO
###
def skillInfo():
  if namespace.skill_info:
    with open('test.json') as data_json:
        datest = json.load(data_json)
        print('SKILLS')
        print('----------------------------------')

        print(datest['skills'][0][0], end='' + ': ')
        print(datest['skills'][0][1]['level'])

        print(datest['skills'][1][0], end='' + ': ')
        print(datest['skills'][1][1]['level'])

        print(datest['skills'][2][0], end='' + ': ')
        print(datest['skills'][2][1]['level'])

        print(datest['skills'][3][0], end='' + ': ')
        print(datest['skills'][3][1]['level'])
###
### FEATURE INFO
###
def featureInfo():
  if namespace.features_info:
    with open('test.json') as data_json:
        datest = json.load(data_json)
        print('FEATURES')
        print('----------------------------------')

        print(datest['features'][0][0], end='' + ': ')
        print(datest['features'][0][1]['level'])

        print(datest['features'][1][0], end='' + ': ')
        print(datest['features'][1][1]['level'])

        print(datest['features'][2][0], end='' + ': ')
        print(datest['features'][2][1]['level'])

        print(datest['features'][3][0], end='' + ': ')
        print(datest['features'][3][1]['level'])

