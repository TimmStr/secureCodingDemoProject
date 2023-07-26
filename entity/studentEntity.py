from pony import orm
from path.paths import Paths
from utils.utils import create_path

db = orm.Database()


class StudentEntity(db.Entity):
    firstname = orm.Required(str)
    lastname = orm.Required(str)
    birthday = orm.Required(str)
    city = orm.Optional(str)


create_path(Paths.DATABASE)
db.bind(provider='sqlite', filename='../' + Paths.SQLITE, create_db=True)
db.generate_mapping(create_tables=True)
