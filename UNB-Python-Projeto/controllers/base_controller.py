from bottle import static_file

class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()


    def _setup_base_routes(self):
        """Configura rotas básicas comuns a todos os controllers"""
        self.app.route('/', method='GET', callback=self.home_redirect)  

        # Rota para arquivos estáticos (CSS, JS, imagens)
        self.app.route('/static/<filename:path>', callback=self.serve_static)
        self.app.route('/helper',callback=self.helper)#rota da helper criei pq n achie outra.


    def home_redirect(self):
        """Redireciona a rota raiz para /users"""
        return self.redirect('/home')


    def helper(self):
        return self.render('helper-final')


    def serve_static(self, filename):
        """Serve arquivos estáticos da pasta static/"""
        return static_file(filename, root='./static')


    def render(self, template, **context):
        """Método auxiliar para renderizar templates"""
        from bottle import template as render_template
        return render_template(template, **context)#template-> o nome do arquivo tpl que eu quero renderizr 
        # **context -> action , obj -> são variáveis que o template pode usar para montar o HTML.


    def redirect(self, path, code=302):
        """Redirecionamento robusto com tratamento de erros"""
        from bottle import HTTPResponse, response as bottle_response
        
        try:
            bottle_response.status = code
            bottle_response.set_header('Location', path)
            return bottle_response
        except Exception as e:
            print(f"ERRO NO REDIRECT: {type(e).__name__} - {str(e)}")
            return HTTPResponse(
                body=f'<script>window.location.href="{path}";</script>',
                status=200,
                headers={'Content-Type': 'text/html'}
            )