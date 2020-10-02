import dominate
from dominate.tags import *
import os, os.path
import sys
from threading import Thread
import time
from interfaces import IObserver

class HTMLCreator(IObserver,Thread):
    
    def __init__(self, model):
        Thread.__init__(self, name="html_thread")
        
        self.doc = dominate.document(title='Shopping list')
        self.table_headers = ['Product', 'Quantity']
        
        model.attach(self)
        
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
                        
    def create_html_doc(self, model):
        self.body.clear()
        with self.body:
            for key, value in model.items():
                with tr():
                    td(key)
                    td(value.quantity)
            

    def save_html_file(self, model):
        html_file = open(os.path.join(sys.path[0], "index.html"), "w")
        self.create_html_doc(model)    
        html_file.write(self.doc.render())
        html_file.close()
        
    # def run(self):
    #     while True:
    #         self.save_html_file()
    #         time.sleep(2)
            
        
    def update(self, subject):
        self.save_html_file(subject)
    
    def update_error(self, error):
        pass


# MODEL = {'apples':4, 'grapes':15, 'tomatoes':103}

# html_file = HTMLCreator(MODEL)

# html_file.run()


