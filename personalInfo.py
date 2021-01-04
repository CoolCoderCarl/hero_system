import methods
import sys_cmd

if __name__ == '__main__':

    if methods.namespace.hero == 'basic':
        methods.basicInfo()
    elif methods.namespace.hero == 'skills':
        methods.skillInfo()
    elif methods.namespace.hero == 'features':
        methods.featureInfo()
    elif sys_cmd.commands.hero == 'system':
        sys_cmd.systemCommands()

