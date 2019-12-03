from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, link, description):
	new_prod = Product(name = name, price = price, link = link, description = description)
	session.add(student_object)
	sessin.commit()

def edit_product(id):
	prod = session.query(Product).filter_by(id = id)
	prod
