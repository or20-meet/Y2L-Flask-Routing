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

def edit_name(id, name ):
	prod = session.query(Product).filter_by(id = id)
	prod.name = name
	session.commit()

def edit_price(id, price):
	prod = session.query(Product).filter_by(id=id)
	prod.price = price
	session.commit()

def edit_link(id, link):
	prod = session.query(Product).filter_by(id=id)
	prod.link = link
	session.commit()

def edit_description(id, description):
	prod = session.query(Product).filter_by(id=id)
	prod.description = description
	session.commit()

def delete_product(id):
	session.query(Product).filter_by(id = id).delete()
	session.commit()

def all_products():
	products = session.query(Product).all()
	return products

def get_product(id):
	prod = session.query(Product).filter_by(id=id)
	return prod



def add_to_cart(productid):
	item = Cart(productID = productid)
	session.add(item)
	session.commit()

def all_cart_items():
	items = session.query(Cart).all()
	return items