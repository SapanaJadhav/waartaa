from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('api_v1', '/api/v1')
    config.add_route('all', '/{all:.*}')
    config.scan()
    return config.make_wsgi_app()
