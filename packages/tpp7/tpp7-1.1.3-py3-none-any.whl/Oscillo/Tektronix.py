import pandas as pd
import scipy as sc
import matplotlib.pyplot as plt
import usbtmc
import uuid, os
import numpy as np

from .Oscillo import _Oscillo
        
class Tektronix(_Oscillo):
    __version__ = 'Tektronix-1.0.3'
    
    modelDict = {
    }
            
    def __init__(self, device = None, ident = (None, None)):
        super().__init__(device, ident)
    
    
    def getChannelList(self):
        self.instr.write('HEAD ON')
        rep = self.instr.ask('SEL?').split(':')[2]
        channelList = [st.split(' ')[0] for st in rep.split(';')]
        return channelList
    
    def getActiveChannelList(self):
        self.instr.write('HEAD ON')
        rep = self.instr.ask('SEL?').split(':')[2]
        channelList = [st.split(' ')[0] for st in rep.split(';') if st.split(' ')[1] == '1']
        return channelList
        
    
    def getChannelData(self, channel='CH1'): 
        self.instr.write("dat:sou "+channel)
        self.instr.write("DATa:ENCdg SRibinary")
        self.instr.write("DATa:WIDth 2")
        self.instr.write("WFMP:ENC BIN")
        self.instr.write("HEAD OFF")
        preamble =  self.instr.ask("WFMPre?").split(';')
        (xincr, ptoff, xzero, xunit, ymult, yzero, yoff, yunit) = [eval(st) for st in preamble[8:16]]
        self.instr.write("curve?")
        curve = self.instr.read_raw()
        V = yzero+ymult*(np.frombuffer(curve[6:-1], dtype=np.int16)-yoff)
        
        # V = yzero+ymult*(np.array([int(st) for st in curve])-yoff)        
        #self.instr.write("WFMP:ENC ASC")
        #curve = self.instr.ask("curve?")
        #V = yzero+ymult*(np.array([int(st) for st in curve.split(',')])-yoff)
        t = xzero+xincr*(np.arange(0,len(V))-ptoff)
        #return (t[6:-1],V[6:-1])
        return (t,V)
    
    def getHardcopy(self):
        self.instr.write("HEADER OFF")
        self.instr.write("HARDC:PORT USB")
        self.instr.write("HARDC:BUTTON SAVE")
        self.instr.write("HARDC:LAY PORTR")
        self.instr.write(f"HARDC:FORM {self.image_format}")
        self.instr.write("HARDC START")
        raw=self.instr.read_raw()
        filename = f"/tmp/{uuid.uuid4()}.{self.image_extension}"
        f = open(filename, "w+b")
        f.write(raw)
        f.close()
        im = plt.imread(filename)
        os.remove(filename)
        return im
