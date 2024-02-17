import os
from pangaeapy.exporter.pan_exporter import PanExporter

class PanODVExporter(PanExporter):

    #check if export is possible
    def verify(self):
        return True

    #create the export file (as IO object if possible)
    def create(self):
        return True

    #save the file  at self.filelocation
    def save(self):
        return True

    #return a string representation of the export file
    def __str__(self):
        return ''