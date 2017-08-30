from flask_assets import Bundle, Environment

# goes to the top of the body
# js_pre = Bundle(
# )

# goes to the bottom of the body
js_post = Bundle(
    'node_modules/jquery/dist/jquery.js',
    'node_modules/jquery-pjax/jquery.pjax.js',
    'node_modules/bootbox/bootbox.js',
    'node_modules/popper.js/dist/umd/popper.min.js',
    'node_modules/bootstrap/dist/js/bootstrap.min.js',
    'js/application.js',
    filters='jsmin',
    output='gen/packed.js')

css = Bundle(
    'node_modules/bootstrap/dist/css/bootstrap.css',
    'css/style.css',
    filters='cssmin',
    output='gen/packed.css')

assets = Environment()

assets.register('js_post', js_post)
assets.register('css_all', css)
