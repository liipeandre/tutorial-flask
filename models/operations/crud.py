from database import database


# TODO: As principais operações de dados, dentro de um model são as abaixo.

def insert(registry):
    database.session.add(registry)


def delete(registry):
    database.session.delete(registry)


def list(model: database.Model):
    return model.query.all()


def view(model: database.Model, id):
    return model.query.get(id)


def edit(model: database.Model, fields):
    registry = view(model, fields['id'])

    for key, value in zip(fields.keys, fields.values):
        setattr(registry, str(key), value)

    insert(registry)
