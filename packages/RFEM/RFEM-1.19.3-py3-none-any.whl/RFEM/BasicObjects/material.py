from RFEM.initModel import clearAttributes, deleteEmptyAttributes, Model, ConvertStrToListOfInt
from RFEM.enums import ObjectTypes


class Material():
    def __init__(self,
                 no: int = 1,
                 name: str = 'S235',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Material Tag
            name (str): Name of Desired Material (As Named in RFEM Database)
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Material
        clientObject = model.clientModel.factory.create('ns0:material')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Material No.
        clientObject.no = no

        # Material Name
        clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add material to client model
        model.clientModel.service.set_material(clientObject)

    @staticmethod
    def DeleteMaterial(materials_no: str = '1 2', model = Model):

        '''
        Args:
            materials_no (str): Numbers of Materials to be deleted
            model (RFEM Class, optional): Model to be edited
        '''

        # Delete from client model
        for material in ConvertStrToListOfInt(materials_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_MATERIAL.name, material)

    @staticmethod
    def GetMaterial(object_index: int = 1, model = Model):

        '''
        Args:
            obejct_index (int): Material Index
            model (RFEM Class, optional): Model to be edited
        '''

        # Get Material from client model
        return model.clientModel.service.get_material(object_index)
