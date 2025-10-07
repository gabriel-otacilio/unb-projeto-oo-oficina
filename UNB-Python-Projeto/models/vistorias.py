import os
from models.user import DATA_DIR
from models.carro import Carro,CarrosModel
from models.problema import Problema


class Vistoria:
    def __init__(self,id,carro_id,status,funcionarios_id=None,prazo=''):
        self.id=id
        self.carro_id=carro_id# aqui eu to passando  objeto 
        self.funcionarios_id=funcionarios_id if funcionarios_id is not None else []
        self.prazo=prazo
        self.status=status
        
    def to_dict(self):
        return{
            'id':self.id,
            'carro_id':self.carro_id.to_dict() if isinstance(self.carro_id, Carro) else self.carro_id,
            'funcionarios_id':self.funcionarios_id,
            'prazo': self.prazo,
            'status':self.status
        }
        
    @classmethod
    def from_dict(cls,data):
        return cls(
            id=data['id'],
            carro_id=data['carro_id'],
            funcionarios_id=data['funcionarios_id'],
            prazo=data['prazo'],
            status=data['status']
            
        )
        

   
        
        
        
        
        
                                   
        
        

class VistoriasModel:
    FILE_PATH = os.path.join(DATA_DIR, 'vistorias.json')
    def __init__(self):
        
        self.vistorias=self._load()
        
    def _load(self):
        import json,os
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH,'r', encoding='utf-8') as f:
            return [Vistoria.from_dict(item) for item in json.load(f)]
        
    def _save(self):
        import json
        with open (self.FILE_PATH,'w', encoding='utf-8') as f:
            json.dump([a.to_dict() for a  in self.vistorias], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.vistorias
    
    def get_by_id(self, vistoria_id):#retorna o objeto
        return next((a for a in self.vistorias if a.id == vistoria_id), None)
    
    def add(self, vistoria):
        self.vistorias.append(vistoria)
        self._save()

   
    def update(self, updated_vistorias):
        for i ,a in enumerate(self.vistorias):
            if a.id == updated_vistorias.id:
                self.vistorias[i] = updated_vistorias
                self._save()
                break
    def delete(self,vistoria_id):
        self.vistorias= [a for a in self.vistorias if a.id != vistoria_id]
        self._save()

      
        
    
         
        