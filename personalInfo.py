import methods

if __name__ == '__main__':

    if methods.namespace.show == 'basic':
        methods.basicInfo()
    elif methods.namespace.show == 'skills':
        methods.skillInfo()
    elif methods.namespace.show == 'features':
        methods.featureInfo()
