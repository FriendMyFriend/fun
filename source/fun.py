class generate:
    def python(type):
        if (type == 'Hello World'):
            f = open('generated.py', 'w')
            f.write('print("Hello, World!")')
            f.close()
        elif (type == 'Template'):
            f = open('generated.py', 'w')
            f.write('def template(): print("Hello, World!")')
            f.close()
        else:
            print('Generator not found')

    def html(type):
        if (type == 'Hello World'):
            f = open('generated.html', 'w')
            f.write('<h1>Hello, World!</h1>')
            f.close()
        elif (type == 'Template'):
            f = open('generated.html', 'w')
            f.write('<!DOCTYPE html><html><head></head><body></body></html>')
            f.close()
        else:
            print('Generator not found')

    def javascript(type):
        if (type == 'Hello World'):
            f = open('generated.js', 'w')
            f.write('console.log("Hello, World");')
            f.close()
        elif (type == 'Template'):
            f = open('generated.js', 'w')
            f.write('function template() {console.log("Hello, World");}')
            f.close()
        else:
            print('Generator not found')