import dominate
from dominate.tags import *
import os, os.path
import sys
from threading import Thread
import time

class HTMLCreator(Thread):
    
    def __init__(self, server):
        Thread.__init__(self, name="html_thread")
        
        self.server = server
        self.doc = dominate.document(title='Shopping list')
        self.table_headers = ['Product', 'Quantity']
        
        with self.doc.head:
            link(rel='stylesheet', href='style.css')

        with self.doc:
            with div(cls='container'):
                h1('Hello World!')
                with table(id='main', cls='table table-striped'):
                    caption(h3('A table to show data'))
                    with thead():
                        with tr():
                            for table_head in self.table_headers:
                                th(table_head)
                        self.body = tbody()
                        
    def create_html_doc(self):
        self.body.clear()
        with self.body:
            for key, value in self.server.model.items():
                with tr():
                    td(key)
                    td(value.quantity)
            

    def save_html_file(self):
        html_file = open(os.path.join(sys.path[0], "index.html"), "w")
        self.create_html_doc()    
        html_file.write(self.doc.render())
        html_file.close()
        
    def run(self):
        while True:
            self.save_html_file()
            time.sleep(2)


# MODEL = {'apples':4, 'grapes':15, 'tomatoes':103}

# html_file = HTMLCreator(MODEL)

# html_file.run()


