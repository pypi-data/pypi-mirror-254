from sqlalchemy.orm import scoped_session, sessionmaker

from connect_extension_utils.db.models import VerboseBaseSession


Session = scoped_session(sessionmaker(class_=VerboseBaseSession))
