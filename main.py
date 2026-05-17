# #models.py
# from enum import StrEnum
#
# from sqlalchemy import Integer
#
#
# class Patient(Base):
#     __table_name__ = 'patients'
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     age = Column(Integer)
#     gender = Column(String)
#     contact = Column(String)
#
#
# #schemas.py
#
# class PatientBase(Basemodel):
#     name : str
#     age : int
#     gender : str
#
#
#
#
#
#
#
#
#
# inp_data = {
#     'nme': 'a',
#     'age': 10,
#     'addr': 'BLR'
# }
#
# import json
#
#
# import pickle
#
# with open('data.pkl', 'wb') as file_obj:
#     pickle.dump(inp_data, file_obj)
#
# with open('data.pkl', 'rb') as file_obj:
#     loaded_data = pickle.load(file_obj)
#
#
# json_data = json.dumps(loaded_data, indent=4)
# print(json_data)



# def reversewords(sentence):
#     return ' '.join(sentence.split()[::-1])
#
# print(reversewords("gk lk"))

from pathlib import Path
from pdf2image import convert_from_path

traning_data = Path(r'E:\demo\Test samples')

images = Path(r'E:\demo\Output_images')

cfg = {"poppler_path": r'E:\demo\poppler-25.12.0\Library\bin', "dpi": 300}



for pdf in traning_data.glob("*.pdf"):
    pages = convert_from_path(pdf, **cfg)
    for i, page in enumerate(pages, 1):
        page.save(images / f"{pdf.stem}_{i}.jpg", "JPEG")

print("Done")



# Hello
