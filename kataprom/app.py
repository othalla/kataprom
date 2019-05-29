import connexion


def post_greeting(name: str) -> str:
    return 'Hello {name}'.format(name=name)


app = connexion.FlaskApp(__name__,
                         port=8080,
                         specification_dir='swagger/',
                         options={"swagger_ui": True})
app.add_api('my_api.yaml', arguments={'title': 'Hello World Example'})
app.run()
