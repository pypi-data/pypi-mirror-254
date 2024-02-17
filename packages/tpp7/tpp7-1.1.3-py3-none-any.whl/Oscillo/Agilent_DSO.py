from .Agilent import Agilent


class DSO(Agilent):
    __version__ = 'Agilent-1.0.3'

    modelDict = {
        "DSO1024A": (0x0957, 0x0588),
    }

    def __init__(self, device = None, ident = (None, None), model= None):
        if model is None:
            super().__init__(device, ident)
            return
        if model in self.modelDict:
            super().__init__(ident = self.modelDict[model])
            return
        
        print('Liste des modèles de '+self.__class__.__name__+' référencés')
        print(self.modelDict)
        raise NameError("le modèle {} n'est pour le moment pas référencé".format(model))
        
   
